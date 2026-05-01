from __future__ import annotations

from django.conf import settings
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
    TEAM_GROUPS,
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
            'AI, Software & Web Development Studio',
            'Axial Foundry is a software and AI studio building websites, web applications, automation, and applied AI for startups, SMEs, and enterprise teams.',
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


def extra(request: HttpRequest) -> HttpResponse:
    """Holding page for the sections relocated from the home page:
    What clients can expect (process), Featured work, and Meet the owner.
    Kept reachable so these can be linked to or embedded elsewhere later."""
    return render(
        request,
        'core/extra.html',
        page_context(
            'Delivery model, featured work, and founder credibility',
            'Extra reference material from Axial Foundry: delivery model, featured work, and founder credibility.',
            process_steps=PROCESS_STEPS,
            featured_work=CASE_STUDIES[:4],
            authority_points=AUTHORITY_POINTS,
        ),
    )


def services(request: HttpRequest) -> HttpResponse:
    services_jsonld = (
        '{"@type":"ItemList","name":"Axial Foundry services",'
        '"itemListElement":['
        '{"@type":"ListItem","position":1,"item":{"@type":"Service",'
        '"name":"AI Systems","description":"AI consulting, chatbots, RAG, prompt engineering, LLM fine-tuning, speech AI, and custom AI workflows.",'
        '"provider":{"@id":"' + (settings.SITE_URL or '') + '#organization"}}},'
        '{"@type":"ListItem","position":2,"item":{"@type":"Service",'
        '"name":"Software Products","description":"Custom web apps, internal tools, portals, SaaS MVPs, backend APIs, and product engineering.",'
        '"provider":{"@id":"' + (settings.SITE_URL or '') + '#organization"}}},'
        '{"@type":"ListItem","position":3,"item":{"@type":"Service",'
        '"name":"Premium Websites","description":"Premium business websites, landing pages, CMS sites, redesigns, and performance work.",'
        '"provider":{"@id":"' + (settings.SITE_URL or '') + '#organization"}}},'
        '{"@type":"ListItem","position":4,"item":{"@type":"Service",'
        '"name":"Automation and Data Systems","description":"Workflow automation, CRM integrations, data pipelines, web scraping, and monitoring dashboards.",'
        '"provider":{"@id":"' + (settings.SITE_URL or '') + '#organization"}}}'
        ']}'
    )
    return render(
        request,
        'core/services.html',
        page_context(
            'AI Services, Custom Software & Web Development',
            'AI assistants, RAG systems, LLM fine-tuning, custom web apps, premium websites, and workflow automation \u2014 four delivery tracks from one studio.',
            service_clusters=SERVICE_CLUSTERS,
            service_details=SERVICE_DETAILS,
            jsonld_extra=services_jsonld,
            breadcrumb_trail=[
                {'name': 'Home', 'url': '/'},
                {'name': 'Services', 'url': '/services/'},
            ],
        ),
    )


def who_we_help(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        'core/who_we_help.html',
        page_context(
            'Who We Help \u2014 Startups, SMEs, Agencies, Enterprise Teams',
            'Software, AI, and automation engagements shaped around your team \u2014 whether you\u2019re a startup, SME, agency, or enterprise group running a pilot.',
            audience_solutions=AUDIENCE_SOLUTIONS,
            need_map=NEED_MAP,
            engagement_paths=ENGAGEMENT_PATHS,
            breadcrumb_trail=[
                {'name': 'Home', 'url': '/'},
                {'name': 'Who We Help', 'url': '/who-we-help/'},
            ],
        ),
    )


def work(request: HttpRequest) -> HttpResponse:
    site_url = settings.SITE_URL or ''
    work_jsonld = (
        '{"@type":"ItemList","name":"Selected work and case studies",'
        '"itemListElement":['
        '{"@type":"ListItem","position":1,"item":{"@type":"CreativeWork",'
        '"name":"CRM-connected WhatsApp assistant for a B2B medical equipment distributor",'
        '"description":"A multi-turn customer support assistant that handles enquiries on WhatsApp, grounds answers in product documentation, and stays connected to the distributor sales workflow.",'
        '"creator":{"@id":"' + site_url + '#organization"},'
        '"url":"' + site_url + '/work/#medical-distributor-whatsapp-assistant"}},'
        '{"@type":"ListItem","position":2,"item":{"@type":"CreativeWork",'
        '"name":"Large-scale data infrastructure for a restaurant intelligence platform",'
        '"description":"A scraping and monitoring layer collecting structured data on more than one million restaurants, with operational dashboards built so the client team could see pipeline health at a glance.",'
        '"creator":{"@id":"' + site_url + '#organization"},'
        '"url":"' + site_url + '/work/#restaurant-intelligence-data-platform"}}'
        ']}'
    )
    return render(
        request,
        'core/work.html',
        page_context(
            'Selected Work & Case Studies',
            'Anonymised case studies including a CRM-connected WhatsApp assistant for a B2B medical distributor and data infrastructure for a UK platform.',
            case_studies=CASE_STUDIES,
            jsonld_extra=work_jsonld,
            breadcrumb_trail=[
                {'name': 'Home', 'url': '/'},
                {'name': 'Work', 'url': '/work/'},
            ],
        ),
    )


def about(request: HttpRequest) -> HttpResponse:
    site_url = settings.SITE_URL or ''
    about_jsonld = (
        '{"@type":"AboutPage","name":"About Axial Foundry",'
        '"url":"' + site_url + '/about/",'
        '"about":{"@id":"' + site_url + '#organization"}}'
    )
    return render(
        request,
        'core/about.html',
        page_context(
            'About the Studio \u2014 AI Engineering & Software Team',
            'Axial Foundry is a hand-picked team of AI engineers, software developers, designers, and GIS specialists. Founder-led delivery and shipped work.',
            capability_groups=CAPABILITY_GROUPS,
            team_groups=TEAM_GROUPS,
            jsonld_extra=about_jsonld,
            breadcrumb_trail=[
                {'name': 'Home', 'url': '/'},
                {'name': 'About the Studio', 'url': '/about/'},
            ],
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
