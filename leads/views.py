from __future__ import annotations

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ContactForm
from .models import Lead
from .utils import consume_rate_limit, get_client_ip, send_lead_notification


SUCCESS_MESSAGE = 'Your information has been submitted successfully. Our team will review the brief and contact you directly.'


def wants_json(request: HttpRequest) -> bool:
    accepts = request.headers.get('Accept', '')
    return 'application/json' in accepts or request.headers.get('X-Requested-With') == 'XMLHttpRequest'


def serialize_form_errors(form: ContactForm) -> dict[str, str]:
    errors: dict[str, str] = {}
    for field_name, field_errors in form.errors.items():
        if field_errors:
            errors[field_name] = field_errors[0]
    return errors


def contact_view(request: HttpRequest) -> HttpResponse:
    submitted = request.GET.get('submitted') == '1'
    submitted_mode = request.GET.get('mode', 'guided')

    if request.method == 'POST':
        submitted_mode = request.POST.get('submission_mode', 'guided')
        form = ContactForm(request.POST)
        ip_address = get_client_ip(request)
        allowed, retry_after = consume_rate_limit(ip_address)

        if not allowed:
            message = 'Too many submissions from this connection. Please try again a little later.'
            if wants_json(request):
                return JsonResponse({'ok': False, 'message': message, 'retry_after': retry_after}, status=429)
            messages.error(request, message)
        elif form.is_valid():
            lead = form.save(commit=False)
            lead.ip_address = ip_address or None
            lead.user_agent = request.META.get('HTTP_USER_AGENT', '')[:1000]
            lead.referrer = request.POST.get('referrer', '')[:500]

            honeypot_value = form.cleaned_data.get('website', '').strip()
            if honeypot_value:
                lead.is_spam = True
            lead.save()

            if not lead.is_spam:
                send_lead_notification(lead)

            if wants_json(request):
                return JsonResponse(
                    {
                        'ok': True,
                        'message': SUCCESS_MESSAGE,
                        'panel_title': 'Project enquiry received',
                        'next_steps': [
                            'We will review the brief, scope, and service fit.',
                            'You will receive a direct response with next-step recommendations.',
                            'If needed, we will suggest a discovery call or a practical starting scope.',
                        ],
                    }
                )

            messages.success(request, SUCCESS_MESSAGE)
            return redirect(f"{reverse('leads:contact')}?submitted=1&mode={submitted_mode}#contact-experience")
        else:
            if wants_json(request):
                return JsonResponse(
                    {
                        'ok': False,
                        'message': 'Please review the highlighted fields and try again.',
                        'errors': serialize_form_errors(form),
                    },
                    status=400,
                )
            messages.error(request, 'Please review the highlighted fields and try again.')
    else:
        form = ContactForm(initial={'inquiry_type': Lead.InquiryType.PROJECT})

    return render(
        request,
        'leads/contact.html',
        {
            'page_title': 'Contact',
            'meta_description': 'Start a conversation with Axial Foundry about software, AI, websites, automation, or product delivery.',
            'og_title': 'Contact',
            'og_description': 'Get in touch with Axial Foundry about software, AI, web development, automation, and product builds.',
            'form': form,
            'submitted': submitted,
            'submitted_mode': submitted_mode,
            'success_message': SUCCESS_MESSAGE,
            'service_choices': Lead.ServiceInterest.choices,
            'budget_choices': Lead.Budget.choices,
        },
    )


@staff_member_required
def dashboard(request: HttpRequest) -> HttpResponse:
    query = request.GET.get('q', '').strip()
    queryset = Lead.objects.all()
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query)
            | Q(email__icontains=query)
            | Q(company__icontains=query)
            | Q(message__icontains=query)
            | Q(phone__icontains=query)
        )
    paginator = Paginator(queryset, 25)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(
        request,
        'leads/dashboard.html',
        {
            'page_title': 'Leads dashboard',
            'meta_description': 'Internal leads dashboard.',
            'query': query,
            'page_obj': page_obj,
            'lead_count': queryset.count(),
        },
    )
