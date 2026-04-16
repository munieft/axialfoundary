from __future__ import annotations

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.defaults import page_not_found

from .content import (
    ABOUT_PRINCIPLES,
    AUDIENCE_SOLUTIONS,
    AUTHORITY_POINTS,
    BRAND_STORY,
    CAPABILITY_GROUPS,
    CASE_STUDIES,
    EXPERTISE_CARDS,
    FAQS,
    ENGAGEMENT_PATHS,
    FEATURED_SOLUTIONS,
    INSIGHT_TOPICS,
    NEED_MAP,
    POSITIONING_STATEMENT,
    PROCESS_STEPS,
    PUBLICATION_HIGHLIGHTS,
    SERVICE_CLUSTERS,
    SERVICE_DETAILS,
    WHY_CHOOSE,
)


def page_context(title: str, description: str, **extra):
    return {
        'page_title': title,
        'meta_description': description,
        'og_title': title,
        'og_description': description,
        **extra,
    }


def home(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        'core/home.html',
        page_context(
            'Software, AI, and digital systems for ambitious teams',
            'Axial Foundry is a premium software and AI studio building websites, custom applications, automation, and AI systems for startups, SMEs, agencies, and enterprise teams.',
            brand_story=BRAND_STORY,
            positioning_statement=POSITIONING_STATEMENT,
            authority_points=AUTHORITY_POINTS,
            service_clusters=SERVICE_CLUSTERS,
            why_choose=WHY_CHOOSE,
            featured_solutions=FEATURED_SOLUTIONS,
            engagement_paths=ENGAGEMENT_PATHS,
            process_steps=PROCESS_STEPS,
            featured_work=CASE_STUDIES[:4],
            faqs=FAQS,
        ),
    )


def services(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        'core/services.html',
        page_context(
            'Services',
            'Explore Axial Foundry services across AI systems, custom software, websites, automation, and data delivery.',
            service_clusters=SERVICE_CLUSTERS,
            service_details=SERVICE_DETAILS,
        ),
    )


def solutions(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        'core/solutions.html',
        page_context(
            'Solutions and industries',
            'See how Axial Foundry helps startups, SMEs, agencies, enterprise teams, and knowledge-heavy organizations solve product, operations, and AI delivery challenges.',
            audience_solutions=AUDIENCE_SOLUTIONS,
            need_map=NEED_MAP,
            featured_solutions=FEATURED_SOLUTIONS,
            engagement_paths=ENGAGEMENT_PATHS,
        ),
    )


def work(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        'core/work.html',
        page_context(
            'Work and case studies',
            'Representative case studies across AI systems, speech workflows, product engineering, automation, and data infrastructure.',
            case_studies=CASE_STUDIES,
        ),
    )


def about(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        'core/about.html',
        page_context(
            'About the Studio',
            'Learn how Axial Foundry combines product thinking, software engineering, and research-backed AI delivery for practical business outcomes.',
            brand_story=BRAND_STORY,
            positioning_statement=POSITIONING_STATEMENT,
            about_principles=ABOUT_PRINCIPLES,
            capability_groups=CAPABILITY_GROUPS,
            process_steps=PROCESS_STEPS,
            authority_points=AUTHORITY_POINTS,
        ),
    )


def insights(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        'core/insights.html',
        page_context(
            'Insights and research',
            'Research-backed perspectives on AI systems, product engineering, speech workflows, evaluation, and implementation strategy.',
            publication_highlights=PUBLICATION_HIGHLIGHTS,
            insight_topics=INSIGHT_TOPICS,
            expertise_cards=EXPERTISE_CARDS,
        ),
    )


def privacy(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        'core/privacy.html',
        page_context(
            'Privacy policy',
            'Privacy information for Axial Foundry website visitors and contact form submissions.',
        ),
    )


def robots_txt(request: HttpRequest) -> HttpResponse:
    response = render(request, 'robots.txt', {})
    response['Content-Type'] = 'text/plain; charset=utf-8'
    return response


def health_check(request: HttpRequest) -> JsonResponse:
    return JsonResponse({'status': 'ok'})


def custom_404(request: HttpRequest, exception) -> HttpResponse:
    return page_not_found(request, exception, template_name='404.html')
