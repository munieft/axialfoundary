Axial Foundry updated codebase export

Project tree
.env.example
.gitignore
DELIVERY_SUMMARY.md
DELIVERY_UPDATE.md
DEPLOYMENT_NOTES.md
FULL_CODEBASE.md
PROJECT_TREE.txt
README.md
axialfoundry/__init__.py
axialfoundry/asgi.py
axialfoundry/settings.py
axialfoundry/urls.py
axialfoundry/wsgi.py
core/__init__.py
core/apps.py
core/content.py
core/context_processors.py
core/sitemaps.py
core/templatetags/__init__.py
core/urls.py
core/views.py
leads/__init__.py
leads/admin.py
leads/apps.py
leads/forms.py
leads/migrations/0001_initial.py
leads/migrations/__init__.py
leads/models.py
leads/urls.py
leads/utils.py
leads/views.py
manage.py
requirements.txt
static/css/theme.css
static/img/blue-beams.jpg
static/img/blue-beams.webp
static/img/circuit-touch.jpg
static/img/circuit-touch.webp
static/img/code-laptop.jpg
static/img/code-laptop.webp
static/img/fiber-cables.jpg
static/img/fiber-cables.webp
static/img/hero-network.jpg
static/img/hero-network.webp
static/img/originals/blue-beams.jpg
static/img/originals/circuit-touch.jpg
static/img/originals/code-laptop.jpg
static/img/originals/fiber-cables.jpg
static/img/originals/hero-network.jpg
static/js/main.js
static/svg/favicon.svg
static/svg/logo-mark.svg
static/svg/logo.svg
static/svg/og-card.svg
templates/404.html
templates/base.html
templates/core/about.html
templates/core/home.html
templates/core/insights.html
templates/core/privacy.html
templates/core/services.html
templates/core/solutions.html
templates/core/work.html
templates/includes/cta_band.html
templates/includes/faq_item.html
templates/includes/footer.html
templates/includes/header.html
templates/includes/hero_visual.html
templates/includes/owner_section.html
templates/includes/page_header.html
templates/includes/page_visual.html
templates/includes/service_graphic.html
templates/includes/theme_toggle.html
templates/leads/contact.html
templates/leads/contact_email.html
templates/leads/contact_email.txt
templates/leads/dashboard.html
templates/robots.txt

============================================================
FILE: .env.example
============================================================
DEBUG=True
SECRET_KEY=change-me-in-production
ALLOWED_HOSTS=127.0.0.1,localhost
CSRF_TRUSTED_ORIGINS=http://127.0.0.1:8000,http://localhost:8000
SITE_URL=http://127.0.0.1:8000

CONTACT_EMAIL=mhtgcu18@gmail.com
CONTACT_PHONE=+92 323 5809900
CONTACT_LOCATION=Lahore, Pakistan
LEADS_NOTIFICATION_EMAIL=mhtgcu18@gmail.com
OWNER_PROFILE_URL=

DATABASE_URL=sqlite:///db.sqlite3

EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
DEFAULT_FROM_EMAIL=studio@axialfoundry.local

RATE_LIMIT_WINDOW_SECONDS=900
RATE_LIMIT_MAX_SUBMISSIONS=5
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False
SECURE_SSL_REDIRECT=False
LOG_LEVEL=INFO


============================================================
FILE: .gitignore
============================================================
__pycache__/
*.py[cod]
*.sqlite3
.env
.venv/
venv/
staticfiles/
node_modules/
.DS_Store


============================================================
FILE: DELIVERY_SUMMARY.md
============================================================
# Axial Foundry — Delivery Summary

## 1. Final selected brand name
Axial Foundry

## 2. Final slogan/tagline
Software, AI, and digital systems built to move business forward.

## 3. Short brand rationale
Axial suggests structure, alignment, and technical precision. Foundry signals craft, build quality, and hands-on execution. Together, the name feels premium, globally usable, and broad enough to cover websites, software products, automation, and AI systems without boxing the studio into one narrow capability.

## 4. Visual identity summary
- **Palette:** Ink `#08111F`, Steel `#0F172A`, Brand Blue `#1870F8`, Brand Light `#4799FF`, Accent Mint `#4EE7C2`, Mist `#DCE6F3`
- **Typography:** Space Grotesk for headings, Inter for body copy
- **Buttons:** Rounded pill buttons with a strong cobalt primary and soft glass secondary
- **Icon treatment:** Minimal outline SVG icons inside rounded glass chips
- **Layout:** Wide-content grid, generous spacing rhythm, dark premium surfaces, restrained gradients, and subtle grid overlays

## 5. Sitemap
- Home
- Services
- Solutions
- Work
- About the Studio
- Insights
- Contact
- Privacy Policy
- 404 page
- Internal leads dashboard (staff only)

## 6. Tech architecture summary
- Django 5 project with `core` and `leads` apps
- SQLite by default, PostgreSQL-ready via `DATABASE_URL`
- WhiteNoise static asset delivery
- Tailwind utility classes via CDN plus custom theme CSS
- Alpine.js for lightweight interactions
- Django ORM lead persistence
- Django admin plus protected staff dashboard for leads
- SMTP-ready notification hook with console backend default for local development
- Honeypot anti-spam and cache-based rate limiting
- SEO basics: Open Graph, sitemap, robots.txt, canonical tags, favicon, and custom 404

## 7. Full project folder tree
See `PROJECT_TREE.txt`.

## 8. Complete code for every file
See `FULL_CODEBASE.md`.

## 9. Django models
See `leads/models.py`.

## 10. .env.example
See `.env.example`.

## 11. requirements.txt
See `requirements.txt`.

## 12. README.md with setup and run instructions
See `README.md`.

## 13. Deployment notes
See `DEPLOYMENT_NOTES.md`.


============================================================
FILE: DELIVERY_UPDATE.md
============================================================
Axial Foundry visual refinement update

What changed in this pass
- Rebuilt the theme toggle into a proper switch and fixed light-mode contrast so headings, navigation, gradient accents, hover states, confirmation panels, and ambient backgrounds remain readable.
- Converted the homepage hero into a rotating multi-slide service carousel with autoplay, manual navigation, dot indicators, swipe support, and a more product-led visual structure.
- Converted page-header visuals into reusable carousels so Services, About, Solutions, Work, Insights, Contact, and Privacy now feel more alive instead of relying on static single-image panels.
- Added stronger hover and motion treatment to key cards including authority cards, service clusters, overview stats, solution cards, and supporting interface elements.
- Reworked the Studio Overview panel so the right side now carries meaningful visual content, supporting micro-cards, and a clearer product-partner feel.
- Simplified the footer navigation so it no longer uses oversized pill bars that compete with the layout.
- Reworked the guided contact intake to use a scrollable step rail, more stable panel sizing, improved small-screen behavior, and a cleaner confirmation modal after successful submission.
- Added a Meet the team section on the About page with fixed-ratio placeholder image blocks so real team photos can be swapped in later without breaking layout.
- Added responsive polish for mobile layouts across the hero, wizard actions, carousel controls, and page visuals.

Key files updated in this pass
- templates/includes/theme_toggle.html
- templates/includes/hero_visual.html
- templates/includes/page_visual.html
- templates/includes/footer.html
- templates/core/home.html
- templates/core/about.html
- templates/core/services.html
- templates/leads/contact.html
- static/css/theme.css
- static/js/main.js

Validation performed
- Python syntax compilation passed.
- JavaScript syntax check passed.
- Template block nesting check passed.


============================================================
FILE: DEPLOYMENT_NOTES.md
============================================================
# Deployment notes

## 1. Production environment variables

At minimum, set the following for production:

```env
DEBUG=False
SECRET_KEY=replace-with-a-strong-secret
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
CSRF_TRUSTED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
SITE_URL=https://yourdomain.com
DATABASE_URL=postgresql://username:password@hostname:5432/database_name
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.your-provider.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-smtp-user
EMAIL_HOST_PASSWORD=your-smtp-password
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=studio@yourdomain.com
LEADS_NOTIFICATION_EMAIL=your-inbox@yourdomain.com
OWNER_PROFILE_URL=https://example.com/owner-profile
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_SSL_REDIRECT=True
```

## 2. Build and release steps

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn axialfoundry.wsgi:application --bind 0.0.0.0:8000
```

## 3. Reverse proxy

Put Django/Gunicorn behind a reverse proxy such as Nginx or a managed platform ingress. Forward `X-Forwarded-Proto` so Django can honor HTTPS correctly with `SECURE_PROXY_SSL_HEADER`.

## 4. Static files

The project uses WhiteNoise and `CompressedManifestStaticFilesStorage`, so static assets can be served directly by Django/Gunicorn for simple deployments.

## 5. Database

SQLite is fine for local development. Use PostgreSQL in production. The project is already configured to switch with `DATABASE_URL`.

## 6. Email delivery

The lead form is SMTP-ready. Move away from the console backend before launch. If you use transactional email infrastructure, set the SMTP credentials and a verified `DEFAULT_FROM_EMAIL`.

## 7. Admin and staff access

- `/admin/` gives full Django admin access.
- `/studio/leads/` is staff-protected and useful for a lightweight internal review flow.

Create a superuser with:

```bash
python manage.py createsuperuser
```

## 8. Operational hardening

Recommended next steps for a live environment:

- Add error monitoring (for example, through your preferred logging or alerting stack)
- Add a stronger shared cache if running multiple app instances
- Add a real analytics layer only if needed and update the privacy policy accordingly
- Back up the production database regularly
- Enforce HTTPS at the proxy and app level

## 9. Health endpoint

The project exposes `/health/` for a simple health check.


============================================================
FILE: PROJECT_TREE.txt
============================================================
.env.example
.gitignore
DELIVERY_SUMMARY.md
DELIVERY_UPDATE.md
DEPLOYMENT_NOTES.md
FULL_CODEBASE.md
PROJECT_TREE.txt
README.md
axialfoundry/__init__.py
axialfoundry/asgi.py
axialfoundry/settings.py
axialfoundry/urls.py
axialfoundry/wsgi.py
core/__init__.py
core/apps.py
core/content.py
core/context_processors.py
core/sitemaps.py
core/templatetags/__init__.py
core/urls.py
core/views.py
leads/__init__.py
leads/admin.py
leads/apps.py
leads/forms.py
leads/migrations/0001_initial.py
leads/migrations/__init__.py
leads/models.py
leads/urls.py
leads/utils.py
leads/views.py
manage.py
requirements.txt
static/css/theme.css
static/img/blue-beams.jpg
static/img/blue-beams.webp
static/img/circuit-touch.jpg
static/img/circuit-touch.webp
static/img/code-laptop.jpg
static/img/code-laptop.webp
static/img/fiber-cables.jpg
static/img/fiber-cables.webp
static/img/hero-network.jpg
static/img/hero-network.webp
static/img/originals/blue-beams.jpg
static/img/originals/circuit-touch.jpg
static/img/originals/code-laptop.jpg
static/img/originals/fiber-cables.jpg
static/img/originals/hero-network.jpg
static/js/main.js
static/svg/favicon.svg
static/svg/logo-mark.svg
static/svg/logo.svg
static/svg/og-card.svg
templates/404.html
templates/base.html
templates/core/about.html
templates/core/home.html
templates/core/insights.html
templates/core/privacy.html
templates/core/services.html
templates/core/solutions.html
templates/core/work.html
templates/includes/cta_band.html
templates/includes/faq_item.html
templates/includes/footer.html
templates/includes/header.html
templates/includes/hero_visual.html
templates/includes/owner_section.html
templates/includes/page_header.html
templates/includes/page_visual.html
templates/includes/service_graphic.html
templates/includes/theme_toggle.html
templates/leads/contact.html
templates/leads/contact_email.html
templates/leads/contact_email.txt
templates/leads/dashboard.html
templates/robots.txt


============================================================
FILE: README.md
============================================================
# Axial Foundry

Axial Foundry is a premium founder-led software and AI studio website built with Django. The project combines studio positioning, polished multi-page marketing content, and a production-aware backend for lead capture, email notifications, staff-only lead review, and SEO basics.

## Stack

- Python 3.12+
- Django 5
- SQLite for local development
- PostgreSQL-ready database configuration via `DATABASE_URL`
- WhiteNoise for static assets
- Tailwind utility classes via CDN for a Python-first, zero-build maintenance workflow
- Alpine.js for lightweight interactivity

## Features

- Multi-page studio website with real content
- Premium visual design and custom SVG branding
- Dual-mode contact experience with a guided project funnel and a one-page enquiry option
- AJAX confirmation panel after successful submission, with server-side fallback
- Contact form with server-side and client-side validation
- Honeypot anti-spam protection
- Lightweight IP-based rate limiting
- Lead persistence with Django ORM
- SMTP-ready email notification hook
- Protected staff-only leads dashboard at `/studio/leads/`
- Clean Django admin integration for leads
- SEO-ready metadata, robots.txt, sitemap.xml, Open Graph card, and custom 404
- Owner profile CTA controlled through a single environment variable: `OWNER_PROFILE_URL`

## Project structure

- `axialfoundry/` – project settings, root URLs, WSGI/ASGI
- `core/` – studio pages, shared content, site context, sitemap, and supporting views
- `leads/` – lead model, form handling, rate limiting, notifications, dashboard, and admin
- `templates/` – shared base, partials, and page templates
- `static/` – custom CSS, JS, and SVG assets

## Local setup

1. Create and activate a virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Copy environment settings:

   ```bash
   cp .env.example .env
   ```

4. Run database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create an admin user:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Visit:

   - Website: `http://127.0.0.1:8000/`
   - Admin: `http://127.0.0.1:8000/admin/`
   - Leads dashboard: `http://127.0.0.1:8000/studio/leads/`

## Contact form configuration

By default, local development uses Django’s console email backend. For SMTP delivery, update `.env`:

```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.your-provider.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-smtp-user
EMAIL_HOST_PASSWORD=your-smtp-password
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=studio@yourdomain.com
LEADS_NOTIFICATION_EMAIL=you@yourdomain.com
```

The contact flow stores submissions in the `Lead` model, supports both guided and quick enquiry modes, and sends an internal notification email if the submission is not marked as spam.

## Database configuration

Local development defaults to SQLite. For PostgreSQL in staging or production, set a Postgres `DATABASE_URL`, for example:

```env
DATABASE_URL=postgresql://username:password@hostname:5432/database_name
```

The project uses `dj-database-url`, so switching databases does not require code changes.

## Owner profile CTA

The “View owner profile” button is controlled by one setting:

```env
OWNER_PROFILE_URL=https://example.com/owner-profile
```

If `OWNER_PROFILE_URL` is empty, the button is hidden gracefully.

## Security and operations notes

- Turn `DEBUG=False` in production.
- Set strong values for `SECRET_KEY`, `ALLOWED_HOSTS`, and `CSRF_TRUSTED_ORIGINS`.
- Configure SMTP before handling live enquiries.
- Run `python manage.py collectstatic` before deployment.
- Consider a stronger production cache such as Redis if you want distributed rate limiting across multiple instances.
- WhiteNoise serves static files directly from Django/Gunicorn for a straightforward deployment path.

## Production run example

```bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn axialfoundry.wsgi:application --bind 0.0.0.0:8000
```

## Notes on styling

This build keeps maintenance Python-first by using Tailwind utility classes through the CDN runtime and storing project-specific visual rules in `static/css/theme.css`. That keeps the repo simple for a Django-oriented owner and avoids introducing a Node build pipeline.


============================================================
FILE: axialfoundry/__init__.py
============================================================


============================================================
FILE: axialfoundry/asgi.py
============================================================
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'axialfoundry.settings')
application = get_asgi_application()


============================================================
FILE: axialfoundry/settings.py
============================================================
from __future__ import annotations

import os
from pathlib import Path

import dj_database_url
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')


def env_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {'1', 'true', 'yes', 'on'}


def env_list(name: str, default: str = '') -> list[str]:
    value = os.getenv(name, default)
    return [item.strip() for item in value.split(',') if item.strip()]


SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-change-me')
DEBUG = env_bool('DEBUG', True)
ALLOWED_HOSTS = env_list('ALLOWED_HOSTS', '127.0.0.1,localhost')
CSRF_TRUSTED_ORIGINS = env_list('CSRF_TRUSTED_ORIGINS', '')

SITE_NAME = 'Axial Foundry'
SITE_URL = os.getenv('SITE_URL', 'http://127.0.0.1:8000').rstrip('/')
CONTACT_EMAIL = os.getenv('CONTACT_EMAIL', 'mhtgcu18@gmail.com')
CONTACT_PHONE = os.getenv('CONTACT_PHONE', '+92 323 5809900')
CONTACT_LOCATION = os.getenv('CONTACT_LOCATION', 'Lahore, Pakistan')
LEADS_NOTIFICATION_EMAIL = os.getenv('LEADS_NOTIFICATION_EMAIL', CONTACT_EMAIL)
OWNER_PROFILE_URL = os.getenv('OWNER_PROFILE_URL', '').strip()

FOUNDER_NAME = 'Munief Hassan Tahir'
FOUNDER_TITLE = 'Senior Machine Learning Engineer — NLP & Speech AI'
FOUNDER_SUMMARY = (
    'Led by Munief Hassan Tahir, a machine learning engineer with 4+ years of experience '
    'across AI systems, software delivery, NLP, speech technologies, and production-grade '
    'Python engineering.'
)

RATE_LIMIT_WINDOW_SECONDS = int(os.getenv('RATE_LIMIT_WINDOW_SECONDS', '900'))
RATE_LIMIT_MAX_SUBMISSIONS = int(os.getenv('RATE_LIMIT_MAX_SUBMISSIONS', '5'))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'core',
    'leads',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'axialfoundry.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.site_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'axialfoundry.wsgi.application'
ASGI_APPLICATION = 'axialfoundry.asgi.application'

DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        conn_health_checks=True,
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Karachi'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = os.getenv('EMAIL_HOST', '')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '587'))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = env_bool('EMAIL_USE_TLS', True)
EMAIL_USE_SSL = env_bool('EMAIL_USE_SSL', False)
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'studio@axialfoundry.local')
SERVER_EMAIL = DEFAULT_FROM_EMAIL

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'axial-foundry-cache',
    }
}

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'
X_FRAME_OPTIONS = 'DENY'
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = False
SESSION_COOKIE_SECURE = env_bool('SESSION_COOKIE_SECURE', not DEBUG)
CSRF_COOKIE_SECURE = env_bool('CSRF_COOKIE_SECURE', not DEBUG)
SECURE_SSL_REDIRECT = env_bool('SECURE_SSL_REDIRECT', False)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': os.getenv('LOG_LEVEL', 'INFO'),
    },
}


============================================================
FILE: axialfoundry/urls.py
============================================================
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from core import views as core_views
from core.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

admin.site.site_header = 'Axial Foundry Admin'
admin.site.site_title = 'Axial Foundry Admin'
admin.site.index_title = 'Site administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('leads.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', core_views.robots_txt, name='robots_txt'),
    path('health/', core_views.health_check, name='health_check'),
]

handler404 = 'core.views.custom_404'


============================================================
FILE: axialfoundry/wsgi.py
============================================================
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'axialfoundry.settings')
application = get_wsgi_application()


============================================================
FILE: core/__init__.py
============================================================


============================================================
FILE: core/apps.py
============================================================
from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'


============================================================
FILE: core/content.py
============================================================
from __future__ import annotations

BRAND_STORY = (
    'Axial Foundry is a founder-led software and AI studio for organizations that need more '
    'than a concept deck. We design and build modern websites, web applications, automation, '
    'internal systems, and applied AI experiences that help teams move faster, communicate '
    'better, and operate with more clarity.'
)

POSITIONING_STATEMENT = (
    'We combine product thinking, Python engineering, and research-backed AI expertise to '
    'turn business needs into working digital systems. That means some engagements are advanced '
    'knowledge assistants or speech workflows, while others are premium company websites, '
    'custom portals, internal tools, or automation layers that remove operational friction.'
)

AUTHORITY_POINTS = [
    {
        'title': '4+ years building production-grade systems',
        'body': 'Hands-on delivery across conversational AI, retrieval systems, speech workflows, APIs, dashboards, and custom business software.',
    },
    {
        'title': 'Research-backed engineering, commercially applied',
        'body': 'Grounded by publication and evaluation work across LREC 2026, EACL 2026, and ChipSAL 2025 without turning the studio into an academic lab.',
    },
    {
        'title': 'International exposure with practical execution',
        'body': 'International research and training experience in Germany and Sri Lanka informs a global, product-oriented way of working.',
    },
    {
        'title': 'Founder-led delivery from strategy to launch',
        'body': 'Clients work with technical decision-makers who can scope, architect, build, refine, and launch the right level of solution.',
    },
]

SERVICE_CLUSTERS = [
    {
        'slug': 'ai-systems',
        'title': 'AI Systems',
        'summary': 'Applied AI for organizations that want useful capabilities inside products, workflows, support channels, or internal knowledge experiences.',
        'items': [
            'AI consulting and implementation strategy',
            'AI assistants and chatbots',
            'RAG and knowledge assistants',
            'Prompt engineering and orchestration',
            'LLM fine-tuning and evaluation',
            'Speech AI and voice workflows',
            'Custom AI workflows and integrations',
        ],
    },
    {
        'slug': 'software-products',
        'title': 'Software Products',
        'summary': 'Custom web apps, portals, APIs, dashboards, and internal systems designed around real operating needs rather than generic templates.',
        'items': [
            'Custom web applications',
            'Internal tools and admin systems',
            'Client portals and partner dashboards',
            'SaaS MVPs and feature delivery',
            'Backend systems and API development',
            'Product engineering and technical planning',
        ],
    },
    {
        'slug': 'web-digital-platforms',
        'title': 'Websites and Digital Platforms',
        'summary': 'Premium digital presence for businesses that need credibility, performance, lead capture, and a stronger online customer journey.',
        'items': [
            'Premium business websites',
            'Conversion-focused landing pages',
            'CMS-backed company sites',
            'Website redesigns and UX upgrades',
            'Performance and content structure improvements',
        ],
    },
    {
        'slug': 'automation-data',
        'title': 'Automation and Data Systems',
        'summary': 'Operational systems that connect data, reduce repetitive work, and improve visibility across sales, support, reporting, and execution.',
        'items': [
            'Workflow automation',
            'CRM and communication integrations',
            'Data pipelines and ETL workflows',
            'Web scraping and structured data capture',
            'Reporting dashboards and monitoring systems',
        ],
    },
]

WHY_CHOOSE = [
    {
        'title': 'End-to-end delivery',
        'body': 'Strategy, architecture, UX planning, implementation, QA, launch, and iteration can stay inside one delivery relationship.',
    },
    {
        'title': 'Software and AI under one roof',
        'body': 'The studio can build the surrounding system, not just the model layer, so the outcome actually fits how the business operates.',
    },
    {
        'title': 'Founder-led execution',
        'body': 'Decisions stay close to the technical work. That means clearer trade-offs, faster progress, and less translation loss between planning and build.',
    },
    {
        'title': 'Custom builds, not generic templates',
        'body': 'Solutions are shaped around the right level of complexity for the client, whether that is a premium website, a data workflow, or a full AI feature.',
    },
    {
        'title': 'Business-friendly communication',
        'body': 'Technical depth is translated into clear scope, working deliverables, and practical next steps for business buyers and technical stakeholders alike.',
    },
    {
        'title': 'Research credibility without unnecessary complexity',
        'body': 'The studio can handle evaluation, benchmarking, prompt quality, and system rigor while still keeping delivery focused on business value.',
    },
]

FEATURED_SOLUTIONS = [
    {
        'title': 'AI customer support assistant',
        'body': 'A brand-aligned assistant that answers common questions, routes conversations, and supports teams with cleaner handoffs.',
        'tags': ['Support', 'Chatbot', 'Automation'],
    },
    {
        'title': 'Internal knowledge assistant',
        'body': 'A retrieval-powered system that turns scattered documents, SOPs, and reference material into a searchable working layer.',
        'tags': ['RAG', 'Knowledge', 'Internal tools'],
    },
    {
        'title': 'CRM-connected chatbot workflow',
        'body': 'A conversational layer connected to CRM records, WhatsApp or messaging channels, and business-specific workflows.',
        'tags': ['CRM', 'WhatsApp', 'Lead handling'],
    },
    {
        'title': 'Custom business dashboard',
        'body': 'A reporting and operations surface that helps teams track activity, exceptions, pipeline state, and important metrics in one place.',
        'tags': ['Dashboard', 'Visibility', 'Reporting'],
    },
    {
        'title': 'Premium company website',
        'body': 'A modern, conversion-aware website that strengthens positioning, supports lead capture, and presents the business with more authority.',
        'tags': ['Website', 'Brand', 'Lead generation'],
    },
    {
        'title': 'Workflow automation system',
        'body': 'An operational layer that removes repetitive admin work, pushes information between systems, and keeps teams moving faster.',
        'tags': ['Automation', 'Operations', 'Integrations'],
    },
    {
        'title': 'Client portal or web app',
        'body': 'A focused application for customers, staff, partners, or internal teams that need a better interface for recurring workflows.',
        'tags': ['Portal', 'Web app', 'Product'],
    },
    {
        'title': 'Speech and transcription workflow',
        'body': 'Transcription, diarization, or voice-enabled processing designed for real content, support, monitoring, or research use cases.',
        'tags': ['Speech AI', 'ASR', 'Diarization'],
    },
]


ENGAGEMENT_PATHS = [
    {
        'title': 'Launch or reposition the business online',
        'body': 'For companies that need a premium website, stronger positioning, better lead capture, and a more credible digital presence.',
        'deliverables': ['Brand-led website UX', 'High-conviction pages', 'Lead capture and analytics'],
    },
    {
        'title': 'Build or extend a software product',
        'body': 'For startups, product teams, and agencies that need a portal, SaaS MVP, backend platform, or client-facing workflow shipped properly.',
        'deliverables': ['Product planning', 'Web app and API build', 'Launch-ready delivery'],
    },
    {
        'title': 'Automate operations or add AI capability',
        'body': 'For teams that want to reduce manual work, connect systems, or introduce assistants, knowledge layers, and workflow intelligence into the business.',
        'deliverables': ['Automation design', 'AI workflow integration', 'Operational systems'],
    },
]

PROCESS_STEPS = [
    {
        'step': '01',
        'title': 'Discovery',
        'body': 'Understand the business need, current constraints, users, success criteria, and what level of solution actually makes sense.',
    },
    {
        'step': '02',
        'title': 'Scope and strategy',
        'body': 'Turn the problem into a delivery plan covering technical direction, user flow, priorities, dependencies, and implementation shape.',
    },
    {
        'step': '03',
        'title': 'UX and system planning',
        'body': 'Map how users interact with the system and how the backend, data, automations, or AI layers will support the outcome.',
    },
    {
        'step': '04',
        'title': 'Build',
        'body': 'Develop the product, website, workflow, or AI system with iterative reviews and clear progress visibility.',
    },
    {
        'step': '05',
        'title': 'QA and refinement',
        'body': 'Validate the experience, pressure-test critical flows, refine outputs, and tighten the system before it reaches real users.',
    },
    {
        'step': '06',
        'title': 'Launch and iteration',
        'body': 'Deploy cleanly, support the rollout, and continue with improvements when the project calls for ongoing evolution.',
    },
]

SERVICE_DETAILS = [
    {
        'group': 'AI Systems',
        'title': 'AI Strategy and Implementation',
        'what_it_is': 'A focused engagement that translates AI possibilities into the right roadmap, architecture, and delivery plan for the business.',
        'who_it_is_for': 'Teams exploring AI seriously and wanting practical direction before investing in the wrong build.',
        'problems_it_solves': [
            'Unclear where AI should fit into the product or operation',
            'Too many tooling options and no solid implementation path',
            'Pressure to “do AI” without knowing the right starting point',
        ],
        'client_receives': [
            'A grounded implementation direction',
            'A recommended scope and system shape',
            'Clear trade-offs around complexity, cost, and maintainability',
        ],
        'typical_engagement': 'Discovery workshops, system mapping, use-case prioritization, architecture recommendations, and implementation planning.',
    },
    {
        'group': 'AI Systems',
        'title': 'AI Assistants and Chatbots',
        'what_it_is': 'Custom conversational systems built for support, lead handling, knowledge access, or workflow assistance.',
        'who_it_is_for': 'Companies that need faster customer communication, structured lead capture, or assistant-style user experiences.',
        'problems_it_solves': [
            'Slow or inconsistent response handling',
            'Repetitive support or lead qualification conversations',
            'Disconnected conversational tools that do not fit business processes',
        ],
        'client_receives': [
            'Conversation design aligned to the brand and workflow',
            'Backend integrations where needed',
            'Deployment-ready assistant flows and safeguards',
        ],
        'typical_engagement': 'Conversation design, prompt and logic design, integrations, testing, channel delivery, and refinement.',
    },
    {
        'group': 'AI Systems',
        'title': 'RAG and Knowledge Assistants',
        'what_it_is': 'Retrieval-augmented systems that help people find grounded answers from documents, knowledge bases, SOPs, or structured content.',
        'who_it_is_for': 'Knowledge-heavy teams, support environments, enterprise departments, and organizations with fragmented information.',
        'problems_it_solves': [
            'Information buried in PDFs, docs, and internal repositories',
            'Slow access to reference knowledge',
            'Need for more reliable answers than a generic chatbot can provide',
        ],
        'client_receives': [
            'Ingestion and retrieval design',
            'Grounded answer workflows',
            'Evaluation and interface considerations for real usage',
        ],
        'typical_engagement': 'Source mapping, ingestion setup, retrieval logic, answer orchestration, evaluation loops, and front-end delivery.',
    },
    {
        'group': 'AI Systems',
        'title': 'LLM Fine-tuning and Evaluation',
        'what_it_is': 'Model adaptation, instruction tuning, benchmarking, and evaluation support for organizations that need more control over output behavior.',
        'who_it_is_for': 'Teams with domain-specific tasks, quality concerns, research-heavy requirements, or specialized language and prompting needs.',
        'problems_it_solves': [
            'Generic model performance is not strong enough for the task',
            'No repeatable way to evaluate model quality',
            'Need for more rigorous tuning or benchmarking decisions',
        ],
        'client_receives': [
            'Evaluation design and benchmark thinking',
            'Model adaptation recommendations or pipelines',
            'Clearer understanding of quality thresholds and trade-offs',
        ],
        'typical_engagement': 'Dataset preparation, instruction design, evaluation planning, adaptation workflows, and reporting.',
    },
    {
        'group': 'AI Systems',
        'title': 'Speech AI Systems',
        'what_it_is': 'Speech-enabled solutions spanning transcription, diarization, text-to-speech, or voice-aware workflows.',
        'who_it_is_for': 'Teams handling calls, audio archives, voice interfaces, monitoring, or multilingual content processing.',
        'problems_it_solves': [
            'Audio content that is difficult to process manually',
            'Need for speaker separation or searchable transcripts',
            'Need to bring voice or speech signals into a larger product or workflow',
        ],
        'client_receives': [
            'Speech pipeline design',
            'Operational integration plan',
            'Delivery around transcription, diarization, TTS, or related interfaces',
        ],
        'typical_engagement': 'Audio workflow mapping, model integration, preprocessing, evaluation, output formatting, and deployment.',
    },
    {
        'group': 'Software and Product Development',
        'title': 'Custom Web Applications',
        'what_it_is': 'Purpose-built web applications designed around the client’s actual product requirements, workflows, and user roles.',
        'who_it_is_for': 'Startups, internal teams, agencies, and organizations that need more than a marketing website.',
        'problems_it_solves': [
            'Manual processes that need a proper application layer',
            'Generic tools that do not fit the workflow',
            'Need for a product or internal system tailored to the business model',
        ],
        'client_receives': [
            'A scoped application architecture',
            'Frontend and backend delivery',
            'Admin controls, user flows, and maintainable Python systems',
        ],
        'typical_engagement': 'Product definition, interface planning, backend development, QA, launch support, and iteration.',
    },
    {
        'group': 'Software and Product Development',
        'title': 'Product and MVP Build',
        'what_it_is': 'Focused product engineering for teams that need to ship an MVP, deliver a feature set, or move from concept to working software.',
        'who_it_is_for': 'Founders, product teams, and agencies that need execution support or technical ownership.',
        'problems_it_solves': [
            'Concepts stuck in planning mode',
            'Need for a reliable delivery partner',
            'Pressure to launch without building an unnecessary amount of infrastructure',
        ],
        'client_receives': [
            'A pragmatic release plan',
            'Technical implementation aligned to product goals',
            'A maintainable path beyond the first launch',
        ],
        'typical_engagement': 'Feature scoping, architecture, sprint-based delivery, release readiness, and post-launch improvements.',
    },
    {
        'group': 'Web and Digital Presence',
        'title': 'Premium Website Development',
        'what_it_is': 'High-credibility websites for businesses that need strong positioning, polished design, performance, and better lead capture.',
        'who_it_is_for': 'Service companies, agencies, studios, consultancies, startups, and organizations upgrading their public-facing presence.',
        'problems_it_solves': [
            'A weak or outdated website that undersells the business',
            'Poor conversion flow or unclear messaging',
            'Need for a more credible digital presence in international markets',
        ],
        'client_receives': [
            'A strategy-backed website structure',
            'Conversion-aware content and user journey design',
            'A fast, maintainable implementation',
        ],
        'typical_engagement': 'Positioning refinement, page planning, UI design, frontend implementation, lead capture integration, and launch.',
    },
    {
        'group': 'Automation and Data',
        'title': 'Automation and Backend Systems',
        'what_it_is': 'Operational tooling that connects systems, removes repetitive work, and gives the business a stronger backend foundation.',
        'who_it_is_for': 'Teams dealing with fragmented processes, manual handoffs, repetitive admin work, or underpowered back-office systems.',
        'problems_it_solves': [
            'Tasks repeated manually across tools',
            'No clean backend logic for the workflow',
            'Need for custom integrations, APIs, or rules-based system behavior',
        ],
        'client_receives': [
            'Workflow-aware backend design',
            'API and integration implementation',
            'Operational systems that support real team usage',
        ],
        'typical_engagement': 'Process mapping, backend development, integrations, data syncing, testing, and deployment.',
    },
    {
        'group': 'Automation and Data',
        'title': 'Data Pipelines and Scraping',
        'what_it_is': 'Structured data capture, transformation, and delivery systems that support research, reporting, automation, or product features.',
        'who_it_is_for': 'Organizations that need better access to data from websites, third-party sources, internal systems, or recurring collection processes.',
        'problems_it_solves': [
            'Important data trapped in manual workflows',
            'Need for repeatable collection and cleanup pipelines',
            'Reporting or product requirements that depend on structured data',
        ],
        'client_receives': [
            'Collection logic and pipeline design',
            'Reliable storage and transformation flows',
            'Structured outputs for reporting, dashboards, or downstream systems',
        ],
        'typical_engagement': 'Source analysis, scraper or collector development, ETL logic, scheduling, monitoring, and output delivery.',
    },
]

AUDIENCE_SOLUTIONS = [
    {
        'title': 'Startups',
        'summary': 'For founders and product teams that need MVPs, technical execution, AI features, or a sharper digital launch presence.',
        'needs': [
            'MVP planning and build',
            'AI features inside a product without overengineering',
            'Custom portals, dashboards, and admin systems',
            'A credible website that supports fundraising or sales conversations',
        ],
    },
    {
        'title': 'SMEs',
        'summary': 'For growing businesses that need better websites, stronger backend systems, less manual work, and more operational clarity.',
        'needs': [
            'Website redesigns and lead capture',
            'Internal tools and workflow automation',
            'CRM-connected processes and data visibility',
            'Business-specific software instead of scattered tools',
        ],
    },
    {
        'title': 'Agencies',
        'summary': 'For creative, marketing, and strategy agencies that need a technically strong partner to help deliver digital products and builds.',
        'needs': [
            'White-label or delivery-partner support',
            'Custom websites and web apps',
            'Automation or backend implementation',
            'AI feature delivery when a client brief calls for it',
        ],
    },
    {
        'title': 'Enterprise Teams',
        'summary': 'For departments and internal teams that need knowledge systems, automations, portals, or specialized AI-enabled workflows.',
        'needs': [
            'Internal knowledge assistants',
            'Operational dashboards and internal tools',
            'Workflow integrations and backend systems',
            'Evaluation-oriented AI delivery with practical constraints in mind',
        ],
    },
    {
        'title': 'Knowledge-heavy organizations',
        'summary': 'For teams where documents, research, procedures, or content need to become more usable, searchable, and operational.',
        'needs': [
            'RAG systems and search experiences',
            'Speech-to-text, diarization, and content workflows',
            'Structured access to documentation and reference material',
            'Interfaces that reduce the friction of finding the right information',
        ],
    },
    {
        'title': 'Service businesses',
        'summary': 'For companies that need stronger digital presence, smoother client handling, and better systems behind day-to-day delivery.',
        'needs': [
            'Premium websites and landing pages',
            'Lead routing and client intake systems',
            'Automation around follow-up, reporting, and internal handoffs',
            'Simple AI additions where they make the service better',
        ],
    },
]

NEED_MAP = [
    {
        'title': 'Lead capture and conversion',
        'body': 'Premium websites, landing pages, lead forms, CRM integration, and conversational touchpoints that support response quality and follow-through.',
    },
    {
        'title': 'Customer communication',
        'body': 'Support assistants, chatbots, messaging workflows, portal experiences, and structured handoffs between automation and human teams.',
    },
    {
        'title': 'Internal operations',
        'body': 'Dashboards, internal tools, workflow approvals, admin systems, and automation layers that reduce repeated manual work.',
    },
    {
        'title': 'Product development',
        'body': 'MVPs, SaaS features, web applications, APIs, and backend systems designed around actual user and business requirements.',
    },
    {
        'title': 'Content and knowledge access',
        'body': 'RAG systems, search interfaces, structured knowledge delivery, transcription, and speech-enabled content workflows.',
    },
    {
        'title': 'Automation and data visibility',
        'body': 'Pipelines, scraping, integrations, reporting dashboards, and backend services that make information more reliable and useful.',
    },
]

CASE_STUDIES = [
    {
        'slug': 'knowledge-assistant',
        'category': 'AI Systems',
        'title': 'Knowledge assistant for document-heavy teams',
        'summary': 'Representative of RAG-powered question answering work built to make internal or public-facing knowledge easier to access through grounded retrieval.',
        'challenge': 'Important information existed across multiple sources and formats, making fast access difficult for end users and support teams.',
        'solution': 'Designed ingestion, retrieval, answer orchestration, evaluation thinking, and user-facing flows for a question-answering experience grounded in curated sources.',
        'deliverables': [
            'Knowledge ingestion workflow',
            'Retrieval and answer design',
            'Prompt and evaluation structure',
            'Python backend and delivery interface',
        ],
        'capabilities': ['RAG', 'Prompt engineering', 'Evaluation', 'Backend systems', 'UX flow'],
        'note': 'Based on real RAG system experience; client-specific details are intentionally withheld.',
    },
    {
        'slug': 'crm-chatbot',
        'category': 'Applied AI and Automation',
        'title': 'CRM-connected WhatsApp assistant',
        'summary': 'A conversational workflow integrating business messaging, OpenAI-powered logic, retrieval, and CRM-connected handling for lead or support interactions.',
        'challenge': 'The business needed a more responsive conversational layer while keeping activity connected to internal processes and contact records.',
        'solution': 'Implemented a chatbot flow combining conversational logic, data retrieval, CRM integration, and channel-aware handling via WhatsApp and Twilio-style workflows.',
        'deliverables': [
            'Conversation logic and fallback handling',
            'CRM-aware data exchange',
            'Lead or support workflow integration',
            'Deployment-ready backend structure',
        ],
        'capabilities': ['Chatbots', 'OpenAI APIs', 'RAG', 'CRM integration', 'Automation'],
        'note': 'Representative of real CRM-integrated chatbot system work.',
    },
    {
        'slug': 'speech-workflow',
        'category': 'Speech AI',
        'title': 'Speech transcription and diarization workflow',
        'summary': 'Speech-oriented system work spanning transcription, speaker diarization, and usable output formatting for operational or research contexts.',
        'challenge': 'Audio-heavy workflows require more than raw transcripts; they need usable structure, speaker clarity, and dependable processing pipelines.',
        'solution': 'Designed an end-to-end pipeline for audio preprocessing, ASR, diarization, output cleanup, and downstream usability for teams working with recorded speech.',
        'deliverables': [
            'Speech processing pipeline',
            'Structured transcript outputs',
            'Speaker-aware formatting',
            'Operational integration points',
        ],
        'capabilities': ['ASR', 'Diarization', 'Speech workflows', 'Python pipelines'],
        'note': 'Grounded in real speech AI delivery experience.',
    },
    {
        'slug': 'model-adaptation',
        'category': 'Model Adaptation',
        'title': 'LLM adaptation and evaluation workflow',
        'summary': 'Representative of model evaluation, instruction tuning, continual pretraining, and benchmarking work used to understand model behavior and quality.',
        'challenge': 'Generic models often need stronger adaptation and more rigorous evaluation before they can be trusted for specialized tasks.',
        'solution': 'Worked on data preparation, tuning logic, evaluation design, and benchmark-oriented analysis for adapted model behavior and performance review.',
        'deliverables': [
            'Evaluation criteria and benchmark framing',
            'Adaptation workflow support',
            'Task-aware testing structure',
            'Technical reporting inputs',
        ],
        'capabilities': ['Instruction tuning', 'Continual pretraining', 'Model evaluation', 'Benchmarking'],
        'note': 'Reflects real research-backed LLM work without disclosing confidential project specifics.',
    },
    {
        'slug': 'data-infrastructure',
        'category': 'Automation and Data',
        'title': 'Web scraping and data infrastructure layer',
        'summary': 'A data collection and processing setup built to support recurring business or research needs through cleaner acquisition and structured outputs.',
        'challenge': 'Valuable information was spread across external sources and manual collection introduced delay, inconsistency, and reporting friction.',
        'solution': 'Developed scraping logic, cleanup steps, data storage patterns, and delivery pipelines that made collected data more usable for downstream systems.',
        'deliverables': [
            'Scraper or collector workflows',
            'Transformation logic',
            'Storage and scheduling patterns',
            'Monitoring-aware pipeline structure',
        ],
        'capabilities': ['Web scraping', 'Data pipelines', 'Automation', 'Monitoring'],
        'note': 'Representative of real data engineering and automation themes.',
    },
    {
        'slug': 'product-platform',
        'category': 'Software Products',
        'title': 'Custom portal and backend system delivery',
        'summary': 'Product-oriented engineering work focused on the application layer around user journeys, data handling, dashboards, and business logic.',
        'challenge': 'Businesses often need operational software that fits their workflow instead of trying to force teams into generic off-the-shelf tools.',
        'solution': 'Built backend services, admin flows, data structures, and web interfaces shaped around product requirements and day-to-day operational usage.',
        'deliverables': [
            'Application architecture',
            'Django or Python backend systems',
            'User-facing workflows and admin views',
            'Launch-ready product features',
        ],
        'capabilities': ['Django', 'REST APIs', 'SQL', 'Dashboards', 'Product engineering'],
        'note': 'Represents software delivery work beyond pure AI engagements.',
    },
]

FAQS = [
    {
        'question': 'Do you only take AI projects?',
        'answer': 'No. Axial Foundry builds premium websites, custom web applications, automation systems, dashboards, portals, and backend workflows as well as AI-enabled products. Many clients need strong software delivery first, with AI added only where it creates a clear advantage.',
    },
    {
        'question': 'Can you build a website without advanced AI?',
        'answer': 'Absolutely. Some of the best-fit engagements are premium company websites, conversion-focused landing pages, or digital platform rebuilds that improve credibility, lead flow, and user experience without needing an LLM-heavy stack.',
    },
    {
        'question': 'What kinds of clients are the best fit?',
        'answer': 'Startups, SMEs, agencies, enterprise teams, service businesses, and knowledge-heavy organizations that need a technically strong partner to scope and ship practical systems.',
    },
    {
        'question': 'Can you work inside an existing product or stack?',
        'answer': 'Yes. Projects can involve adding AI features to an existing product, improving a current backend workflow, redesigning a live website, or building a new system that integrates with the tools already in place.',
    },
    {
        'question': 'How do engagements usually start?',
        'answer': 'Most engagements begin with a discovery and scoping conversation to clarify goals, constraints, priorities, and the right delivery shape. From there, the work can move into strategy, design, implementation, or a focused build phase.',
    },
    {
        'question': 'Do you support agencies as a technical delivery partner?',
        'answer': 'Yes. Axial Foundry can work as a trusted technical partner for agencies that need help delivering websites, applications, automations, or AI features for their own clients.',
    },
    {
        'question': 'Do you provide support after launch?',
        'answer': 'Yes, where needed. Projects can include post-launch refinement, iteration, and ongoing technical support depending on the shape of the engagement.',
    },
]

ABOUT_PRINCIPLES = [
    {
        'title': 'Build what the business actually needs',
        'body': 'Not every problem needs a large AI layer. Sometimes the right answer is a strong website, a better admin system, a lean portal, or a dependable backend workflow.',
    },
    {
        'title': 'Keep technical depth connected to delivery',
        'body': 'Research rigor matters, but it should support better implementation choices, testing discipline, and more dependable outcomes for users and teams.',
    },
    {
        'title': 'Design for maintainability',
        'body': 'Systems should be understandable, evolvable, and realistic for the client to own after launch, especially when the stack is Python-first.',
    },
    {
        'title': 'Treat credibility as part of the product',
        'body': 'For client-facing platforms, communication, interface quality, content structure, and trust signals are part of the build, not afterthoughts.',
    },
]

CAPABILITY_GROUPS = [
    {
        'title': 'Applied AI',
        'items': ['LLMs', 'RAG', 'Prompt engineering', 'Evaluation', 'Instruction tuning', 'Speech AI'],
    },
    {
        'title': 'Software Engineering',
        'items': ['Python', 'Django', 'Flask', 'REST APIs', 'SQL', 'Backend systems'],
    },
    {
        'title': 'Web and Product Delivery',
        'items': ['Business websites', 'Web apps', 'Portals', 'Dashboards', 'UX planning', 'Launch support'],
    },
    {
        'title': 'Automation and Data',
        'items': ['Web scraping', 'Pipelines', 'CRM integration', 'Reporting', 'Monitoring', 'Workflow systems'],
    },
]

PUBLICATION_HIGHLIGHTS = [
    {
        'venue': 'LREC 2026',
        'title': 'Language and speech system research',
        'body': 'Reflects rigorous work around language technology, evaluation, and practical system thinking that strengthens delivery quality.',
    },
    {
        'venue': 'EACL 2026',
        'title': 'Model and multilingual NLP contribution',
        'body': 'Supports the studio’s ability to approach model behavior, benchmarking, and system design with more technical discipline.',
    },
    {
        'venue': 'ChipSAL 2025',
        'title': 'Benchmarking and applied LLM evaluation',
        'body': 'Shows a strong foundation in comparing model performance, understanding task fit, and bringing research methods into real implementation decisions.',
    },
]

INSIGHT_TOPICS = [
    {
        'title': 'How to add AI without rebuilding your entire product',
        'body': 'Many businesses do not need a from-scratch AI platform. The smarter route is often to add one high-value capability into an existing product or workflow.',
    },
    {
        'title': 'When a knowledge assistant is the right fit',
        'body': 'A retrieval-powered assistant makes sense when the challenge is scattered information, repeat questions, or slow access to trusted material.',
    },
    {
        'title': 'Why evaluation matters before scaling AI features',
        'body': 'Without a clear evaluation loop, teams end up guessing whether an AI feature is helpful, risky, or simply too inconsistent for production.',
    },
    {
        'title': 'What makes an internal tool actually useful',
        'body': 'Good internal products are shaped around real roles, repeated actions, and friction points, not just a list of requested screens.',
    },
    {
        'title': 'Speech systems as part of a workflow, not a demo',
        'body': 'Transcription, diarization, and voice processing become valuable when they fit reporting, review, monitoring, or documentation processes.',
    },
    {
        'title': 'Data pipelines that support automation',
        'body': 'Automation quality depends on how reliable the underlying data flow is. Collection, cleanup, structure, and monitoring all matter.',
    },
]

EXPERTISE_CARDS = [
    {
        'title': 'AI systems implementation',
        'body': 'From assistants and retrieval layers to model evaluation and prompt design, with delivery framed around operational fit.',
    },
    {
        'title': 'Product engineering',
        'body': 'Web applications, portals, APIs, backend logic, dashboards, and MVP builds with maintainable Python foundations.',
    },
    {
        'title': 'Speech and language systems',
        'body': 'ASR, diarization, TTS, multilingual workflows, and language-technology thinking that can support practical products.',
    },
    {
        'title': 'Automation and data infrastructure',
        'body': 'Scraping, pipelines, monitoring, reporting, and integration work that improves visibility and removes repetitive effort.',
    },
]


============================================================
FILE: core/context_processors.py
============================================================
from __future__ import annotations

from django.conf import settings
from django.urls import reverse


def site_settings(request):
    navigation = [
        {'label': 'Home', 'url': reverse('core:home')},
        {'label': 'Services', 'url': reverse('core:services')},
        {'label': 'Solutions', 'url': reverse('core:solutions')},
        {'label': 'Work', 'url': reverse('core:work')},
        {'label': 'About the Studio', 'url': reverse('core:about')},
        {'label': 'Insights', 'url': reverse('core:insights')},
        {'label': 'Contact', 'url': reverse('leads:contact')},
    ]
    return {
        'site_name': settings.SITE_NAME,
        'site_url': settings.SITE_URL,
        'contact_email': settings.CONTACT_EMAIL,
        'contact_phone': settings.CONTACT_PHONE,
        'contact_location': settings.CONTACT_LOCATION,
        'owner_profile_url': settings.OWNER_PROFILE_URL,
        'founder_name': settings.FOUNDER_NAME,
        'founder_title': settings.FOUNDER_TITLE,
        'founder_summary': settings.FOUNDER_SUMMARY,
        'site_navigation': navigation,
        'default_og_path': '/static/svg/og-card.svg',
    }


============================================================
FILE: core/sitemaps.py
============================================================
from __future__ import annotations

from django.urls import reverse
from django.contrib.sitemaps import Sitemap


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return [
            'core:home',
            'core:services',
            'core:solutions',
            'core:work',
            'core:about',
            'core:insights',
            'leads:contact',
            'core:privacy',
        ]

    def location(self, item):
        return reverse(item)


============================================================
FILE: core/templatetags/__init__.py
============================================================


============================================================
FILE: core/urls.py
============================================================
from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('solutions/', views.solutions, name='solutions'),
    path('work/', views.work, name='work'),
    path('about/', views.about, name='about'),
    path('insights/', views.insights, name='insights'),
    path('privacy/', views.privacy, name='privacy'),
]


============================================================
FILE: core/views.py
============================================================
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


============================================================
FILE: leads/__init__.py
============================================================


============================================================
FILE: leads/admin.py
============================================================
from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'company',
        'email',
        'service_interest',
        'budget',
        'inquiry_type',
        'is_spam',
        'created_at',
    )
    list_filter = ('service_interest', 'budget', 'inquiry_type', 'is_spam', 'created_at')
    search_fields = ('name', 'email', 'company', 'message', 'phone')
    readonly_fields = ('created_at', 'ip_address', 'user_agent', 'referrer')
    date_hierarchy = 'created_at'


============================================================
FILE: leads/apps.py
============================================================
from django.apps import AppConfig


class LeadsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'leads'


============================================================
FILE: leads/forms.py
============================================================
from __future__ import annotations

from django import forms

from .models import Lead


class ContactForm(forms.ModelForm):
    website = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Lead
        fields = [
            'name',
            'email',
            'phone',
            'company',
            'service_interest',
            'budget',
            'timeline',
            'message',
            'inquiry_type',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'you@company.com', 'required': True}),
            'phone': forms.TextInput(attrs={'placeholder': '+1 555 123 4567'}),
            'company': forms.TextInput(attrs={'placeholder': 'Company or organization'}),
            'service_interest': forms.Select(),
            'budget': forms.Select(),
            'timeline': forms.TextInput(attrs={'placeholder': 'For example: 2–4 weeks, this quarter, or flexible'}),
            'message': forms.Textarea(
                attrs={
                    'placeholder': 'Tell us what you want to build, improve, automate, or launch.',
                    'rows': 6,
                    'required': True,
                    'minlength': 20,
                }
            ),
            'inquiry_type': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inquiry_type'].initial = Lead.InquiryType.PROJECT
        common_class = (
            'mt-2 w-full rounded-2xl border border-white/12 bg-slate-950/50 px-4 py-3 '
            'text-sm text-slate-100 placeholder:text-slate-500 focus:border-brand-500 '
            'focus:outline-none focus:ring-2 focus:ring-brand-500/30'
        )
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.HiddenInput):
                continue
            field.widget.attrs['class'] = common_class
        self.fields['service_interest'].choices = [('', 'Select a service')] + list(self.fields['service_interest'].choices)
        self.fields['budget'].choices = [('', 'Select a budget range')] + list(self.fields['budget'].choices)
        self.fields['service_interest'].widget.attrs['required'] = True

    def clean_name(self):
        value = self.cleaned_data['name'].strip()
        if len(value) < 2:
            raise forms.ValidationError('Please enter a valid name.')
        return value

    def clean_email(self):
        return self.cleaned_data['email'].strip().lower()

    def clean_message(self):
        value = self.cleaned_data['message'].strip()
        if len(value) < 20:
            raise forms.ValidationError('Please share a little more detail so we can respond usefully.')
        return value


============================================================
FILE: leads/migrations/0001_initial.py
============================================================
# Generated by Django 5 on project creation.

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('company', models.CharField(blank=True, max_length=120)),
                ('service_interest', models.CharField(choices=[('ai-strategy', 'AI Strategy'), ('ai-chatbot', 'AI Chatbot / Assistant'), ('rag-knowledge', 'RAG / Knowledge Assistant'), ('llm-fine-tuning', 'LLM Fine-tuning'), ('speech-ai', 'Speech AI'), ('website-development', 'Website Development'), ('web-application-development', 'Web Application Development'), ('automation-backend-systems', 'Automation / Backend Systems'), ('data-pipelines-scraping', 'Data Pipelines / Scraping'), ('product-mvp-build', 'Product / MVP Build'), ('research-collaboration', 'Research Collaboration'), ('other', 'Other')], max_length=50)),
                ('budget', models.CharField(blank=True, choices=[('under-3000', 'Under $3,000'), ('3000-10000', '$3,000 – $10,000'), ('10000-25000', '$10,000 – $25,000'), ('25000-plus', '$25,000+'), ('discuss', "Let's discuss")], max_length=30)),
                ('timeline', models.CharField(blank=True, max_length=120)),
                ('message', models.TextField()),
                ('inquiry_type', models.CharField(choices=[('project', 'Project Inquiry'), ('partnership', 'Partnership'), ('research', 'Research Collaboration'), ('other', 'Other')], default='project', max_length=20)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('user_agent', models.TextField(blank=True)),
                ('referrer', models.URLField(blank=True, max_length=500)),
                ('is_spam', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Lead',
                'verbose_name_plural': 'Leads',
                'ordering': ['-created_at'],
            },
        ),
    ]


============================================================
FILE: leads/migrations/__init__.py
============================================================


============================================================
FILE: leads/models.py
============================================================
from __future__ import annotations

from django.db import models


class Lead(models.Model):
    class ServiceInterest(models.TextChoices):
        AI_STRATEGY = 'ai-strategy', 'AI Strategy'
        AI_CHATBOT = 'ai-chatbot', 'AI Chatbot / Assistant'
        RAG = 'rag-knowledge', 'RAG / Knowledge Assistant'
        FINE_TUNING = 'llm-fine-tuning', 'LLM Fine-tuning'
        SPEECH_AI = 'speech-ai', 'Speech AI'
        WEBSITE = 'website-development', 'Website Development'
        WEB_APP = 'web-application-development', 'Web Application Development'
        AUTOMATION = 'automation-backend-systems', 'Automation / Backend Systems'
        DATA = 'data-pipelines-scraping', 'Data Pipelines / Scraping'
        PRODUCT = 'product-mvp-build', 'Product / MVP Build'
        RESEARCH = 'research-collaboration', 'Research Collaboration'
        OTHER = 'other', 'Other'

    class Budget(models.TextChoices):
        UNDER_3K = 'under-3000', 'Under $3,000'
        RANGE_3_10K = '3000-10000', '$3,000 – $10,000'
        RANGE_10_25K = '10000-25000', '$10,000 – $25,000'
        OVER_25K = '25000-plus', '$25,000+'
        DISCUSS = 'discuss', "Let's discuss"

    class InquiryType(models.TextChoices):
        PROJECT = 'project', 'Project Inquiry'
        PARTNERSHIP = 'partnership', 'Partnership'
        RESEARCH = 'research', 'Research Collaboration'
        OTHER = 'other', 'Other'

    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=120, blank=True)
    service_interest = models.CharField(max_length=50, choices=ServiceInterest.choices)
    budget = models.CharField(max_length=30, choices=Budget.choices, blank=True)
    timeline = models.CharField(max_length=120, blank=True)
    message = models.TextField()
    inquiry_type = models.CharField(max_length=20, choices=InquiryType.choices, default=InquiryType.PROJECT)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True)
    referrer = models.URLField(max_length=500, blank=True)
    is_spam = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'

    def __str__(self) -> str:
        return f'{self.name} — {self.get_service_interest_display()}'


============================================================
FILE: leads/urls.py
============================================================
from django.urls import path

from . import views

app_name = 'leads'

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('studio/leads/', views.dashboard, name='dashboard'),
]


============================================================
FILE: leads/utils.py
============================================================
from __future__ import annotations

import logging
import time

from django.conf import settings
from django.core.cache import cache
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

logger = logging.getLogger(__name__)


def get_client_ip(request) -> str:
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded_for:
        return forwarded_for.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR', '')


def consume_rate_limit(ip_address: str) -> tuple[bool, int]:
    if not ip_address:
        return True, 0

    window = settings.RATE_LIMIT_WINDOW_SECONDS
    limit = settings.RATE_LIMIT_MAX_SUBMISSIONS
    key = f'lead-rate-limit:{ip_address}'
    now = int(time.time())
    state = cache.get(key)

    if not state or now - state['start'] > window:
        state = {'start': now, 'count': 0}

    if state['count'] >= limit:
        retry_after = max(window - (now - state['start']), 0)
        return False, retry_after

    state['count'] += 1
    cache.set(key, state, timeout=window)
    return True, 0


def send_lead_notification(lead) -> None:
    recipient = settings.LEADS_NOTIFICATION_EMAIL
    if not recipient:
        return

    context = {
        'lead': lead,
        'site_name': settings.SITE_NAME,
        'contact_email': settings.CONTACT_EMAIL,
    }
    subject = f'New lead for {settings.SITE_NAME}: {lead.name}'
    text_body = render_to_string('leads/contact_email.txt', context)
    html_body = render_to_string('leads/contact_email.html', context)

    email = EmailMultiAlternatives(
        subject=subject,
        body=text_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[recipient],
        reply_to=[lead.email],
    )
    email.attach_alternative(html_body, 'text/html')

    try:
        email.send(fail_silently=False)
    except Exception:
        logger.exception('Lead notification email failed to send.')


============================================================
FILE: leads/views.py
============================================================
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


============================================================
FILE: manage.py
============================================================
#!/usr/bin/env python
import os
import sys


def main() -> None:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'axialfoundry.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and available on your "
            "PYTHONPATH environment variable? Did you forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


============================================================
FILE: requirements.txt
============================================================
Django>=5.1,<5.3
whitenoise>=6.6,<7.0
dj-database-url>=2.2,<3.0
python-dotenv>=1.0,<2.0
gunicorn>=22.0,<24.0
psycopg[binary]>=3.2,<4.0


============================================================
FILE: static/css/theme.css
============================================================
:root {
    --ink: #08111f;
    --steel: #0f172a;
    --panel: rgba(15, 23, 42, 0.78);
    --line: rgba(255, 255, 255, 0.08);
    --line-strong: rgba(255, 255, 255, 0.14);
    --muted: #94a3b8;
    --copy: #dbe5f2;
    --brand: #1870f8;
    --brand-soft: rgba(24, 112, 248, 0.12);
    --accent: #4ee7c2;
}

* {
    box-sizing: border-box;
}

html,
body {
    min-height: 100%;
}

body {
    background:
        radial-gradient(circle at top left, rgba(24, 112, 248, 0.14), transparent 28%),
        radial-gradient(circle at right 15%, rgba(78, 231, 194, 0.08), transparent 18%),
        linear-gradient(180deg, #08111f 0%, #091220 40%, #07101a 100%);
    overflow-x: hidden;
}

[x-cloak] {
    display: none !important;
}

.site-grid {
    pointer-events: none;
    position: fixed;
    inset: 0;
    opacity: 0.52;
    background-image:
        linear-gradient(to right, rgba(255, 255, 255, 0.025) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.025) 1px, transparent 1px);
    background-size: 72px 72px;
    mask-image: linear-gradient(180deg, rgba(0, 0, 0, 0.7), transparent 90%);
    animation: gridDrift 24s linear infinite;
}

.ambient-orb,
.ambient-beam {
    pointer-events: none;
    position: fixed;
    z-index: 0;
    filter: blur(32px);
}

.ambient-orb {
    border-radius: 999px;
    opacity: 0.24;
    animation: orbFloat 20s ease-in-out infinite;
}

.ambient-orb--one {
    top: 7rem;
    right: -6rem;
    width: 18rem;
    height: 18rem;
    background: radial-gradient(circle, rgba(24, 112, 248, 0.6), rgba(24, 112, 248, 0.04) 70%);
}

.ambient-orb--two {
    bottom: 8rem;
    left: -5rem;
    width: 16rem;
    height: 16rem;
    background: radial-gradient(circle, rgba(78, 231, 194, 0.42), rgba(78, 231, 194, 0.04) 72%);
    animation-duration: 24s;
    animation-direction: reverse;
}

.ambient-beam {
    inset: auto;
    top: 28%;
    left: 20%;
    width: 48rem;
    height: 9rem;
    border-radius: 999px;
    background: linear-gradient(90deg, rgba(24, 112, 248, 0.18), rgba(78, 231, 194, 0.05), rgba(24, 112, 248, 0.18));
    transform: rotate(-14deg);
    opacity: 0.18;
    animation: beamPulse 18s ease-in-out infinite;
}

.section-shell {
    position: relative;
    padding-top: 5.5rem;
    padding-bottom: 5.5rem;
}

.section-divider {
    border-top: 1px solid rgba(255, 255, 255, 0.06);
}

.section-title {
    margin-top: 1rem;
    font-family: 'Space Grotesk', Inter, sans-serif;
    font-size: clamp(2rem, 4vw, 3.3rem);
    line-height: 1.02;
    font-weight: 700;
    letter-spacing: -0.04em;
    color: #ffffff;
}

.section-intro {
    margin-top: 1.5rem;
    max-width: 42rem;
    font-size: 1.06rem;
    line-height: 1.9;
    color: #c5d2e3;
}

.eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #85c0ff;
}

.eyebrow::before {
    content: '';
    display: inline-block;
    width: 0.75rem;
    height: 0.75rem;
    border-radius: 999px;
    background: linear-gradient(135deg, rgba(24, 112, 248, 1), rgba(78, 231, 194, 1));
    box-shadow: 0 0 0 4px rgba(24, 112, 248, 0.12);
    animation: dotPulse 5s ease-in-out infinite;
}

.gradient-text {
    background: linear-gradient(135deg, #ffffff 0%, #9cc8ff 46%, #7af2d0 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}

.surface-card {
    position: relative;
    border: 1px solid rgba(255, 255, 255, 0.09);
    background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.04), rgba(255, 255, 255, 0.02)),
        rgba(8, 17, 31, 0.75);
    border-radius: 1.75rem;
    padding: 1.6rem;
    box-shadow: 0 18px 55px rgba(2, 6, 23, 0.28);
    backdrop-filter: blur(22px);
    transition: transform 220ms ease, border-color 220ms ease, box-shadow 220ms ease, background 220ms ease;
}

.surface-card:hover {
    transform: translateY(-2px);
    border-color: rgba(71, 153, 255, 0.18);
    box-shadow: 0 24px 65px rgba(2, 6, 23, 0.34);
}

@media (min-width: 768px) {
    .surface-card {
        padding: 1.8rem;
    }
}

.surface-graph {
    background-image:
        linear-gradient(180deg, rgba(24, 112, 248, 0.12), transparent),
        linear-gradient(180deg, rgba(255, 255, 255, 0.04), rgba(255, 255, 255, 0.02));
}

.pointer-glow {
    position: relative;
    isolation: isolate;
}

.pointer-glow::after {
    content: '';
    position: absolute;
    inset: 0;
    z-index: 0;
    border-radius: inherit;
    background: radial-gradient(340px circle at var(--pointer-x, 50%) var(--pointer-y, 50%), rgba(255, 255, 255, 0.08), transparent 48%);
    opacity: 0;
    transition: opacity 220ms ease;
    pointer-events: none;
}

.pointer-glow:hover::after,
.pointer-glow.is-active::after {
    opacity: 1;
}

.icon-chip {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 2.75rem;
    height: 2.75rem;
    border-radius: 1rem;
    border: 1px solid rgba(24, 112, 248, 0.18);
    background: linear-gradient(180deg, rgba(24, 112, 248, 0.18), rgba(255, 255, 255, 0.04));
    color: #cce0ff;
}

.success-icon {
    width: 3.25rem;
    height: 3.25rem;
    border-radius: 1.2rem;
}

.button-primary,
.button-secondary,
.pill-link,
.contact-row,
.footer-link {
    transition: transform 160ms ease, border-color 160ms ease, background 160ms ease, color 160ms ease, box-shadow 160ms ease;
}

.button-primary {
    display: inline-flex;
    align-items: center;
    gap: 0.65rem;
    border-radius: 999px;
    background: linear-gradient(135deg, #1d74f8, #125bd7);
    padding: 0.9rem 1.35rem;
    font-size: 0.95rem;
    font-weight: 600;
    color: #ffffff;
    box-shadow: 0 15px 35px rgba(24, 112, 248, 0.25);
}

.button-primary:hover {
    transform: translateY(-1px);
    box-shadow: 0 20px 44px rgba(24, 112, 248, 0.32);
}

.button-secondary {
    display: inline-flex;
    align-items: center;
    gap: 0.65rem;
    border: 1px solid rgba(255, 255, 255, 0.14);
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.04);
    padding: 0.88rem 1.35rem;
    font-size: 0.95rem;
    font-weight: 600;
    color: #e2e8f0;
}

.button-secondary:hover,
.pill-link:hover,
.contact-row:hover,
.footer-link:hover {
    transform: translateY(-1px);
    border-color: rgba(255, 255, 255, 0.22);
    background: rgba(255, 255, 255, 0.08);
    color: #ffffff;
}

.pill-link {
    display: inline-flex;
    align-items: center;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.03);
    padding: 0.7rem 1rem;
}

.footer-link,
.contact-row {
    display: inline-flex;
    border: 1px solid transparent;
    border-radius: 1rem;
    padding: 0.7rem 1rem;
    background: rgba(255, 255, 255, 0.02);
    color: #cbd5e1;
}

.label-field {
    display: inline-flex;
    font-size: 0.82rem;
    font-weight: 600;
    letter-spacing: 0.03em;
    color: #d5e3f4;
}

.field-control {
    margin-top: 0.7rem;
    width: 100%;
    border-radius: 1rem;
    border: 1px solid rgba(255, 255, 255, 0.12);
    background: rgba(2, 6, 23, 0.52);
    padding: 0.92rem 1rem;
    font-size: 0.95rem;
    color: #f8fbff;
    outline: none;
    transition: border-color 160ms ease, box-shadow 160ms ease, background 160ms ease, transform 160ms ease;
}

.field-control:hover {
    border-color: rgba(255, 255, 255, 0.2);
}

.field-control:focus {
    border-color: rgba(71, 153, 255, 0.72);
    box-shadow: 0 0 0 5px rgba(24, 112, 248, 0.15);
    background: rgba(2, 6, 23, 0.66);
}

.field-control::placeholder {
    color: #64748b;
}

.field-control--textarea {
    min-height: 10rem;
    resize: vertical;
}

.error-text {
    margin-top: 0.55rem;
    font-size: 0.82rem;
    color: #fca5a5;
}

.mode-switcher {
    display: inline-flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    border-radius: 999px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    background: rgba(255, 255, 255, 0.04);
    padding: 0.42rem;
}

.mode-switcher__button {
    border-radius: 999px;
    padding: 0.82rem 1rem;
    font-size: 0.92rem;
    font-weight: 600;
    color: #94a3b8;
}

.mode-switcher__button.is-active {
    background: linear-gradient(135deg, rgba(24, 112, 248, 0.2), rgba(78, 231, 194, 0.14));
    color: #ffffff;
    box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.08);
}

.stepper-shell {
    border-radius: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.08);
    background: rgba(255, 255, 255, 0.03);
    padding: 1.1rem;
}

.stepper-bar {
    position: relative;
    overflow: hidden;
    height: 0.55rem;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.06);
}

.stepper-bar__progress {
    height: 100%;
    border-radius: inherit;
    background: linear-gradient(90deg, rgba(24, 112, 248, 0.95), rgba(78, 231, 194, 0.92));
    transition: width 220ms ease;
    box-shadow: 0 0 18px rgba(24, 112, 248, 0.35);
}

.step-chip {
    display: flex;
    align-items: flex-start;
    gap: 0.85rem;
    border-radius: 1rem;
    border: 1px solid rgba(255, 255, 255, 0.08);
    background: rgba(2, 6, 23, 0.35);
    padding: 0.95rem;
    transition: border-color 160ms ease, background 160ms ease, transform 160ms ease;
}

.step-chip:hover {
    transform: translateY(-1px);
    border-color: rgba(255, 255, 255, 0.14);
}

.step-chip.is-current {
    border-color: rgba(71, 153, 255, 0.24);
    background: rgba(24, 112, 248, 0.1);
}

.step-chip__index {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-width: 2rem;
    height: 2rem;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.08);
    font-size: 0.82rem;
    font-weight: 700;
    color: #ffffff;
}

.status-chip {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    border-radius: 999px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 0.35rem 0.7rem;
    font-size: 0.76rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.16em;
}

.status-chip::before {
    content: '';
    width: 0.55rem;
    height: 0.55rem;
    border-radius: 999px;
    background: currentColor;
    box-shadow: 0 0 0 4px rgba(255, 255, 255, 0.06);
}

.status-chip-live {
    color: #9af7de;
    background: rgba(78, 231, 194, 0.09);
}

.contact-tile {
    border-radius: 1.25rem;
    border: 1px solid rgba(255, 255, 255, 0.08);
    background: rgba(255, 255, 255, 0.03);
    padding: 1rem;
}

.timeline-list {
    display: grid;
    gap: 1rem;
}

.timeline-item {
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 1rem;
    align-items: flex-start;
    border-radius: 1.35rem;
    border: 1px solid rgba(255, 255, 255, 0.08);
    background: rgba(255, 255, 255, 0.03);
    padding: 1rem;
}

.timeline-item__index {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-width: 2.3rem;
    height: 2.3rem;
    border-radius: 999px;
    background: rgba(24, 112, 248, 0.14);
    color: #cfe3ff;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.14em;
}

.confirmation-inline-panel {
    border-radius: 1.8rem;
    border: 1px solid rgba(78, 231, 194, 0.18);
    background:
        linear-gradient(180deg, rgba(78, 231, 194, 0.08), rgba(255, 255, 255, 0.02)),
        rgba(8, 17, 31, 0.78);
    padding: 1.8rem;
    box-shadow: 0 20px 60px rgba(2, 6, 23, 0.28);
}

.success-panel {
    box-shadow: 0 28px 90px rgba(2, 6, 23, 0.44);
}

.reveal-ready {
    opacity: 0;
    transform: translateY(20px);
}

.reveal-ready.is-visible {
    opacity: 1;
    transform: translateY(0);
    transition: opacity 620ms ease, transform 620ms ease;
}

.product-console {
    position: relative;
    overflow: hidden;
    border-radius: 2rem;
    border: 1px solid rgba(255, 255, 255, 0.1);
    background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.06), rgba(255, 255, 255, 0.02)),
        rgba(8, 17, 31, 0.78);
    padding: 1.25rem;
    box-shadow: 0 24px 65px rgba(2, 6, 23, 0.34);
    backdrop-filter: blur(22px);
}

.product-console::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(115deg, transparent 0%, rgba(255, 255, 255, 0.08) 20%, transparent 40%);
    transform: translateX(-120%);
    animation: surfaceSweep 10s linear infinite;
    pointer-events: none;
}

.console-dots {
    display: flex;
    gap: 0.5rem;
}

.console-dots span {
    width: 0.7rem;
    height: 0.7rem;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.15);
}

.console-dots span:nth-child(1) {
    background: rgba(244, 114, 182, 0.58);
}

.console-dots span:nth-child(2) {
    background: rgba(250, 204, 21, 0.58);
}

.console-dots span:nth-child(3) {
    background: rgba(78, 231, 194, 0.58);
}

.signal-line {
    position: relative;
    overflow: hidden;
    height: 0.55rem;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.06);
}

.signal-line span {
    display: block;
    height: 100%;
    border-radius: inherit;
    background: linear-gradient(90deg, rgba(24, 112, 248, 0.92), rgba(78, 231, 194, 0.9));
    animation: pulseWidth 4.8s ease-in-out infinite;
}

.flow-column,
.metric-stack {
    display: grid;
    gap: 0.9rem;
}

.flow-node,
.metric-card,
.capability-pill {
    border-radius: 1.25rem;
    border: 1px solid rgba(255, 255, 255, 0.08);
    background: rgba(255, 255, 255, 0.04);
}

.flow-node {
    position: relative;
    padding: 1rem;
}

.flow-node::after {
    content: '';
    position: absolute;
    left: 1.2rem;
    right: 1.2rem;
    bottom: -0.45rem;
    height: 1px;
    background: linear-gradient(90deg, rgba(24, 112, 248, 0.3), rgba(78, 231, 194, 0.15));
}

.flow-node:last-child::after {
    display: none;
}

.metric-card {
    padding: 1rem;
}

.capability-pill {
    padding: 0.65rem 0.85rem;
    font-size: 0.84rem;
    color: #d6e4f5;
}

.prose a {
    color: #9cc8ff;
}

.prose a:hover {
    color: #ffffff;
}

input::placeholder,
textarea::placeholder,
select {
    opacity: 1;
}

@keyframes gridDrift {
    0% {
        transform: translate3d(0, 0, 0);
    }
    50% {
        transform: translate3d(0, -10px, 0);
    }
    100% {
        transform: translate3d(0, 0, 0);
    }
}

@keyframes orbFloat {
    0%,
    100% {
        transform: translate3d(0, 0, 0) scale(1);
    }
    50% {
        transform: translate3d(0, -18px, 0) scale(1.05);
    }
}

@keyframes beamPulse {
    0%,
    100% {
        opacity: 0.12;
        transform: rotate(-14deg) translate3d(0, 0, 0);
    }
    50% {
        opacity: 0.22;
        transform: rotate(-14deg) translate3d(18px, -12px, 0);
    }
}

@keyframes dotPulse {
    0%,
    100% {
        box-shadow: 0 0 0 4px rgba(24, 112, 248, 0.12);
    }
    50% {
        box-shadow: 0 0 0 6px rgba(24, 112, 248, 0.16);
    }
}

@keyframes pulseWidth {
    0%,
    100% {
        width: 72%;
    }
    50% {
        width: 92%;
    }
}

@keyframes surfaceSweep {
    0% {
        transform: translateX(-140%);
    }
    45%,
    100% {
        transform: translateX(140%);
    }
}

@media (prefers-reduced-motion: reduce) {
    html {
        scroll-behavior: auto;
    }

    *,
    *::before,
    *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
    }

    .site-grid,
    .ambient-orb,
    .ambient-beam {
        animation: none !important;
    }
}

/* Visual layer refresh */
:root {
    --theme-bg: #08111f;
    --theme-bg-alt: #0b1423;
    --theme-surface: rgba(8, 17, 31, 0.76);
    --theme-surface-strong: rgba(10, 18, 33, 0.88);
    --theme-border: rgba(255, 255, 255, 0.09);
    --theme-heading: #ffffff;
    --theme-copy: #dce6f3;
    --theme-muted: #94a3b8;
    --theme-muted-strong: #cbd5e1;
    --theme-soft: rgba(255, 255, 255, 0.05);
    --theme-header: rgba(8, 17, 31, 0.8);
    --theme-footer: rgba(2, 6, 23, 0.82);
}

html[data-theme='light'] {
    --theme-bg: #f6f9fd;
    --theme-bg-alt: #eaf1f8;
    --theme-surface: rgba(255, 255, 255, 0.82);
    --theme-surface-strong: rgba(255, 255, 255, 0.9);
    --theme-border: rgba(15, 23, 42, 0.08);
    --theme-heading: #0f172a;
    --theme-copy: #334155;
    --theme-muted: #64748b;
    --theme-muted-strong: #475569;
    --theme-soft: rgba(15, 23, 42, 0.04);
    --theme-header: rgba(255, 255, 255, 0.84);
    --theme-footer: rgba(248, 250, 252, 0.96);
}

body {
    color: var(--theme-copy);
    background:
        radial-gradient(circle at top left, rgba(24, 112, 248, 0.12), transparent 28%),
        radial-gradient(circle at right 15%, rgba(78, 231, 194, 0.08), transparent 18%),
        linear-gradient(180deg, var(--theme-bg) 0%, var(--theme-bg-alt) 45%, var(--theme-bg) 100%);
}

main,
footer,
body > header {
    position: relative;
    z-index: 1;
}

body > header {
    background: var(--theme-header) !important;
    border-color: var(--theme-border) !important;
}

footer {
    background: var(--theme-footer) !important;
    border-color: var(--theme-border) !important;
}

.site-canvas {
    position: fixed;
    inset: 0;
    z-index: -2;
    width: 100%;
    height: 100%;
    pointer-events: none;
    opacity: 0.95;
}

.site-grid {
    z-index: -1;
    opacity: 0.5;
}

html[data-theme='light'] .site-grid {
    opacity: 0.28;
    background-image:
        linear-gradient(to right, rgba(15, 23, 42, 0.035) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(15, 23, 42, 0.035) 1px, transparent 1px);
}

.surface-card {
    background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.02)),
        var(--theme-surface);
    border-color: var(--theme-border);
}

html[data-theme='light'] .surface-card {
    box-shadow: 0 18px 55px rgba(15, 23, 42, 0.08);
}

html[data-theme='light'] .text-white {
    color: var(--theme-heading) !important;
}

html[data-theme='light'] .text-slate-500 {
    color: #64748b !important;
}

html[data-theme='light'] .text-slate-400 {
    color: #64748b !important;
}

html[data-theme='light'] .text-slate-300 {
    color: #475569 !important;
}

html[data-theme='light'] .text-slate-200,
html[data-theme='light'] .text-slate-100 {
    color: #334155 !important;
}

html[data-theme='light'] .bg-ink {
    background-color: #f6f9fd !important;
}

html[data-theme='light'] .bg-white\/5 {
    background-color: rgba(15, 23, 42, 0.04) !important;
}

html[data-theme='light'] .bg-white\/\[0\.08\] {
    background-color: rgba(15, 23, 42, 0.06) !important;
}

html[data-theme='light'] .bg-slate-950\/60,
html[data-theme='light'] .bg-slate-950\/\[0\.96\],
html[data-theme='light'] .bg-slate-900\/70,
html[data-theme='light'] .bg-slate-900\/\[0\.85\] {
    background-color: rgba(255, 255, 255, 0.86) !important;
}

html[data-theme='light'] .border-white\/10,
html[data-theme='light'] .border-white\/\[0\.08\] {
    border-color: rgba(15, 23, 42, 0.08) !important;
}

html[data-theme='light'] .prose {
    --tw-prose-body: #334155;
    --tw-prose-headings: #0f172a;
    --tw-prose-links: #0e57d4;
    --tw-prose-bullets: #0e57d4;
    --tw-prose-bold: #0f172a;
}

html[data-theme='light'] .button-secondary,
html[data-theme='light'] .pill-link,
html[data-theme='light'] .contact-row,
html[data-theme='light'] .contact-tile,
html[data-theme='light'] .step-chip,
html[data-theme='light'] .faq-card {
    border-color: rgba(15, 23, 42, 0.08) !important;
    background: rgba(255, 255, 255, 0.82) !important;
}

html[data-theme='light'] .button-secondary {
    color: #0f172a;
}

html[data-theme='light'] .status-chip,
html[data-theme='light'] .wizard-status-card,
html[data-theme='light'] .hero-callout,
html[data-theme='light'] .page-chip,
html[data-theme='light'] .wizard-review__item,
html[data-theme='light'] .choice-card,
html[data-theme='light'] .field-control,
html[data-theme='light'] .faq-item,
html[data-theme='light'] .timeline-item,
html[data-theme='light'] .contact-tile,
html[data-theme='light'] .contact-row {
    color: #0f172a;
}

.nav-utility-button,
.theme-switch {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.65rem;
    border-radius: 999px;
    border: 1px solid var(--theme-border);
    background: var(--theme-soft);
    color: var(--theme-heading);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.06);
    transition: border-color 180ms ease, transform 180ms ease, background 180ms ease;
    backdrop-filter: blur(16px);
}

.theme-switch {
    padding: 0.68rem 0.92rem;
}

.theme-switch:hover,
.nav-utility-button:hover {
    transform: translateY(-1px);
    border-color: rgba(71, 153, 255, 0.28);
}

.nav-utility-button {
    width: 2.85rem;
    height: 2.85rem;
}

.theme-switch__icon {
    display: inline-flex;
    width: 1rem;
    height: 1rem;
}

.theme-switch__icon svg {
    width: 100%;
    height: 100%;
}

.theme-switch__label {
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.04em;
}

html[data-theme='dark'] .theme-switch__icon--moon,
html[data-theme='light'] .theme-switch__icon--sun {
    display: none;
}

.hero-home-shell {
    position: relative;
}

.hero-benefit {
    border-radius: 1rem;
    border: 1px solid var(--theme-border);
    background: var(--theme-soft);
    padding: 0.95rem 1rem;
    font-size: 0.92rem;
    line-height: 1.5;
    color: var(--theme-muted-strong);
}

.hero-media {
    position: relative;
    margin-inline: auto;
    max-width: 44rem;
}

.hero-media__glow {
    position: absolute;
    inset: -2rem;
    border-radius: 2.5rem;
    background: radial-gradient(circle at center, rgba(24, 112, 248, 0.16), transparent 60%);
    filter: blur(24px);
}

.hero-media__frame {
    position: relative;
    overflow: hidden;
    border-radius: 2rem;
    border: 1px solid var(--theme-border);
    background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.02)),
        var(--theme-surface-strong);
    padding: 1rem;
    box-shadow: 0 24px 80px rgba(2, 6, 23, 0.35);
}

.hero-media__toolbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    padding-bottom: 0.9rem;
}

.hero-media__screen {
    position: relative;
    overflow: hidden;
    border-radius: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.08);
    min-height: 380px;
}

.hero-media__image {
    display: block;
    width: 100%;
    min-height: 380px;
    object-fit: cover;
}

.hero-media__overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, rgba(8, 17, 31, 0.12), rgba(8, 17, 31, 0.5));
}

html[data-theme='light'] .hero-media__overlay {
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.08), rgba(248, 250, 252, 0.3));
}

.hero-media__scan {
    position: absolute;
    left: 0;
    right: 0;
    height: 26%;
    bottom: 16%;
    background: linear-gradient(180deg, transparent, rgba(78, 231, 194, 0.16), transparent);
    mix-blend-mode: screen;
    animation: scanMove 7s ease-in-out infinite;
}

.hero-media__details {
    pointer-events: none;
}

.hero-callout {
    position: absolute;
    max-width: 15rem;
    border-radius: 1rem;
    border: 1px solid rgba(255, 255, 255, 0.12);
    background: rgba(8, 17, 31, 0.72);
    padding: 0.9rem 1rem;
    box-shadow: 0 16px 35px rgba(2, 6, 23, 0.3);
    backdrop-filter: blur(16px);
}

html[data-theme='light'] .hero-callout {
    background: rgba(255, 255, 255, 0.9);
    border-color: rgba(15, 23, 42, 0.08);
}

.hero-callout__label {
    display: block;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #85c0ff;
}

.hero-callout__value {
    display: block;
    margin-top: 0.45rem;
    font-size: 0.9rem;
    line-height: 1.5;
    color: var(--theme-heading);
}

.hero-callout--top {
    top: 4.3rem;
    left: 1.25rem;
}

.hero-callout--left {
    bottom: 6.5rem;
    left: 1.25rem;
}

.hero-callout--bottom {
    right: 1.25rem;
    bottom: 1.4rem;
}

.page-visual__frame {
    position: relative;
    overflow: hidden;
    min-height: 390px;
    border-radius: 2rem;
    border: 1px solid var(--theme-border);
    background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.04), rgba(255, 255, 255, 0.02)),
        var(--theme-surface-strong);
    box-shadow: 0 24px 70px rgba(2, 6, 23, 0.3);
}

.page-visual__media,
.page-visual__shade {
    position: absolute;
    inset: 0;
}

.page-visual__image {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.page-visual__shade {
    background: linear-gradient(180deg, rgba(8, 17, 31, 0.12), rgba(8, 17, 31, 0.68));
}

html[data-theme='light'] .page-visual__shade {
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.08), rgba(248, 250, 252, 0.45));
}

.page-visual__graphic {
    position: absolute;
    top: 1rem;
    right: 1rem;
    width: min(42%, 230px);
}

.page-visual__stack {
    position: absolute;
    left: 1rem;
    right: 1rem;
    bottom: 1rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.7rem;
}

.page-chip {
    display: inline-flex;
    align-items: center;
    border-radius: 999px;
    border: 1px solid rgba(255, 255, 255, 0.12);
    background: rgba(8, 17, 31, 0.68);
    padding: 0.6rem 0.9rem;
    font-size: 0.78rem;
    font-weight: 600;
    color: #dce6f3;
    backdrop-filter: blur(16px);
}

html[data-theme='light'] .page-chip {
    background: rgba(255, 255, 255, 0.88);
    border-color: rgba(15, 23, 42, 0.08);
    color: #0f172a;
}

.solution-card__graphic {
    min-height: 6.8rem;
}

.service-graphic {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    min-height: 132px;
}

.service-graphic--compact {
    min-height: 104px;
}

.service-graphic svg {
    width: 100%;
    max-width: 220px;
    height: auto;
}

.sg-panel {
    fill: rgba(255, 255, 255, 0.04);
    stroke: rgba(255, 255, 255, 0.1);
    stroke-width: 1.5;
}

.sg-soft {
    fill: rgba(255, 255, 255, 0.08);
}

.sg-dot {
    fill: rgba(255, 255, 255, 0.42);
}

html[data-theme='light'] .sg-panel {
    fill: rgba(255, 255, 255, 0.72);
    stroke: rgba(15, 23, 42, 0.08);
}

html[data-theme='light'] .sg-soft {
    fill: rgba(15, 23, 42, 0.08);
}

html[data-theme='light'] .sg-dot {
    fill: rgba(15, 23, 42, 0.25);
}

.sg-pulse {
    animation: sgPulse 4.8s ease-in-out infinite;
    transform-origin: center;
}

.sg-float {
    animation: sgFloat 5.6s ease-in-out infinite;
}

.sg-dash {
    stroke-dasharray: 8 10;
    animation: sgDash 12s linear infinite;
}

.sg-orbit {
    stroke-dasharray: 6 8;
    animation: sgOrbit 18s linear infinite;
    transform-origin: center;
}

.wizard-status-card {
    min-width: 16rem;
    border-radius: 1.4rem;
    border: 1px solid var(--theme-border);
    background: var(--theme-soft);
    padding: 1rem 1.1rem;
}

.wizard-status-card__top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.75rem;
}

.wizard-steps {
    display: grid;
    gap: 0.75rem;
}

@media (min-width: 768px) {
    .wizard-steps {
        grid-template-columns: repeat(7, minmax(0, 1fr));
    }
}

.wizard-panel-stack {
    min-height: 34rem;
}

.wizard-panel {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    min-height: 34rem;
}

.wizard-panel__eyebrow {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #85c0ff;
}

.wizard-panel__title {
    margin-top: 0.85rem;
    font-family: 'Space Grotesk', Inter, sans-serif;
    font-size: clamp(2rem, 3vw, 2.6rem);
    line-height: 1.05;
    font-weight: 700;
    color: var(--theme-heading);
}

.wizard-panel__text {
    margin-top: 1rem;
    max-width: 42rem;
    font-size: 1rem;
    line-height: 1.8;
    color: var(--theme-muted);
}

.choice-grid {
    display: grid;
    gap: 1rem;
}

.choice-grid--services {
    grid-template-columns: repeat(1, minmax(0, 1fr));
}

@media (min-width: 768px) {
    .choice-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .choice-grid--services {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }
}

@media (min-width: 1200px) {
    .choice-grid--services {
        grid-template-columns: repeat(3, minmax(0, 1fr));
    }
}

.choice-card {
    min-height: 7.5rem;
    border-radius: 1.35rem;
    border: 1px solid var(--theme-border);
    background: var(--theme-soft);
    padding: 1rem 1rem 1.05rem;
    text-align: left;
    transition: transform 180ms ease, border-color 180ms ease, background 180ms ease, box-shadow 180ms ease;
}

.choice-card:hover {
    transform: translateY(-2px);
    border-color: rgba(71, 153, 255, 0.22);
    background: rgba(24, 112, 248, 0.08);
}

.choice-card.is-selected {
    border-color: rgba(71, 153, 255, 0.36);
    background: linear-gradient(180deg, rgba(24, 112, 248, 0.16), rgba(255, 255, 255, 0.04));
    box-shadow: 0 12px 32px rgba(15, 23, 42, 0.16);
}

.choice-card--compact {
    min-height: auto;
}

.choice-card__title {
    display: block;
    font-size: 1rem;
    font-weight: 600;
    color: var(--theme-heading);
}

.choice-card__meta {
    display: block;
    margin-top: 0.55rem;
    font-size: 0.88rem;
    line-height: 1.65;
    color: var(--theme-muted);
}

.wizard-actions {
    display: flex;
    align-items: center;
    gap: 1rem;
    border-top: 1px solid var(--theme-border);
    padding-top: 1.6rem;
}

.wizard-review__item {
    display: flex;
    flex-direction: column;
    gap: 0.45rem;
    border-radius: 1rem;
    border: 1px solid var(--theme-border);
    background: var(--theme-soft);
    padding: 1rem;
}

.wizard-review__label {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #85c0ff;
}

.wizard-review__value {
    font-size: 0.95rem;
    line-height: 1.6;
    color: var(--theme-heading);
}

.wizard-review__value--block {
    white-space: pre-wrap;
}

.field-control {
    background: rgba(2, 6, 23, 0.42);
    border-color: var(--theme-border);
    color: var(--theme-heading);
}

.field-control::placeholder {
    color: var(--theme-muted);
}

html[data-theme='light'] .field-control {
    background: rgba(255, 255, 255, 0.86);
    box-shadow: none;
}

.page-header-shell,
.hero-home-shell {
    position: relative;
}

@media (max-width: 1023px) {
    .hero-media__screen,
    .page-visual__frame {
        min-height: 320px;
    }

    .hero-media__image {
        min-height: 320px;
    }

    .page-visual__graphic {
        width: min(46%, 180px);
    }
}

@media (max-width: 767px) {
    .hero-callout--top {
        top: auto;
        left: 1rem;
        bottom: 7rem;
    }

    .hero-callout--left {
        left: 1rem;
        bottom: 1rem;
    }

    .hero-callout--bottom {
        display: none;
    }

    .wizard-panel,
    .wizard-panel-stack {
        min-height: auto;
    }

    .wizard-actions {
        flex-direction: column;
        align-items: stretch;
    }

    .wizard-actions .ml-auto {
        margin-left: 0 !important;
        width: 100%;
    }

    .wizard-actions .button-primary,
    .wizard-actions .button-secondary {
        width: 100%;
        justify-content: center;
    }
}

@keyframes scanMove {
    0%,
    100% { transform: translateY(30%); }
    50% { transform: translateY(-50%); }
}

@keyframes sgPulse {
    0%,
    100% { transform: scale(1); opacity: 0.9; }
    50% { transform: scale(1.12); opacity: 1; }
}

@keyframes sgFloat {
    0%,
    100% { transform: translateY(0); }
    50% { transform: translateY(-4px); }
}

@keyframes sgDash {
    to { stroke-dashoffset: -120; }
}

@keyframes sgOrbit {
    to { transform: rotate(360deg); }
}
@media (max-width: 640px) {
    .theme-switch__label {
        display: none;
    }

    .theme-switch {
        padding: 0.72rem;
    }
}


/* === Visual refresh and component system overrides === */
.section-title {
    color: var(--theme-heading);
}

.section-intro {
    color: var(--theme-muted-strong);
}

.eyebrow {
    color: #85c0ff;
}

.eyebrow--compact {
    font-size: 0.66rem;
    letter-spacing: 0.18em;
}

html[data-theme='light'] {
    --theme-bg: #edf4fb;
    --theme-bg-alt: #f8fbff;
    --theme-surface: rgba(255, 255, 255, 0.78);
    --theme-surface-strong: rgba(255, 255, 255, 0.9);
    --theme-border: rgba(15, 23, 42, 0.09);
    --theme-heading: #091525;
    --theme-copy: #3a4b62;
    --theme-muted: #66768c;
    --theme-muted-strong: #475569;
    --theme-soft: rgba(15, 23, 42, 0.035);
    --theme-header: rgba(248, 251, 255, 0.84);
    --theme-footer: rgba(244, 248, 252, 0.96);
}

html[data-theme='light'] body {
    background:
        radial-gradient(circle at 10% 0%, rgba(24, 112, 248, 0.16), transparent 23%),
        radial-gradient(circle at 100% 5%, rgba(78, 231, 194, 0.1), transparent 20%),
        radial-gradient(circle at 0% 80%, rgba(24, 112, 248, 0.08), transparent 24%),
        linear-gradient(180deg, #eef5fb 0%, #f8fbff 44%, #edf3f9 100%);
}

html[data-theme='light'] .ambient-orb--one {
    background: radial-gradient(circle, rgba(24, 112, 248, 0.3), rgba(24, 112, 248, 0.02) 70%);
    opacity: 0.18;
}

html[data-theme='light'] .ambient-orb--two {
    background: radial-gradient(circle, rgba(78, 231, 194, 0.28), rgba(78, 231, 194, 0.02) 72%);
    opacity: 0.12;
}

html[data-theme='light'] .ambient-beam {
    opacity: 0.06;
}

html[data-theme='light'] .hero-home-shell,
html[data-theme='light'] .page-header-shell {
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.26), rgba(255, 255, 255, 0));
}

html[data-theme='light'] .hero-benefit,
html[data-theme='light'] .overview-stat,
html[data-theme='light'] .overview-mini-card,
html[data-theme='light'] .authority-card,
html[data-theme='light'] .cluster-card,
html[data-theme='light'] .media-carousel__navitem {
    background: rgba(255, 255, 255, 0.72);
}

.pointer-glow::after {
    background: radial-gradient(340px circle at var(--pointer-x, 50%) var(--pointer-y, 50%), rgba(71, 153, 255, 0.14), transparent 48%);
}

.surface-card {
    overflow: hidden;
}

.surface-card::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: inherit;
    background: linear-gradient(135deg, rgba(71, 153, 255, 0.08), transparent 34%, rgba(78, 231, 194, 0.08));
    opacity: 0;
    transition: opacity 220ms ease;
    pointer-events: none;
}

.surface-card:hover::before {
    opacity: 1;
}

.service-graphic svg {
    transition: transform 260ms ease, filter 260ms ease;
}

.surface-card:hover .service-graphic svg,
.surface-card:focus-within .service-graphic svg {
    transform: translateY(-4px) scale(1.01);
    filter: drop-shadow(0 18px 26px rgba(24, 112, 248, 0.16));
}

.hero-benefit,
.overview-stat,
.overview-mini-card {
    transition: transform 180ms ease, border-color 180ms ease, background 180ms ease, box-shadow 180ms ease;
}

.hero-benefit:hover,
.overview-stat:hover,
.overview-mini-card:hover {
    transform: translateY(-2px);
    border-color: rgba(71, 153, 255, 0.18);
    box-shadow: 0 18px 32px rgba(2, 6, 23, 0.12);
}

.hero-benefit {
    position: relative;
    overflow: hidden;
}

.hero-benefit::after {
    content: '';
    position: absolute;
    inset-inline: 0;
    bottom: 0;
    height: 2px;
    background: linear-gradient(90deg, rgba(24, 112, 248, 0), rgba(24, 112, 248, 0.72), rgba(78, 231, 194, 0));
    opacity: 0;
    transition: opacity 180ms ease;
}

.hero-benefit:hover::after {
    opacity: 1;
}

.authority-card {
    min-height: 100%;
}

.authority-card__header {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.authority-card__number {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 2.9rem;
    height: 2.9rem;
    border-radius: 1rem;
    border: 1px solid var(--theme-border);
    background: linear-gradient(180deg, rgba(24, 112, 248, 0.16), rgba(255, 255, 255, 0.04));
    color: #85c0ff;
    font-weight: 700;
    letter-spacing: 0.04em;
}

.authority-card__line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, rgba(71, 153, 255, 0.42), rgba(78, 231, 194, 0));
    transform-origin: left center;
    transition: transform 220ms ease;
}

.authority-card:hover .authority-card__line {
    transform: scaleX(1.08);
}

.hero-carousel-shell {
    position: relative;
}

.hero-carousel-shell__glow {
    position: absolute;
    inset: -2rem;
    border-radius: 2.5rem;
    background: radial-gradient(circle at center, rgba(24, 112, 248, 0.16), transparent 64%);
    filter: blur(28px);
}

.media-carousel {
    position: relative;
    overflow: hidden;
    border-radius: 2rem;
    border: 1px solid var(--theme-border);
    background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.02)),
        var(--theme-surface-strong);
    box-shadow: 0 28px 84px rgba(2, 6, 23, 0.3);
}

.media-carousel__topbar {
    position: relative;
    z-index: 6;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    padding: 1rem 1rem 0;
}

.media-carousel__viewport {
    position: relative;
    min-height: 420px;
}

.media-carousel--page .media-carousel__viewport {
    min-height: 390px;
}

.media-carousel__slide {
    position: absolute;
    inset: 0;
    opacity: 0;
    transform: scale(1.03);
    transition: opacity 420ms ease, transform 700ms ease;
    pointer-events: none;
}

.media-carousel__slide.is-active {
    opacity: 1;
    transform: scale(1);
    pointer-events: auto;
}

.media-carousel__image,
.media-carousel__shade {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
}

.media-carousel__image {
    object-fit: cover;
}

.media-carousel__shade {
    background:
        linear-gradient(180deg, rgba(8, 17, 31, 0.18), rgba(8, 17, 31, 0.78)),
        radial-gradient(circle at 78% 22%, rgba(24, 112, 248, 0.22), transparent 22%);
}

html[data-theme='light'] .media-carousel__shade {
    background:
        linear-gradient(180deg, rgba(248, 250, 252, 0.08), rgba(248, 250, 252, 0.56)),
        linear-gradient(180deg, rgba(15, 23, 42, 0.08), rgba(15, 23, 42, 0.28));
}

.media-carousel__content {
    position: absolute;
    left: 1rem;
    right: 1rem;
    bottom: 1rem;
    z-index: 3;
    max-width: min(32rem, calc(100% - 2rem));
    border-radius: 1.4rem;
    border: 1px solid rgba(255, 255, 255, 0.12);
    background: rgba(8, 17, 31, 0.72);
    padding: 1.05rem 1.1rem 1.1rem;
    box-shadow: 0 20px 44px rgba(2, 6, 23, 0.28);
    backdrop-filter: blur(16px);
}

.media-carousel__content--page {
    max-width: min(26rem, calc(100% - 2rem));
}

html[data-theme='light'] .media-carousel__content {
    background: rgba(255, 255, 255, 0.84);
    border-color: rgba(15, 23, 42, 0.08);
}

.media-carousel__eyebrow {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #85c0ff;
}

.media-carousel__title {
    margin-top: 0.6rem;
    font-family: 'Space Grotesk', Inter, sans-serif;
    font-size: clamp(1.45rem, 3vw, 2rem);
    line-height: 1.05;
    font-weight: 700;
    color: #ffffff;
}

html[data-theme='light'] .media-carousel__title {
    color: #091525;
}

.media-carousel__text {
    margin-top: 0.75rem;
    font-size: 0.93rem;
    line-height: 1.7;
    color: #d5e3f4;
}

html[data-theme='light'] .media-carousel__text {
    color: #475569;
}

.media-carousel__chips {
    margin-top: 0.85rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.55rem;
}

.media-carousel__chips span {
    display: inline-flex;
    align-items: center;
    border-radius: 999px;
    border: 1px solid rgba(255, 255, 255, 0.14);
    background: rgba(255, 255, 255, 0.05);
    padding: 0.45rem 0.72rem;
    font-size: 0.72rem;
    font-weight: 600;
    color: #e2edf9;
}

html[data-theme='light'] .media-carousel__chips span {
    background: rgba(15, 23, 42, 0.04);
    border-color: rgba(15, 23, 42, 0.08);
    color: #334155;
}

.media-carousel__footer {
    position: relative;
    z-index: 6;
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    gap: 1rem;
    padding: 0 1rem 1rem;
}

.media-carousel__footer--page {
    align-items: center;
}

.media-carousel__navlist {
    display: grid;
    flex: 1;
    gap: 0.7rem;
    grid-template-columns: repeat(2, minmax(0, 1fr));
}

.media-carousel__navitem {
    display: flex;
    flex-direction: column;
    gap: 0.18rem;
    align-items: flex-start;
    border-radius: 1rem;
    border: 1px solid var(--theme-border);
    background: rgba(255, 255, 255, 0.04);
    padding: 0.82rem 0.9rem;
    text-align: left;
    transition: transform 180ms ease, border-color 180ms ease, background 180ms ease;
}

.media-carousel__navitem:hover,
.media-carousel__navitem.is-active {
    transform: translateY(-1px);
    border-color: rgba(71, 153, 255, 0.22);
    background: rgba(24, 112, 248, 0.1);
}

.media-carousel__navlabel {
    font-size: 0.86rem;
    font-weight: 600;
    color: var(--theme-heading);
}

.media-carousel__navmeta {
    font-size: 0.74rem;
    line-height: 1.55;
    color: var(--theme-muted);
}

.media-carousel__controls {
    display: flex;
    align-items: center;
    gap: 0.55rem;
}

.carousel-control {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 2.8rem;
    height: 2.8rem;
    border-radius: 999px;
    border: 1px solid var(--theme-border);
    background: rgba(255, 255, 255, 0.06);
    color: var(--theme-heading);
    transition: transform 180ms ease, border-color 180ms ease, background 180ms ease;
}

.carousel-control:hover {
    transform: translateY(-1px);
    border-color: rgba(71, 153, 255, 0.28);
    background: rgba(24, 112, 248, 0.12);
}

.carousel-control svg {
    width: 1rem;
    height: 1rem;
}

.media-carousel__dots {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
}

.media-carousel__dot {
    width: 0.58rem;
    height: 0.58rem;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.28);
    transition: transform 180ms ease, background 180ms ease, width 180ms ease;
}

.media-carousel__dot.is-active {
    width: 1.55rem;
    background: linear-gradient(90deg, rgba(24, 112, 248, 0.95), rgba(78, 231, 194, 0.9));
}

html[data-theme='light'] .media-carousel__dot {
    background: rgba(15, 23, 42, 0.16);
}

.hero-carousel-shell__badges {
    pointer-events: none;
}

.hero-floating-chip {
    position: absolute;
    z-index: 5;
    border-radius: 999px;
    border: 1px solid rgba(255, 255, 255, 0.12);
    background: rgba(8, 17, 31, 0.72);
    padding: 0.72rem 0.95rem;
    font-size: 0.76rem;
    font-weight: 600;
    color: #dce6f3;
    backdrop-filter: blur(16px);
    animation: heroChipFloat 9s ease-in-out infinite;
}

html[data-theme='light'] .hero-floating-chip {
    background: rgba(255, 255, 255, 0.86);
    border-color: rgba(15, 23, 42, 0.08);
    color: #334155;
}

.hero-floating-chip--one {
    left: 1rem;
    top: 4.75rem;
}

.hero-floating-chip--two {
    right: 1rem;
    top: 8rem;
    animation-delay: 1.2s;
}

.hero-floating-chip--three {
    right: 1rem;
    bottom: 7.25rem;
    animation-delay: 2.4s;
}

.overview-stat {
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
    border-radius: 1.2rem;
    border: 1px solid var(--theme-border);
    background: var(--theme-soft);
    padding: 1rem;
}

.overview-stat__kicker {
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: #85c0ff;
}

.overview-stat__value {
    color: var(--theme-heading);
    font-weight: 600;
    line-height: 1.6;
}

.overview-board {
    display: grid;
    gap: 1rem;
}

.overview-board__hero {
    position: relative;
    overflow: hidden;
    border-radius: 1.45rem;
    min-height: 320px;
}

.overview-board__image,
.overview-board__shade {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
}

.overview-board__image {
    object-fit: cover;
}

.overview-board__shade {
    background: linear-gradient(180deg, rgba(8, 17, 31, 0.12), rgba(8, 17, 31, 0.74));
}

.overview-board__copy {
    position: absolute;
    left: 1rem;
    right: 1rem;
    bottom: 1rem;
    border-radius: 1.2rem;
    border: 1px solid rgba(255, 255, 255, 0.12);
    background: rgba(8, 17, 31, 0.64);
    padding: 1rem;
    backdrop-filter: blur(14px);
}

html[data-theme='light'] .overview-board__copy {
    background: rgba(255, 255, 255, 0.84);
    border-color: rgba(15, 23, 42, 0.08);
}

.overview-board__eyebrow {
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #85c0ff;
}

.overview-board__title {
    margin-top: 0.55rem;
    font-family: 'Space Grotesk', Inter, sans-serif;
    font-size: clamp(1.3rem, 2.6vw, 1.9rem);
    line-height: 1.15;
    font-weight: 700;
    color: #ffffff;
}

html[data-theme='light'] .overview-board__title {
    color: #091525;
}

.overview-board__grid {
    display: grid;
    gap: 0.85rem;
    grid-template-columns: repeat(2, minmax(0, 1fr));
}

.overview-mini-card {
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
    border-radius: 1.2rem;
    border: 1px solid var(--theme-border);
    background: var(--theme-soft);
    padding: 1rem;
}

.overview-mini-card__title {
    font-weight: 600;
    color: var(--theme-heading);
}

.overview-mini-card__text {
    font-size: 0.86rem;
    line-height: 1.65;
    color: var(--theme-muted);
}

.team-card__media {
    position: relative;
    overflow: hidden;
    aspect-ratio: 4 / 5;
    border-radius: 1.45rem;
    border: 1px solid var(--theme-border);
}

.team-card__image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 420ms ease;
}

.team-card:hover .team-card__image {
    transform: scale(1.03);
}

.team-card__badge {
    position: absolute;
    left: 0.9rem;
    top: 0.9rem;
    display: inline-flex;
    align-items: center;
    border-radius: 999px;
    border: 1px solid rgba(255, 255, 255, 0.12);
    background: rgba(8, 17, 31, 0.68);
    padding: 0.5rem 0.72rem;
    font-size: 0.72rem;
    font-weight: 600;
    color: #dce6f3;
    backdrop-filter: blur(12px);
}

html[data-theme='light'] .team-card__badge {
    background: rgba(255, 255, 255, 0.88);
    border-color: rgba(15, 23, 42, 0.08);
    color: #334155;
}

.footer-nav-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.footer-nav-link {
    display: inline-flex;
    align-items: center;
    padding: 0;
    border: 0;
    background: transparent;
    color: var(--theme-copy);
    line-height: 1.6;
}

.footer-nav-link:hover {
    transform: none;
    border: 0;
    background: transparent;
    color: var(--theme-heading);
}

.theme-toggle-switch {
    display: inline-flex;
    align-items: center;
    gap: 0.7rem;
    border-radius: 999px;
    border: 1px solid var(--theme-border);
    background: var(--theme-soft);
    padding: 0.38rem 0.5rem 0.38rem 0.42rem;
    color: var(--theme-heading);
    transition: transform 180ms ease, border-color 180ms ease, background 180ms ease;
    backdrop-filter: blur(16px);
}

.theme-toggle-switch:hover {
    transform: translateY(-1px);
    border-color: rgba(71, 153, 255, 0.24);
}

.theme-toggle-switch__track {
    position: relative;
    display: inline-flex;
    align-items: center;
    justify-content: space-between;
    gap: 1.55rem;
    width: 3.5rem;
    height: 2rem;
    border-radius: 999px;
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.08), rgba(255, 255, 255, 0.03));
    padding: 0 0.35rem;
}

html[data-theme='light'] .theme-toggle-switch__track {
    background: rgba(15, 23, 42, 0.05);
}

.theme-toggle-switch__thumb {
    position: absolute;
    left: 0.18rem;
    top: 0.18rem;
    width: 1.64rem;
    height: 1.64rem;
    border-radius: 999px;
    background: linear-gradient(135deg, #1870f8, #4ee7c2);
    box-shadow: 0 8px 18px rgba(24, 112, 248, 0.22);
    transition: transform 220ms ease;
}

html[data-theme='light'] .theme-toggle-switch__thumb {
    transform: translateX(1.48rem);
}

.theme-toggle-switch__icon {
    position: relative;
    z-index: 1;
    width: 0.88rem;
    height: 0.88rem;
    color: var(--theme-heading);
}

.theme-toggle-switch__icon svg {
    width: 100%;
    height: 100%;
}

.theme-toggle-switch__label {
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.04em;
}

.media-carousel--page .media-carousel__dots {
    gap: 0.45rem;
}

.wizard-steps {
    display: flex;
    gap: 0.8rem;
    overflow-x: auto;
    padding-bottom: 0.35rem;
    scrollbar-width: none;
    scroll-snap-type: x proximity;
}

.wizard-steps::-webkit-scrollbar {
    display: none;
}

.step-chip {
    flex: 0 0 11rem;
    min-width: 11rem;
    scroll-snap-align: start;
    min-height: 6.2rem;
    border-radius: 1.2rem;
    background: rgba(2, 6, 23, 0.38);
}

html[data-theme='light'] .step-chip {
    background: rgba(255, 255, 255, 0.76);
}

.step-chip__index {
    min-width: 2.25rem;
    min-height: 2.25rem;
    border-radius: 0.85rem;
    background: rgba(24, 112, 248, 0.14);
    color: #85c0ff;
}

.step-chip.is-current .step-chip__index {
    background: linear-gradient(135deg, rgba(24, 112, 248, 0.24), rgba(78, 231, 194, 0.16));
}

.wizard-panel-stack {
    min-height: 31rem;
}

.wizard-panel {
    min-height: 31rem;
}

.wizard-status-card {
    min-width: 18rem;
}

.step-chip__hint {
    color: var(--theme-muted);
}

@media (max-width: 767px) {
    .theme-toggle-switch__label {
        display: none;
    }

    .media-carousel__viewport {
        min-height: 360px;
    }

    .media-carousel--page .media-carousel__viewport {
        min-height: 330px;
    }

    .media-carousel__content,
    .media-carousel__content--page {
        max-width: calc(100% - 2rem);
    }

    .media-carousel__footer {
        flex-direction: column;
        align-items: stretch;
    }

    .media-carousel__navlist {
        grid-template-columns: repeat(1, minmax(0, 1fr));
    }

    .hero-floating-chip--two,
    .hero-floating-chip--three {
        display: none;
    }

    .overview-board__grid {
        grid-template-columns: repeat(1, minmax(0, 1fr));
    }

    .step-chip {
        flex-basis: 9.5rem;
        min-width: 9.5rem;
        min-height: 5.6rem;
    }

    .step-chip__hint {
        display: none;
    }

    .wizard-status-card {
        min-width: 0;
    }
}

@media (min-width: 1024px) {
    .media-carousel--page .media-carousel__content--page {
        max-width: 23rem;
    }
}

@media (min-width: 1280px) {
    .media-carousel__viewport {
        min-height: 450px;
    }
}

@keyframes heroChipFloat {
    0%,
    100% { transform: translateY(0); }
    50% { transform: translateY(-4px); }
}


/* === Final light-mode and interaction polish === */
html[data-theme='light'] .gradient-text {
    background: linear-gradient(135deg, #0e57d4 0%, #1870f8 46%, #0fa97f 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}

html[data-theme='light'] .hover\:text-white:hover,
html[data-theme='light'] .hover\:text-white:focus-visible,
html[data-theme='light'] .hover\:text-slate-300:hover,
html[data-theme='light'] .hover\:text-slate-300:focus-visible {
    color: var(--theme-heading) !important;
}

html[data-theme='light'] .hover\:bg-white\/5:hover,
html[data-theme='light'] .hover\:bg-white\/5:focus-visible {
    background-color: rgba(15, 23, 42, 0.04) !important;
}

html[data-theme='light'] .hover\:bg-white\/10:hover,
html[data-theme='light'] .hover\:bg-white\/10:focus-visible {
    background-color: rgba(15, 23, 42, 0.06) !important;
}

html[data-theme='light'] body > header .text-slate-400 {
    color: #526277 !important;
}

html[data-theme='light'] body > header .text-slate-300 {
    color: #334155 !important;
}

html[data-theme='light'] body > header .button-primary {
    box-shadow: 0 14px 30px rgba(24, 112, 248, 0.18);
}

html[data-theme='light'] .status-chip-live {
    color: #0f7b66;
    background: rgba(78, 231, 194, 0.16);
    border-color: rgba(15, 23, 42, 0.08);
}

html[data-theme='light'] .hero-carousel-shell__glow {
    background: radial-gradient(circle at center, rgba(24, 112, 248, 0.12), transparent 66%);
}

html[data-theme='light'] .overview-board__copy,
html[data-theme='light'] .media-carousel__content,
html[data-theme='light'] .media-carousel__content--page {
    text-shadow: 0 2px 20px rgba(255, 255, 255, 0.22);
}

html[data-theme='light'] .confirmation-inline-panel,
html[data-theme='light'] .success-panel {
    border-color: rgba(15, 23, 42, 0.08);
    background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.96), rgba(247, 250, 254, 0.96)),
        rgba(255, 255, 255, 0.96);
}

html[data-theme='light'] .confirmation-inline-panel .text-accent-100,
html[data-theme='light'] .success-panel .text-slate-300 {
    color: #475569 !important;
}

html[data-theme='light'] .success-panel .bg-white\/5 {
    background-color: rgba(15, 23, 42, 0.035) !important;
}

@media (max-width: 640px) {
    .wizard-actions {
        gap: 0.75rem;
    }

    .wizard-actions .ml-auto {
        margin-left: 0 !important;
        width: 100%;
    }

    .wizard-actions .button-secondary,
    .wizard-actions .button-primary {
        width: 100%;
        justify-content: center;
    }
}


============================================================
FILE: static/js/main.js
============================================================
(function () {
    const THEME_KEY = 'axial-theme';

    function currentTheme() {
        return document.documentElement.getAttribute('data-theme') || 'dark';
    }

    function applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        try {
            localStorage.setItem(THEME_KEY, theme);
        } catch (error) {
            // ignore storage issues
        }

        const meta = document.querySelector('meta[name="theme-color"]');
        if (meta) {
            meta.setAttribute('content', theme === 'light' ? '#f6f9fd' : '#08111f');
        }

        document.querySelectorAll('[data-theme-toggle]').forEach((button) => {
            const nextTheme = theme === 'dark' ? 'light' : 'dark';
            button.setAttribute('aria-label', `Switch to ${nextTheme} mode`);
            button.setAttribute('aria-checked', theme === 'light' ? 'true' : 'false');
            button.dataset.themeState = theme;
            const label = button.querySelector('[data-theme-label]');
            if (label) {
                label.textContent = theme === 'light' ? 'Light' : 'Dark';
            }
        });

        window.dispatchEvent(new CustomEvent('axial-theme-change', { detail: { theme } }));
    }

    function initThemeToggle() {
        const initialTheme = currentTheme();
        applyTheme(initialTheme);

        document.querySelectorAll('[data-theme-toggle]').forEach((button) => {
            button.addEventListener('click', () => {
                applyTheme(currentTheme() === 'dark' ? 'light' : 'dark');
            });
        });
    }

    function initAnimatedBackground() {
        const canvas = document.querySelector('[data-animated-bg]');
        if (!canvas) {
            return;
        }

        const prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        const context = canvas.getContext('2d');
        let width = 0;
        let height = 0;
        let nodes = [];
        let animationFrame;

        function palette() {
            if (currentTheme() === 'light') {
                return {
                    dot: 'rgba(24,112,248,0.20)',
                    line: 'rgba(24,112,248,0.06)',
                    glow: 'rgba(78,231,194,0.06)',
                };
            }
            return {
                dot: 'rgba(78,231,194,0.28)',
                line: 'rgba(71,153,255,0.09)',
                glow: 'rgba(24,112,248,0.08)',
            };
        }

        function resize() {
            width = window.innerWidth;
            height = window.innerHeight;
            const ratio = Math.min(window.devicePixelRatio || 1, 1.5);
            canvas.width = Math.floor(width * ratio);
            canvas.height = Math.floor(height * ratio);
            canvas.style.width = `${width}px`;
            canvas.style.height = `${height}px`;
            context.setTransform(ratio, 0, 0, ratio, 0, 0);

            const count = Math.max(18, Math.min(38, Math.floor((width * height) / 52000)));
            nodes = Array.from({ length: count }, () => ({
                x: Math.random() * width,
                y: Math.random() * height,
                vx: (Math.random() - 0.5) * 0.22,
                vy: (Math.random() - 0.5) * 0.22,
                r: Math.random() * 1.8 + 1,
            }));
        }

        function draw() {
            const colors = palette();
            context.clearRect(0, 0, width, height);

            const glow = context.createRadialGradient(width * 0.82, height * 0.18, 0, width * 0.82, height * 0.18, width * 0.45);
            glow.addColorStop(0, colors.glow);
            glow.addColorStop(1, 'rgba(0,0,0,0)');
            context.fillStyle = glow;
            context.fillRect(0, 0, width, height);

            nodes.forEach((node) => {
                node.x += node.vx;
                node.y += node.vy;
                if (node.x < -20) node.x = width + 20;
                if (node.x > width + 20) node.x = -20;
                if (node.y < -20) node.y = height + 20;
                if (node.y > height + 20) node.y = -20;
            });

            for (let i = 0; i < nodes.length; i += 1) {
                for (let j = i + 1; j < nodes.length; j += 1) {
                    const a = nodes[i];
                    const b = nodes[j];
                    const distance = Math.hypot(a.x - b.x, a.y - b.y);
                    if (distance < 160) {
                        context.strokeStyle = colors.line;
                        context.lineWidth = 1;
                        context.beginPath();
                        context.moveTo(a.x, a.y);
                        context.lineTo(b.x, b.y);
                        context.stroke();
                    }
                }
            }

            nodes.forEach((node) => {
                context.fillStyle = colors.dot;
                context.beginPath();
                context.arc(node.x, node.y, node.r, 0, Math.PI * 2);
                context.fill();
            });

            animationFrame = window.requestAnimationFrame(draw);
        }

        resize();
        window.addEventListener('resize', resize);
        window.addEventListener('axial-theme-change', resize);

        if (prefersReducedMotion) {
            draw();
            if (animationFrame) {
                window.cancelAnimationFrame(animationFrame);
            }
            return;
        }

        draw();
    }

    function initPointerGlow() {
        document.querySelectorAll('.pointer-glow').forEach((element) => {
            element.addEventListener('pointermove', (event) => {
                const rect = element.getBoundingClientRect();
                const x = ((event.clientX - rect.left) / rect.width) * 100;
                const y = ((event.clientY - rect.top) / rect.height) * 100;
                element.style.setProperty('--pointer-x', `${x}%`);
                element.style.setProperty('--pointer-y', `${y}%`);
                element.classList.add('is-active');
            });
            element.addEventListener('pointerleave', () => {
                element.classList.remove('is-active');
            });
        });
    }


    function initMediaCarousels() {
        const prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

        document.querySelectorAll('[data-media-carousel]').forEach((carousel) => {
            const slides = Array.from(carousel.querySelectorAll('[data-carousel-slide]'));
            if (slides.length <= 1) {
                return;
            }

            const dots = Array.from(carousel.querySelectorAll('[data-carousel-dot]'));
            const jumps = Array.from(carousel.querySelectorAll('[data-carousel-jump]'));
            const nextButton = carousel.querySelector('[data-carousel-next]');
            const prevButton = carousel.querySelector('[data-carousel-prev]');
            const interval = Number.parseInt(carousel.dataset.interval || '5600', 10);
            let activeIndex = 0;
            let timer = null;
            let startX = 0;
            let isTouching = false;

            function show(index) {
                activeIndex = (index + slides.length) % slides.length;
                slides.forEach((slide, slideIndex) => {
                    const active = slideIndex === activeIndex;
                    slide.classList.toggle('is-active', active);
                    slide.setAttribute('aria-hidden', active ? 'false' : 'true');
                });
                dots.forEach((dot, dotIndex) => dot.classList.toggle('is-active', dotIndex === activeIndex));
                jumps.forEach((jump, jumpIndex) => jump.classList.toggle('is-active', jumpIndex === activeIndex));
            }

            function next() {
                show(activeIndex + 1);
            }

            function prev() {
                show(activeIndex - 1);
            }

            function stopTimer() {
                if (timer) {
                    window.clearInterval(timer);
                    timer = null;
                }
            }

            function startTimer() {
                stopTimer();
                if (prefersReducedMotion) {
                    return;
                }
                timer = window.setInterval(next, interval);
            }

            if (nextButton) {
                nextButton.addEventListener('click', () => {
                    next();
                    startTimer();
                });
            }

            if (prevButton) {
                prevButton.addEventListener('click', () => {
                    prev();
                    startTimer();
                });
            }

            dots.forEach((dot, index) => {
                dot.addEventListener('click', () => {
                    show(index);
                    startTimer();
                });
            });

            jumps.forEach((jump, index) => {
                jump.addEventListener('click', () => {
                    show(index);
                    startTimer();
                });
            });

            carousel.addEventListener('mouseenter', stopTimer);
            carousel.addEventListener('mouseleave', startTimer);
            carousel.addEventListener('focusin', stopTimer);
            carousel.addEventListener('focusout', startTimer);

            carousel.addEventListener('touchstart', (event) => {
                if (!event.touches || !event.touches[0]) {
                    return;
                }
                startX = event.touches[0].clientX;
                isTouching = true;
            }, { passive: true });

            carousel.addEventListener('touchend', (event) => {
                if (!isTouching || !event.changedTouches || !event.changedTouches[0]) {
                    return;
                }
                const deltaX = event.changedTouches[0].clientX - startX;
                if (Math.abs(deltaX) > 40) {
                    if (deltaX < 0) {
                        next();
                    } else {
                        prev();
                    }
                    startTimer();
                }
                isTouching = false;
            }, { passive: true });

            show(0);
            startTimer();
        });
    }

    function initReveals() {
        const revealTargets = Array.from(
            document.querySelectorAll('[data-reveal], .surface-card, .section-title, .section-intro, .confirmation-inline-panel')
        );

        revealTargets.forEach((element, index) => {
            element.classList.add('reveal-ready');
            element.style.transitionDelay = `${Math.min(index % 6, 5) * 55}ms`;
        });

        if ('IntersectionObserver' in window) {
            const observer = new IntersectionObserver(
                (entries) => {
                    entries.forEach((entry) => {
                        if (entry.isIntersecting) {
                            entry.target.classList.add('is-visible');
                            observer.unobserve(entry.target);
                        }
                    });
                },
                { threshold: 0.12, rootMargin: '0px 0px -6% 0px' }
            );
            revealTargets.forEach((element) => observer.observe(element));
        } else {
            revealTargets.forEach((element) => element.classList.add('is-visible'));
        }
    }

    function initFlashMessages() {
        document.querySelectorAll('[data-flash]').forEach((item) => {
            setTimeout(() => {
                item.style.transition = 'opacity 220ms ease, transform 220ms ease';
                item.style.opacity = '0';
                item.style.transform = 'translateY(-6px)';
                setTimeout(() => item.remove(), 250);
            }, 6500);
        });
    }

    function syncReferrerFields() {
        document.querySelectorAll('[data-referrer-field]').forEach((field) => {
            if (document.referrer) {
                field.value = document.referrer;
            }
        });
    }

    window.contactExperience = function () {
        return {
            step: 1,
            submitting: false,
            successOpen: false,
            successMessage: 'Your information has been submitted successfully. Our team will review the brief and contact you directly.',
            successSteps: [
                'We will review the project brief and service fit.',
                'Our team will contact you with a practical next step.',
                'If useful, we will recommend a scoped discovery conversation or starting build route.',
            ],
            errorMessage: '',
            serverErrors: {},
            steps: [
                { index: 1, label: 'Need', hint: 'Choose the main service' },
                { index: 2, label: 'Budget', hint: 'Set commercial range' },
                { index: 3, label: 'Timeline', hint: 'Share delivery timing' },
                { index: 4, label: 'Contact', hint: 'Add reply details' },
                { index: 5, label: 'Context', hint: 'Optional business info' },
                { index: 6, label: 'Brief', hint: 'Describe the project' },
                { index: 7, label: 'Review', hint: 'Submit the intake' },
            ],
            form: {
                inquiry_type: 'project',
                service_interest: '',
                budget: '',
                timeline: '',
                name: '',
                email: '',
                company: '',
                phone: '',
                message: '',
            },
            serviceLabels: {
                'ai-strategy': 'AI Strategy',
                'ai-chatbot': 'AI Chatbot / Assistant',
                'rag-knowledge': 'RAG / Knowledge Assistant',
                'llm-fine-tuning': 'LLM Fine-tuning',
                'speech-ai': 'Speech AI',
                'website-development': 'Website Development',
                'web-application-development': 'Web Application Development',
                'automation-backend-systems': 'Automation / Backend Systems',
                'data-pipelines-scraping': 'Data Pipelines / Scraping',
                'product-mvp-build': 'Product / MVP Build',
                'research-collaboration': 'Research Collaboration',
                other: 'Other',
            },
            budgetLabels: {
                'under-3000': 'Under $3,000',
                '3000-10000': '$3,000 – $10,000',
                '10000-25000': '$10,000 – $25,000',
                '25000-plus': '$25,000+',
                discuss: "Let's discuss",
            },

            init() {
                this.bindVisibleFieldListeners();
            },

            get progress() {
                return (this.step / this.steps.length) * 100;
            },

            get currentStep() {
                return this.steps[this.step - 1] || this.steps[0];
            },

            get readableService() {
                return this.serviceLabels[this.form.service_interest] || 'Not selected';
            },

            get readableBudget() {
                return this.budgetLabels[this.form.budget] || 'Not specified';
            },

            bindVisibleFieldListeners() {
                this.$nextTick(() => {
                    this.$root.querySelectorAll('[id^="wizard_"]').forEach((field) => {
                        field.addEventListener('input', () => {
                            const key = field.id.replace('wizard_', '');
                            this.clearError(key);
                            this.errorMessage = '';
                        });
                    });
                });
            },

            clearError(name) {
                if (this.serverErrors[name]) {
                    delete this.serverErrors[name];
                    this.serverErrors = { ...this.serverErrors };
                }
            },

            pickService(value) {
                this.form.service_interest = value;
                this.clearError('service_interest');
                this.errorMessage = '';
                setTimeout(() => this.goNext(), 120);
            },

            pickBudget(value) {
                this.form.budget = value;
                this.clearError('budget');
                this.errorMessage = '';
                setTimeout(() => this.goNext(), 120);
            },

            pickTimeline(value) {
                this.form.timeline = value;
                this.clearError('timeline');
                this.errorMessage = '';
                setTimeout(() => this.goNext(), 120);
            },

            goTo(index) {
                if (index < this.step) {
                    this.step = index;
                    return;
                }

                for (let current = this.step; current < index; current += 1) {
                    if (!this.validateStep(current)) {
                        return;
                    }
                }

                this.step = index;
            },

            goNext() {
                if (!this.validateStep(this.step)) {
                    return;
                }
                this.step = Math.min(this.step + 1, this.steps.length);
            },

            goBack() {
                this.step = Math.max(this.step - 1, 1);
            },

            validateEmail(value) {
                return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
            },

            focusById(id) {
                const target = document.getElementById(id);
                if (target) {
                    target.focus({ preventScroll: false });
                }
            },

            validateStep(index) {
                const name = (this.form.name || '').trim();
                const email = (this.form.email || '').trim();
                const message = (this.form.message || '').trim();

                if (index === 1 && !this.form.service_interest) {
                    this.serverErrors = { ...this.serverErrors, service_interest: 'Please choose the closest service fit.' };
                    return false;
                }

                if (index === 4) {
                    if (name.length < 2) {
                        this.serverErrors = { ...this.serverErrors, name: 'Please enter a valid name.' };
                        this.focusById('wizard_name');
                        return false;
                    }
                    if (!this.validateEmail(email)) {
                        this.serverErrors = { ...this.serverErrors, email: 'Please enter a valid email address.' };
                        this.focusById('wizard_email');
                        return false;
                    }
                }

                if (index === 6 && message.length < 20) {
                    this.serverErrors = { ...this.serverErrors, message: 'Please share a little more detail so we can respond usefully.' };
                    this.focusById('wizard_message');
                    return false;
                }

                return true;
            },

            validateBeforeSubmit() {
                for (let i = 1; i <= this.steps.length; i += 1) {
                    if (!this.validateStep(i)) {
                        this.step = i;
                        return false;
                    }
                }
                return true;
            },

            syncReferrers(formElement) {
                formElement.querySelectorAll('[data-referrer-field]').forEach((field) => {
                    if (document.referrer) {
                        field.value = document.referrer;
                    }
                });
            },

            applyServerErrors(errors = {}) {
                this.serverErrors = errors;
                const firstField = Object.keys(errors)[0];
                if (!firstField) {
                    return;
                }
                if (['service_interest'].includes(firstField)) this.step = 1;
                if (['budget'].includes(firstField)) this.step = 2;
                if (['timeline'].includes(firstField)) this.step = 3;
                if (['name', 'email'].includes(firstField)) this.step = 4;
                if (['company', 'phone'].includes(firstField)) this.step = 5;
                if (['message'].includes(firstField)) this.step = 6;
            },

            async submit(formElement) {
                this.errorMessage = '';
                this.serverErrors = {};
                this.syncReferrers(formElement);

                if (!this.validateBeforeSubmit()) {
                    return;
                }

                this.submitting = true;

                try {
                    const response = await fetch(formElement.action || window.location.pathname, {
                        method: 'POST',
                        headers: {
                            Accept: 'application/json',
                            'X-Requested-With': 'XMLHttpRequest',
                        },
                        credentials: 'same-origin',
                        body: new FormData(formElement),
                    });
                    const payload = await response.json();

                    if (!response.ok || !payload.ok) {
                        this.errorMessage = payload.message || 'Please review the highlighted fields and try again.';
                        this.applyServerErrors(payload.errors || {});
                        return;
                    }

                    this.form = {
                        inquiry_type: 'project',
                        service_interest: '',
                        budget: '',
                        timeline: '',
                        name: '',
                        email: '',
                        company: '',
                        phone: '',
                        message: '',
                    };
                    formElement.reset();
                    this.step = 1;
                    this.successMessage = payload.message || this.successMessage;
                    this.successSteps = payload.next_steps || this.successSteps;
                    this.successOpen = true;
                } catch (error) {
                    this.errorMessage = 'Something went wrong while sending your enquiry. Please try again or email the studio directly.';
                } finally {
                    this.submitting = false;
                }
            },
        };
    };

    window.addEventListener('DOMContentLoaded', () => {
        initThemeToggle();
        initAnimatedBackground();
        initFlashMessages();
        syncReferrerFields();
        initPointerGlow();
        initMediaCarousels();
        initReveals();
    });
}());


============================================================
FILE: templates/404.html
============================================================
{% extends 'base.html' %}

{% block content %}
<section class="mx-auto max-w-5xl px-6 py-24 lg:px-8 lg:py-32">
    <div class="grid gap-8 lg:grid-cols-[0.9fr_1.1fr] lg:items-center">
        <div class="mx-auto max-w-lg rounded-[2rem] border border-white/10 bg-slate-950/60 p-10 shadow-glow backdrop-blur-xl lg:mx-0">
            <p class="eyebrow">404</p>
            <h1 class="mt-4 font-display text-4xl font-bold tracking-tight text-white sm:text-5xl">That page does not exist.</h1>
            <p class="mt-6 text-lg leading-8 text-slate-300">The page may have moved, or the link may be incorrect. Use the options below to get back on track.</p>
            <div class="mt-8 flex flex-wrap gap-4">
                <a href="{% url 'core:home' %}" class="button-primary">Go home</a>
                <a href="{% url 'leads:contact' %}" class="button-secondary">Contact the studio</a>
            </div>
        </div>
        <div class="surface-card">
            {% include 'includes/service_graphic.html' with variant='product' %}
        </div>
    </div>
</section>
{% endblock %}


============================================================
FILE: templates/base.html
============================================================
{% load static %}
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% if page_title %}{{ page_title }} · {% endif %}{{ site_name }}</title>
    <meta name="description" content="{{ meta_description|default:'Premium software, AI, websites, and automation for ambitious teams.' }}">
    <meta name="theme-color" content="#08111f">
    {% if site_url %}
    <link rel="canonical" href="{{ site_url }}{{ request.path }}">
    {% endif %}
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="{{ site_name }}">
    <meta property="og:title" content="{{ og_title|default:page_title|default:site_name }}">
    <meta property="og:description" content="{{ og_description|default:meta_description }}">
    {% if site_url %}
    <meta property="og:url" content="{{ site_url }}{{ request.path }}">
    <meta property="og:image" content="{{ site_url }}{{ og_image_path|default:default_og_path }}">
    {% endif %}
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{{ og_title|default:page_title|default:site_name }}">
    <meta name="twitter:description" content="{{ og_description|default:meta_description }}">
    {% if site_url %}
    <meta name="twitter:image" content="{{ site_url }}{{ og_image_path|default:default_og_path }}">
    {% endif %}
    <link rel="icon" type="image/svg+xml" href="{% static 'svg/favicon.svg' %}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
    <script>
        (function () {
            try {
                var stored = localStorage.getItem('axial-theme');
                var prefersLight = window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches;
                var theme = stored || (prefersLight ? 'light' : 'dark');
                document.documentElement.setAttribute('data-theme', theme);
                var meta = document.querySelector('meta[name="theme-color"]');
                if (meta) {
                    meta.setAttribute('content', theme === 'light' ? '#f6f9fd' : '#08111f');
                }
            } catch (error) {
                document.documentElement.setAttribute('data-theme', 'dark');
            }
        }());
    </script>
    <script src="https://cdn.tailwindcss.com?plugins=forms,typography"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
                        display: ['Space Grotesk', 'Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
                    },
                    colors: {
                        brand: {
                            50: '#eef7ff',
                            100: '#d9ebff',
                            200: '#b9dbff',
                            300: '#85c0ff',
                            400: '#4799ff',
                            500: '#1870f8',
                            600: '#0e57d4',
                            700: '#1147ab',
                            800: '#153c87',
                            900: '#172f68',
                        },
                        accent: {
                            300: '#87f0d4',
                            400: '#4ee7c2',
                            500: '#10c79e',
                        },
                        ink: '#08111f',
                        steel: '#0f172a',
                        mist: '#dce6f3',
                    },
                    boxShadow: {
                        glow: '0 0 0 1px rgba(71, 153, 255, 0.12), 0 24px 70px rgba(7, 17, 31, 0.35)',
                    },
                    backgroundImage: {
                        'hero-radial': 'radial-gradient(circle at top right, rgba(71,153,255,0.25), transparent 30%), radial-gradient(circle at bottom left, rgba(78,231,194,0.16), transparent 26%)',
                    },
                },
            },
        }
    </script>
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <link rel="stylesheet" href="{% static 'css/theme.css' %}">
</head>
<body class="bg-ink text-slate-100 antialiased selection:bg-brand-400/30 selection:text-white">
    <canvas class="site-canvas" data-animated-bg aria-hidden="true"></canvas>
    <div class="site-grid"></div>
    <div class="ambient-orb ambient-orb--one"></div>
    <div class="ambient-orb ambient-orb--two"></div>
    <div class="ambient-beam"></div>
    {% include 'includes/header.html' %}

    {% if messages %}
    <div class="relative z-40 mx-auto max-w-7xl px-6 pt-6">
        {% for message in messages %}
            <div data-flash class="mb-3 flex items-start gap-3 rounded-2xl border border-white/10 bg-slate-900/[0.85] px-4 py-4 shadow-glow backdrop-blur-sm">
                <div class="mt-1 h-2.5 w-2.5 rounded-full {% if message.tags == 'success' %}bg-accent-400{% elif message.tags == 'error' %}bg-rose-400{% else %}bg-brand-400{% endif %}"></div>
                <p class="text-sm text-slate-200">{{ message }}</p>
            </div>
        {% endfor %}
    </div>
    {% endif %}

    <main>
        {% block content %}{% endblock %}
    </main>

    {% include 'includes/footer.html' %}
    <script src="{% static 'js/main.js' %}"></script>
</body>
</html>


============================================================
FILE: templates/core/about.html
============================================================
{% extends 'base.html' %}

{% block content %}
{% include 'includes/page_header.html' with kicker='About the Studio' title='A founder-led studio built to turn technical depth into practical delivery.' intro='Axial Foundry exists for companies that need a capable partner to scope and ship software, AI features, digital platforms, and operational systems without unnecessary complexity.' supporting_copy='The studio is not built around hype, inflated claims, or one narrow service line. It is built around solving the right problem well.' visual='about' image='img/code-laptop.jpg' image_alt='Programming interface' %}

<section class="section-shell">
    <div class="mx-auto grid max-w-7xl gap-12 px-6 lg:grid-cols-[1fr_.95fr] lg:px-8 lg:items-start">
        <div>
            <p class="eyebrow">Studio point of view</p>
            <h2 class="section-title">{{ brand_story }}</h2>
            <p class="mt-5 max-w-2xl text-base leading-8 text-slate-400">{{ positioning_statement }}</p>
        </div>
        <div class="surface-card pointer-glow" data-reveal>
            <div class="grid gap-5 lg:grid-cols-[1fr_170px] lg:items-center">
                <div>
                    <h3 class="font-display text-2xl font-semibold text-white">What the studio builds</h3>
                    <ul class="mt-5 space-y-3 text-sm leading-7 text-slate-300">
                        <li>Premium business websites and landing pages</li>
                        <li>Custom web applications, portals, dashboards, and internal tools</li>
                        <li>Backend systems, APIs, and workflow automations</li>
                        <li>AI assistants, RAG experiences, prompt systems, and evaluation layers</li>
                        <li>Speech-enabled workflows and language-aware product capabilities</li>
                    </ul>
                </div>
                <div class="hidden lg:block">
                    {% include 'includes/service_graphic.html' with variant='product' %}
                </div>
            </div>
        </div>
    </div>
</section>

<section class="section-shell section-divider">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="max-w-3xl">
            <p class="eyebrow">How the studio works</p>
            <h2 class="section-title">A delivery model designed for clarity, quality, and maintainability.</h2>
        </div>
        <div class="mt-10 grid gap-5 md:grid-cols-2 xl:grid-cols-4">
            {% for item in about_principles %}
            <article class="surface-card h-full pointer-glow" data-reveal>
                <h3 class="font-display text-xl font-semibold text-white">{{ item.title }}</h3>
                <p class="mt-4 text-sm leading-7 text-slate-400">{{ item.body }}</p>
            </article>
            {% endfor %}
        </div>
    </div>
</section>

<section class="section-shell section-divider">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="max-w-3xl">
            <p class="eyebrow">Capabilities</p>
            <h2 class="section-title">Software, AI, product, and data strengths that work together.</h2>
        </div>
        <div class="mt-10 grid gap-5 md:grid-cols-2 xl:grid-cols-4">
            {% for group in capability_groups %}
            <article class="surface-card h-full pointer-glow" data-reveal>
                <h3 class="font-display text-xl font-semibold text-white">{{ group.title }}</h3>
                <div class="mt-5 flex flex-wrap gap-2">
                    {% for item in group.items %}
                    <span class="rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs text-slate-300">{{ item }}</span>
                    {% endfor %}
                </div>
            </article>
            {% endfor %}
        </div>
    </div>
</section>

<section class="section-shell section-divider">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="max-w-3xl">
            <p class="eyebrow">Meet the team</p>
            <h2 class="section-title">Structured placeholders for future team profiles.</h2>
            <p class="section-intro">These cards are intentionally built with fixed image ratios and stable spacing so you can replace placeholder imagery with real team photos later without disturbing the visual flow.</p>
        </div>
        <div class="mt-10 grid gap-6 md:grid-cols-2 xl:grid-cols-3">
            <article class="surface-card team-card pointer-glow" data-reveal>
                <div class="team-card__media">
                    <img src="https://images.unsplash.com/photo-1758873268745-dd2cf0d677b5?auto=format&fit=crop&fm=jpg&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&ixlib=rb-4.1.0&q=60&w=3000" alt="Placeholder collaborative team lead image" class="team-card__image">
                    <span class="team-card__badge">Replace image later</span>
                </div>
                <div class="mt-5">
                    <p class="eyebrow eyebrow--compact">Team lead placeholder</p>
                    <h3 class="mt-3 font-display text-2xl font-semibold text-white">Product and Delivery Lead</h3>
                    <p class="mt-4 text-sm leading-7 text-slate-400">Use this area for a short introduction covering delivery ownership, client communication, and cross-functional coordination.</p>
                </div>
            </article>
            <article class="surface-card team-card pointer-glow" data-reveal>
                <div class="team-card__media">
                    <img src="https://images.unsplash.com/photo-1758873269035-aae0e1fd3422?auto=format&fit=crop&fm=jpg&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&ixlib=rb-4.1.0&q=60&w=3000" alt="Placeholder planning and workshop image" class="team-card__image">
                    <span class="team-card__badge">Replace image later</span>
                </div>
                <div class="mt-5">
                    <p class="eyebrow eyebrow--compact">Team lead placeholder</p>
                    <h3 class="mt-3 font-display text-2xl font-semibold text-white">Engineering and Systems Lead</h3>
                    <p class="mt-4 text-sm leading-7 text-slate-400">Use this block for backend, architecture, product engineering, or platform delivery leadership depending on the final team structure.</p>
                </div>
            </article>
            <article class="surface-card team-card pointer-glow" data-reveal>
                <div class="team-card__media">
                    <img src="https://images.unsplash.com/photo-1758518727401-53823b36c47b?auto=format&fit=crop&fm=jpg&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&ixlib=rb-4.1.0&q=60&w=3000" alt="Placeholder professional team profile image" class="team-card__image">
                    <span class="team-card__badge">Replace image later</span>
                </div>
                <div class="mt-5">
                    <p class="eyebrow eyebrow--compact">Team lead placeholder</p>
                    <h3 class="mt-3 font-display text-2xl font-semibold text-white">AI and Research Systems Lead</h3>
                    <p class="mt-4 text-sm leading-7 text-slate-400">Use this card for a concise introduction covering AI implementation, model evaluation, experimentation, or technical advisory responsibility.</p>
                </div>
            </article>
        </div>
    </div>
</section>

<section class="section-shell section-divider">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="max-w-3xl">
            <p class="eyebrow">What clients can expect</p>
            <h2 class="section-title">A structured path from scope to launch.</h2>
        </div>
        <div class="mt-10 grid gap-5 lg:grid-cols-2 xl:grid-cols-3">
            {% for item in process_steps %}
            <article class="surface-card h-full pointer-glow" data-reveal>
                <span class="text-sm font-semibold tracking-[0.28em] text-brand-300">{{ item.step }}</span>
                <h3 class="mt-4 font-display text-2xl font-semibold text-white">{{ item.title }}</h3>
                <p class="mt-4 text-sm leading-7 text-slate-400">{{ item.body }}</p>
            </article>
            {% endfor %}
        </div>
    </div>
</section>

<section class="section-shell section-divider">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        {% include 'includes/owner_section.html' %}
    </div>
</section>

<section class="mx-auto max-w-7xl px-6 py-10 lg:px-8 lg:py-16">
    {% include 'includes/cta_band.html' %}
</section>
{% endblock %}


============================================================
FILE: templates/core/home.html
============================================================
{% extends 'base.html' %}

{% block content %}
<section class="relative overflow-hidden border-b border-white/[0.08] hero-home-shell">
    <div class="absolute inset-0 bg-hero-radial opacity-90"></div>
    <div class="mx-auto grid max-w-7xl gap-14 px-6 py-20 lg:grid-cols-[0.88fr_1.12fr] lg:items-center lg:px-8 lg:py-28">
        <div class="relative z-10 max-w-2xl">
            <p class="eyebrow">Premium software and AI studio</p>
            <h1 class="mt-5 max-w-3xl font-display text-5xl font-bold tracking-tight text-white sm:text-6xl">
                Software, AI, and digital systems <span class="gradient-text">built for teams that need execution.</span>
            </h1>
            <p class="mt-6 max-w-2xl text-lg leading-8 text-slate-300">
                Axial Foundry helps startups, SMEs, agencies, and enterprise teams ship premium websites, custom software, automation, internal tools, and applied AI systems.
            </p>
            <div class="mt-7 grid gap-3 sm:grid-cols-3">
                <div class="hero-benefit">Websites that sell clearly</div>
                <div class="hero-benefit">Apps and portals that fit operations</div>
                <div class="hero-benefit">AI and automation with real utility</div>
            </div>
            <div class="mt-8 flex flex-wrap gap-4">
                <a href="{% url 'leads:contact' %}#contact-experience" class="button-primary">Start a project</a>
                <a href="{% url 'core:services' %}" class="button-secondary">Explore services</a>
            </div>
            <div class="mt-10 flex flex-wrap gap-3 text-sm text-slate-300">
                <a href="mailto:{{ contact_email }}" class="pill-link">{{ contact_email }}</a>
                <a href="tel:{{ contact_phone }}" class="pill-link">{{ contact_phone }}</a>
                <span class="pill-link">{{ contact_location }}</span>
            </div>
        </div>
        <div class="relative z-10">
            {% include 'includes/hero_visual.html' %}
        </div>
    </div>
</section>

<section class="section-shell">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="max-w-3xl">
            <p class="eyebrow">Authority and credibility</p>
            <h2 class="section-title">Research-backed capability, production-focused delivery.</h2>
            <p class="section-intro">The studio pairs business-friendly product thinking with real depth in AI systems, Python engineering, and technical implementation.</p>
        </div>
        <div class="mt-10 grid gap-5 md:grid-cols-2 xl:grid-cols-4">
            {% for item in authority_points %}
            <article class="surface-card authority-card pointer-glow h-full" data-reveal>
                <div class="authority-card__header">
                    <div class="authority-card__number">0{{ forloop.counter }}</div>
                    <div class="authority-card__line"></div>
                </div>
                <h3 class="mt-6 font-display text-xl font-semibold text-white">{{ item.title }}</h3>
                <p class="mt-4 text-sm leading-7 text-slate-400">{{ item.body }}</p>
            </article>
            {% endfor %}
        </div>
    </div>
</section>

<section class="section-shell section-divider">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="flex flex-col gap-6 lg:flex-row lg:items-end lg:justify-between">
            <div class="max-w-3xl">
                <p class="eyebrow">What the studio builds</p>
                <h2 class="section-title">A broader studio offering than a typical AI shop.</h2>
                <p class="section-intro">Some clients need advanced AI. Others need a premium website, a custom portal, a backend system, or a faster internal workflow. Axial Foundry handles both.</p>
            </div>
            <a href="{% url 'core:services' %}" class="button-secondary self-start lg:self-auto">See all services</a>
        </div>
        <div class="mt-10 grid gap-5 xl:grid-cols-2">
            {% for cluster in service_clusters %}
            <article class="surface-card h-full pointer-glow cluster-card" data-reveal>
                <div class="grid gap-5 lg:grid-cols-[1fr_190px] lg:items-center">
                    <div>
                        <p class="text-xs uppercase tracking-[0.22em] text-brand-300">{{ forloop.counter|stringformat:'02d' }}</p>
                        <h3 class="mt-3 font-display text-2xl font-semibold text-white">{{ cluster.title }}</h3>
                        <p class="mt-4 text-sm leading-7 text-slate-400">{{ cluster.summary }}</p>
                        <div class="mt-6 flex flex-wrap gap-2">
                            {% for item in cluster.items %}
                            <span class="rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs text-slate-300">{{ item }}</span>
                            {% endfor %}
                        </div>
                    </div>
                    <div class="hidden lg:block">
                        {% if forloop.counter == 1 %}
                            {% include 'includes/service_graphic.html' with variant='chatbot' %}
                        {% elif forloop.counter == 2 %}
                            {% include 'includes/service_graphic.html' with variant='portal' %}
                        {% elif forloop.counter == 3 %}
                            {% include 'includes/service_graphic.html' with variant='website' %}
                        {% else %}
                            {% include 'includes/service_graphic.html' with variant='automation' %}
                        {% endif %}
                    </div>
                </div>
            </article>
            {% endfor %}
        </div>
    </div>
</section>

<section class="section-shell section-divider">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="max-w-3xl">
            <p class="eyebrow">Why choose this studio</p>
            <h2 class="section-title">Custom delivery with the feel of a serious product partner.</h2>
        </div>
        <div class="mt-10 grid gap-5 md:grid-cols-2 xl:grid-cols-3">
            {% for item in why_choose %}
            <article class="surface-card h-full pointer-glow" data-reveal>
                <h3 class="font-display text-xl font-semibold text-white">{{ item.title }}</h3>
                <p class="mt-4 text-sm leading-7 text-slate-400">{{ item.body }}</p>
            </article>
            {% endfor %}
        </div>
    </div>
</section>

<section class="section-shell section-divider">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="max-w-3xl">
            <p class="eyebrow">Featured solutions and use cases</p>
            <h2 class="section-title">Concrete solution types buyers can immediately relate to.</h2>
        </div>
        <div class="mt-10 grid gap-5 md:grid-cols-2 xl:grid-cols-4">
            {% for item in featured_solutions %}
            <article class="surface-card h-full solution-card pointer-glow" data-reveal>
                <div class="solution-card__graphic">
                    {% if forloop.counter == 1 %}
                        {% include 'includes/service_graphic.html' with variant='chatbot' compact=True %}
                    {% elif forloop.counter == 2 %}
                        {% include 'includes/service_graphic.html' with variant='knowledge' compact=True %}
                    {% elif forloop.counter == 3 %}
                        {% include 'includes/service_graphic.html' with variant='automation' compact=True %}
                    {% elif forloop.counter == 4 %}
                        {% include 'includes/service_graphic.html' with variant='dashboard' compact=True %}
                    {% elif forloop.counter == 5 %}
                        {% include 'includes/service_graphic.html' with variant='website' compact=True %}
                    {% elif forloop.counter == 6 %}
                        {% include 'includes/service_graphic.html' with variant='automation' compact=True %}
                    {% elif forloop.counter == 7 %}
                        {% include 'includes/service_graphic.html' with variant='portal' compact=True %}
                    {% else %}
                        {% include 'includes/service_graphic.html' with variant='speech' compact=True %}
                    {% endif %}
                </div>
                <h3 class="mt-5 font-display text-xl font-semibold text-white">{{ item.title }}</h3>
                <p class="mt-4 text-sm leading-7 text-slate-400">{{ item.body }}</p>
                <div class="mt-6 flex flex-wrap gap-2">
                    {% for tag in item.tags %}
                    <span class="rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs text-slate-300">{{ tag }}</span>
                    {% endfor %}
                </div>
            </article>
            {% endfor %}
        </div>
    </div>
</section>

<section class="section-shell section-divider">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="max-w-3xl">
            <p class="eyebrow">What clients can expect</p>
            <h2 class="section-title">A professional delivery model from scope to launch.</h2>
        </div>
        <div class="mt-10 grid gap-5 lg:grid-cols-2 xl:grid-cols-3">
            {% for item in process_steps %}
            <article class="surface-card h-full pointer-glow" data-reveal>
                <span class="text-sm font-semibold tracking-[0.28em] text-brand-300">{{ item.step }}</span>
                <h3 class="mt-4 font-display text-2xl font-semibold text-white">{{ item.title }}</h3>
                <p class="mt-4 text-sm leading-7 text-slate-400">{{ item.body }}</p>
            </article>
            {% endfor %}
        </div>
    </div>
</section>

<section class="section-shell section-divider">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="grid gap-8 lg:grid-cols-[1fr_1.05fr] lg:items-start">
            <div>
                <p class="eyebrow">Studio overview</p>
                <h2 class="section-title">{{ brand_story }}</h2>
                <p class="mt-5 max-w-2xl text-base leading-8 text-slate-400">{{ positioning_statement }}</p>
                <div class="mt-8 grid gap-4 sm:grid-cols-2">
                    <div class="overview-stat">
                        <span class="overview-stat__kicker">Delivery model</span>
                        <span class="overview-stat__value">Strategy to launch</span>
                    </div>
                    <div class="overview-stat">
                        <span class="overview-stat__kicker">Capability mix</span>
                        <span class="overview-stat__value">Software + AI + automation</span>
                    </div>
                    <div class="overview-stat">
                        <span class="overview-stat__kicker">Working style</span>
                        <span class="overview-stat__value">Founder-led and hands-on</span>
                    </div>
                    <div class="overview-stat">
                        <span class="overview-stat__kicker">Client fit</span>
                        <span class="overview-stat__value">International and product-minded</span>
                    </div>
                </div>
            </div>
            <div class="overview-board surface-card pointer-glow" data-reveal>
                <div class="overview-board__hero">
                    <img src="https://images.unsplash.com/photo-1758873268745-dd2cf0d677b5?auto=format&fit=crop&fm=jpg&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&ixlib=rb-4.1.0&q=60&w=3000" alt="Collaborative software team" class="overview-board__image">
                    <div class="overview-board__shade"></div>
                    <div class="overview-board__copy">
                        <p class="overview-board__eyebrow">Actual product partner energy</p>
                        <h3 class="overview-board__title">The studio is designed to feel like an extension of the client team.</h3>
                    </div>
                </div>
                <div class="overview-board__grid">
                    <div class="overview-mini-card">
                        <span class="overview-mini-card__title">Premium websites</span>
                        <span class="overview-mini-card__text">Positioning and conversion that look credible internationally.</span>
                    </div>
                    <div class="overview-mini-card">
                        <span class="overview-mini-card__title">Custom systems</span>
                        <span class="overview-mini-card__text">Apps, portals, and internal tools shaped around operations.</span>
                    </div>
                    <div class="overview-mini-card">
                        <span class="overview-mini-card__title">Applied AI</span>
                        <span class="overview-mini-card__text">Assistants, retrieval, and workflow intelligence where it makes sense.</span>
                    </div>
                    <div class="overview-mini-card">
                        <span class="overview-mini-card__title">Automation</span>
                        <span class="overview-mini-card__text">Integrations and backend systems that save time and reduce friction.</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="section-shell section-divider">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="flex flex-col gap-6 lg:flex-row lg:items-end lg:justify-between">
            <div class="max-w-3xl">
                <p class="eyebrow">Featured work</p>
                <h2 class="section-title">Anonymized case studies that show technical breadth.</h2>
                <p class="section-intro">Grounded examples across AI systems, software platforms, backend and data systems, and business workflow delivery.</p>
            </div>
            <a href="{% url 'core:work' %}" class="button-secondary self-start lg:self-auto">View all case studies</a>
        </div>
        <div class="mt-10 grid gap-5 xl:grid-cols-2">
            {% for case in featured_work %}
            <article class="surface-card h-full pointer-glow" data-reveal>
                <div class="grid gap-5 lg:grid-cols-[1fr_180px] lg:items-center">
                    <div>
                        <p class="text-xs uppercase tracking-[0.22em] text-brand-300">{{ case.category }}</p>
                        <h3 class="mt-3 font-display text-2xl font-semibold text-white">{{ case.title }}</h3>
                        <p class="mt-4 text-sm leading-7 text-slate-400">{{ case.summary }}</p>
                    </div>
                    <div class="hidden lg:block">
                        {% if forloop.counter == 1 %}
                            {% include 'includes/service_graphic.html' with variant='knowledge' %}
                        {% elif forloop.counter == 2 %}
                            {% include 'includes/service_graphic.html' with variant='chatbot' %}
                        {% elif forloop.counter == 3 %}
                            {% include 'includes/service_graphic.html' with variant='speech' %}
                        {% else %}
                            {% include 'includes/service_graphic.html' with variant='llm' %}
                        {% endif %}
                    </div>
                </div>
                <div class="mt-6 flex flex-wrap gap-2">
                    {% for cap in case.capabilities %}
                    <span class="rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs text-slate-300">{{ cap }}</span>
                    {% endfor %}
                </div>
            </article>
            {% endfor %}
        </div>
    </div>
</section>

<section class="section-shell section-divider">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        {% include 'includes/owner_section.html' %}
    </div>
</section>

<section class="section-shell section-divider">
    <div class="mx-auto max-w-5xl px-6 lg:px-8">
        <div class="max-w-3xl">
            <p class="eyebrow">FAQ</p>
            <h2 class="section-title">Common questions from prospective clients.</h2>
        </div>
        <div class="mt-10 space-y-4">
            {% for item in faqs %}
                {% include 'includes/faq_item.html' %}
            {% endfor %}
        </div>
    </div>
</section>

<section class="mx-auto max-w-7xl px-6 py-10 lg:px-8 lg:py-16">
    {% include 'includes/cta_band.html' %}
</section>
{% endblock %}


============================================================
FILE: templates/core/insights.html
============================================================
{% extends 'base.html' %}

{% block content %}
{% include 'includes/page_header.html' with kicker='Insights and research' title='Technical credibility that supports better delivery decisions.' intro='Research and deep technical work inform how Axial Foundry thinks about AI quality, implementation trade-offs, speech systems, and product architecture — but the studio stays focused on practical application.' supporting_copy='This page is intentionally secondary to the studio’s services. It exists to show depth without turning the website into an academic profile.' visual='insights' image='img/blue-beams.jpg' image_alt='Abstract blue light beams' %}

<section class="section-shell">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="max-w-3xl">
            <p class="eyebrow">Selected publication highlights</p>
            <h2 class="section-title">Research grounding that strengthens implementation quality.</h2>
        </div>
        <div class="mt-10 grid gap-5 md:grid-cols-3">
            {% for item in publication_highlights %}
            <article class="surface-card h-full">
                <p class="text-xs uppercase tracking-[0.22em] text-brand-300">{{ item.venue }}</p>
                <h3 class="mt-3 font-display text-2xl font-semibold text-white">{{ item.title }}</h3>
                <p class="mt-4 text-sm leading-7 text-slate-400">{{ item.body }}</p>
            </article>
            {% endfor %}
        </div>
    </div>
</section>

<section class="section-shell section-divider">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="max-w-3xl">
            <p class="eyebrow">Practical thought leadership</p>
            <h2 class="section-title">Topics the studio thinks about when shaping high-quality delivery.</h2>
        </div>
        <div class="mt-10 grid gap-5 lg:grid-cols-2 xl:grid-cols-3">
            {% for item in insight_topics %}
            <article class="surface-card h-full">
                <h3 class="font-display text-xl font-semibold text-white">{{ item.title }}</h3>
                <p class="mt-4 text-sm leading-7 text-slate-400">{{ item.body }}</p>
            </article>
            {% endfor %}
        </div>
    </div>
</section>

<section class="section-shell section-divider">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="max-w-3xl">
            <p class="eyebrow">Core expertise areas</p>
            <h2 class="section-title">Where research-grade thinking meets business-ready implementation.</h2>
        </div>
        <div class="mt-10 grid gap-5 md:grid-cols-2 xl:grid-cols-4">
            {% for item in expertise_cards %}
            <article class="surface-card h-full">
                {% if forloop.counter == 1 %}
                    {% include 'includes/service_graphic.html' with variant='llm' compact=True %}
                {% elif forloop.counter == 2 %}
                    {% include 'includes/service_graphic.html' with variant='speech' compact=True %}
                {% elif forloop.counter == 3 %}
                    {% include 'includes/service_graphic.html' with variant='automation' compact=True %}
                {% else %}
                    {% include 'includes/service_graphic.html' with variant='strategy' compact=True %}
                {% endif %}
                <h3 class="mt-5 font-display text-xl font-semibold text-white">{{ item.title }}</h3>
                <p class="mt-4 text-sm leading-7 text-slate-400">{{ item.body }}</p>
            </article>
            {% endfor %}
        </div>
    </div>
</section>

<section class="mx-auto max-w-7xl px-6 py-10 lg:px-8 lg:py-16">
    {% include 'includes/cta_band.html' %}
</section>
{% endblock %}


============================================================
FILE: templates/core/privacy.html
============================================================
{% extends 'base.html' %}

{% block content %}
{% include 'includes/page_header.html' with kicker='Privacy policy' title='Privacy information for website visitors and contact enquiries.' intro='This policy explains how Axial Foundry handles information submitted through this website and how that information is used to respond to business enquiries.' visual='privacy' %}

<section class="section-shell">
    <div class="mx-auto max-w-4xl px-6 lg:px-8">
        <div class="surface-card prose prose-invert max-w-none prose-p:text-slate-300 prose-li:text-slate-300 prose-strong:text-white prose-headings:font-display prose-headings:text-white">
            <h2>Information collected</h2>
            <p>Axial Foundry may collect personal and business contact information submitted through the contact form, including your name, email address, phone number, company name, project details, budget range, and timeline information.</p>

            <h2>How information is used</h2>
            <p>Submitted information is used to review enquiries, respond to project requests, evaluate service fit, and continue relevant business communication. Information is not sold to third parties.</p>

            <h2>Lead handling and storage</h2>
            <p>Contact submissions are stored in the site database for follow-up and business recordkeeping. Anti-spam and lightweight security measures may record technical details such as IP address, user agent, and referral source when a form is submitted.</p>

            <h2>Email communication</h2>
            <p>If email delivery is configured, submitted enquiries may trigger an internal notification so the studio can respond efficiently. Replying to an enquiry may continue the conversation over email or phone using the contact details you provided.</p>

            <h2>Cookies and analytics</h2>
            <p>This website is designed to operate with minimal complexity. If analytics or additional tracking tools are added in the future, this policy should be updated to reflect the tools used and the purpose they serve.</p>

            <h2>Data retention</h2>
            <p>Enquiry data may be retained for business continuity, project history, relationship management, legal compliance, and security review unless deletion is requested and retention is not otherwise required.</p>

            <h2>Your choices</h2>
            <p>You may request access to, correction of, or deletion of the contact information you have submitted, subject to any legal or operational requirements that apply.</p>

            <h2>Contact</h2>
            <p>For privacy-related questions, contact <a href="mailto:{{ contact_email }}">{{ contact_email }}</a> or call <a href="tel:{{ contact_phone }}">{{ contact_phone }}</a>.</p>
        </div>
    </div>
</section>
{% endblock %}


============================================================
FILE: templates/core/services.html
============================================================
{% extends 'base.html' %}

{% block content %}
{% include 'includes/page_header.html' with kicker='Services' title='Software, AI, websites, and operational systems built around real business needs.' intro='Axial Foundry serves companies that need a capable delivery partner — whether the project is a premium website, a product MVP, an internal tool, a workflow automation, or a deeper AI implementation.' supporting_copy='The goal is not to push the most complex stack. The goal is to design and build the right system for the client’s stage, users, and operating reality.' visual='services' image='img/fiber-cables.jpg' image_alt='Fiber optic connections and infrastructure' %}

<section class="section-shell">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="grid gap-5 xl:grid-cols-2">
            {% for cluster in service_clusters %}
            <article class="surface-card h-full pointer-glow" data-reveal>
                <div class="grid gap-5 lg:grid-cols-[1fr_190px] lg:items-center">
                    <div>
                        <h2 class="font-display text-2xl font-semibold text-white">{{ cluster.title }}</h2>
                        <p class="mt-4 text-sm leading-7 text-slate-400">{{ cluster.summary }}</p>
                        <ul class="mt-6 grid gap-3 sm:grid-cols-2">
                            {% for item in cluster.items %}
                            <li class="rounded-2xl border border-white/[0.08] bg-white/5 px-4 py-3 text-sm text-slate-300">{{ item }}</li>
                            {% endfor %}
                        </ul>
                    </div>
                    <div class="hidden lg:block">
                        {% if forloop.counter == 1 %}
                            {% include 'includes/service_graphic.html' with variant='chatbot' %}
                        {% elif forloop.counter == 2 %}
                            {% include 'includes/service_graphic.html' with variant='portal' %}
                        {% elif forloop.counter == 3 %}
                            {% include 'includes/service_graphic.html' with variant='website' %}
                        {% else %}
                            {% include 'includes/service_graphic.html' with variant='automation' %}
                        {% endif %}
                    </div>
                </div>
            </article>
            {% endfor %}
        </div>
    </div>
</section>

<section class="section-shell section-divider">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="max-w-3xl">
            <p class="eyebrow">Service detail</p>
            <h2 class="section-title">What each engagement is, who it helps, and what clients receive.</h2>
        </div>
        <div class="mt-10 space-y-6">
            {% for service in service_details %}
            <article class="surface-card pointer-glow" data-reveal>
                <div class="grid gap-8 xl:grid-cols-[0.9fr_0.78fr_0.6fr] xl:items-start">
                    <div>
                        <p class="text-xs uppercase tracking-[0.22em] text-brand-300">{{ service.group }}</p>
                        <h3 class="mt-3 font-display text-2xl font-semibold text-white">{{ service.title }}</h3>
                        <p class="mt-4 text-sm leading-7 text-slate-400"><span class="font-semibold text-slate-200">What it is:</span> {{ service.what_it_is }}</p>
                        <p class="mt-4 text-sm leading-7 text-slate-400"><span class="font-semibold text-slate-200">Who it is for:</span> {{ service.who_it_is_for }}</p>
                    </div>
                    <div class="grid gap-6 md:grid-cols-2 xl:grid-cols-1">
                        <div>
                            <h4 class="font-display text-lg font-semibold text-white">Problems it solves</h4>
                            <ul class="mt-4 space-y-3 text-sm leading-7 text-slate-400">
                                {% for item in service.problems_it_solves %}
                                <li class="flex gap-3"><span class="mt-2 h-2 w-2 rounded-full bg-brand-400"></span><span>{{ item }}</span></li>
                                {% endfor %}
                            </ul>
                        </div>
                        <div>
                            <h4 class="font-display text-lg font-semibold text-white">What the client receives</h4>
                            <ul class="mt-4 space-y-3 text-sm leading-7 text-slate-400">
                                {% for item in service.client_receives %}
                                <li class="flex gap-3"><span class="mt-2 h-2 w-2 rounded-full bg-accent-400"></span><span>{{ item }}</span></li>
                                {% endfor %}
                            </ul>
                        </div>
                    </div>
                    <div class="grid gap-5">
                        <div class="surface-card h-full bg-white/5 pointer-glow">
                            {% if service.title == 'AI Strategy and Implementation' %}
                                {% include 'includes/service_graphic.html' with variant='strategy' %}
                            {% elif service.title == 'AI Assistants and Chatbots' %}
                                {% include 'includes/service_graphic.html' with variant='chatbot' %}
                            {% elif service.title == 'RAG and Knowledge Assistants' %}
                                {% include 'includes/service_graphic.html' with variant='knowledge' %}
                            {% elif service.title == 'LLM Fine-tuning and Evaluation' %}
                                {% include 'includes/service_graphic.html' with variant='llm' %}
                            {% elif service.title == 'Speech AI Systems' %}
                                {% include 'includes/service_graphic.html' with variant='speech' %}
                            {% elif service.title == 'Custom Web Applications' %}
                                {% include 'includes/service_graphic.html' with variant='webapp' %}
                            {% elif service.title == 'Product and MVP Build' %}
                                {% include 'includes/service_graphic.html' with variant='product' %}
                            {% elif service.title == 'Premium Website Development' %}
                                {% include 'includes/service_graphic.html' with variant='website' %}
                            {% else %}
                                {% include 'includes/service_graphic.html' with variant='automation' %}
                            {% endif %}
                        </div>
                    </div>
                </div>
                <div class="mt-8 rounded-2xl border border-white/[0.08] bg-white/5 px-5 py-4 text-sm leading-7 text-slate-300">
                    <span class="font-semibold text-white">Typical engagement includes:</span> {{ service.typical_engagement }}
                </div>
            </article>
            {% endfor %}
        </div>
    </div>
</section>

<section class="mx-auto max-w-7xl px-6 py-10 lg:px-8 lg:py-16">
    {% include 'includes/cta_band.html' %}
</section>
{% endblock %}


============================================================
FILE: templates/core/solutions.html
============================================================
{% extends 'base.html' %}

{% block content %}
{% include 'includes/page_header.html' with kicker='Solutions and industries' title='Solutions shaped around business needs, team types, and delivery reality.' intro='Axial Foundry works with startups, SMEs, agencies, enterprise teams, service businesses, and knowledge-heavy organizations that need software, automation, websites, or AI capabilities that actually fit how they work.' supporting_copy='The same studio can support a sharp business website, a custom internal system, a portal, an AI assistant, or a broader product build depending on what the situation calls for.' visual='solutions' image='img/hero-network.jpg' image_alt='Connected city network' %}

<section class="section-shell">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="grid gap-5 md:grid-cols-2 xl:grid-cols-3">
            {% for item in audience_solutions %}
            <article class="surface-card h-full">
                <div class="solution-card__graphic">
                    {% if forloop.counter == 1 %}
                        {% include 'includes/service_graphic.html' with variant='product' compact=True %}
                    {% elif forloop.counter == 2 %}
                        {% include 'includes/service_graphic.html' with variant='website' compact=True %}
                    {% elif forloop.counter == 3 %}
                        {% include 'includes/service_graphic.html' with variant='portal' compact=True %}
                    {% elif forloop.counter == 4 %}
                        {% include 'includes/service_graphic.html' with variant='automation' compact=True %}
                    {% elif forloop.counter == 5 %}
                        {% include 'includes/service_graphic.html' with variant='knowledge' compact=True %}
                    {% else %}
                        {% include 'includes/service_graphic.html' with variant='dashboard' compact=True %}
                    {% endif %}
                </div>
                <h2 class="mt-5 font-display text-2xl font-semibold text-white">{{ item.title }}</h2>
                <p class="mt-4 text-sm leading-7 text-slate-400">{{ item.summary }}</p>
                <ul class="mt-6 space-y-3 text-sm text-slate-300">
                    {% for need in item.needs %}
                    <li class="flex gap-3"><span class="mt-2 h-2 w-2 rounded-full bg-brand-400"></span><span>{{ need }}</span></li>
                    {% endfor %}
                </ul>
            </article>
            {% endfor %}
        </div>
    </div>
</section>

<section class="section-shell section-divider">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="max-w-3xl">
            <p class="eyebrow">Business needs map</p>
            <h2 class="section-title">How the studio maps capabilities to real operating problems.</h2>
        </div>
        <div class="mt-10 grid gap-5 lg:grid-cols-2 xl:grid-cols-3">
            {% for item in need_map %}
            <article class="surface-card h-full">
                <h3 class="font-display text-xl font-semibold text-white">{{ item.title }}</h3>
                <p class="mt-4 text-sm leading-7 text-slate-400">{{ item.body }}</p>
            </article>
            {% endfor %}
        </div>
    </div>
</section>

<section class="section-shell section-divider">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="max-w-3xl">
            <p class="eyebrow">Representative solution types</p>
            <h2 class="section-title">Examples of where the studio can add immediate value.</h2>
        </div>
        <div class="mt-10 grid gap-5 md:grid-cols-2 xl:grid-cols-4">
            {% for item in featured_solutions %}
            <article class="surface-card h-full solution-card">
                <div class="solution-card__graphic">
                    {% if forloop.counter == 1 %}
                        {% include 'includes/service_graphic.html' with variant='chatbot' compact=True %}
                    {% elif forloop.counter == 2 %}
                        {% include 'includes/service_graphic.html' with variant='knowledge' compact=True %}
                    {% elif forloop.counter == 3 %}
                        {% include 'includes/service_graphic.html' with variant='automation' compact=True %}
                    {% elif forloop.counter == 4 %}
                        {% include 'includes/service_graphic.html' with variant='dashboard' compact=True %}
                    {% elif forloop.counter == 5 %}
                        {% include 'includes/service_graphic.html' with variant='website' compact=True %}
                    {% elif forloop.counter == 6 %}
                        {% include 'includes/service_graphic.html' with variant='automation' compact=True %}
                    {% elif forloop.counter == 7 %}
                        {% include 'includes/service_graphic.html' with variant='portal' compact=True %}
                    {% else %}
                        {% include 'includes/service_graphic.html' with variant='speech' compact=True %}
                    {% endif %}
                </div>
                <h3 class="mt-5 font-display text-xl font-semibold text-white">{{ item.title }}</h3>
                <p class="mt-4 text-sm leading-7 text-slate-400">{{ item.body }}</p>
            </article>
            {% endfor %}
        </div>
    </div>
</section>

<section class="mx-auto max-w-7xl px-6 py-10 lg:px-8 lg:py-16">
    {% include 'includes/cta_band.html' %}
</section>
{% endblock %}


============================================================
FILE: templates/core/work.html
============================================================
{% extends 'base.html' %}

{% block content %}
{% include 'includes/page_header.html' with kicker='Work and case studies' title='Representative build themes grounded in real delivery experience.' intro='These case studies are anonymized and intentionally avoid client names, inflated claims, or made-up ROI numbers. They are designed to show breadth across AI systems, software engineering, speech workflows, automation, and data infrastructure.' supporting_copy='The goal is to give prospects a credible view of what the studio can build, while respecting confidential implementation details.' visual='work' image='img/circuit-touch.jpg' image_alt='Interactive circuit interface' %}

<section class="section-shell">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="space-y-6">
            {% for case in case_studies %}
            <article class="surface-card">
                <div class="grid gap-8 xl:grid-cols-[0.8fr_1fr_0.5fr] xl:items-start">
                    <div>
                        <p class="text-xs uppercase tracking-[0.22em] text-brand-300">{{ case.category }}</p>
                        <h2 class="mt-3 font-display text-3xl font-semibold text-white">{{ case.title }}</h2>
                        <p class="mt-4 text-sm leading-7 text-slate-400">{{ case.summary }}</p>
                        <div class="mt-6 flex flex-wrap gap-2">
                            {% for cap in case.capabilities %}
                            <span class="rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs text-slate-300">{{ cap }}</span>
                            {% endfor %}
                        </div>
                    </div>
                    <div class="grid gap-6 md:grid-cols-2">
                        <div>
                            <h3 class="font-display text-lg font-semibold text-white">Challenge</h3>
                            <p class="mt-3 text-sm leading-7 text-slate-400">{{ case.challenge }}</p>
                        </div>
                        <div>
                            <h3 class="font-display text-lg font-semibold text-white">What was built</h3>
                            <p class="mt-3 text-sm leading-7 text-slate-400">{{ case.solution }}</p>
                        </div>
                    </div>
                    <div class="hidden xl:block">
                        {% if forloop.counter == 1 %}
                            {% include 'includes/service_graphic.html' with variant='knowledge' %}
                        {% elif forloop.counter == 2 %}
                            {% include 'includes/service_graphic.html' with variant='chatbot' %}
                        {% elif forloop.counter == 3 %}
                            {% include 'includes/service_graphic.html' with variant='speech' %}
                        {% elif forloop.counter == 4 %}
                            {% include 'includes/service_graphic.html' with variant='llm' %}
                        {% elif forloop.counter == 5 %}
                            {% include 'includes/service_graphic.html' with variant='automation' %}
                        {% else %}
                            {% include 'includes/service_graphic.html' with variant='portal' %}
                        {% endif %}
                    </div>
                </div>
                <div class="mt-8 grid gap-6 lg:grid-cols-[1.1fr_.9fr]">
                    <div>
                        <h3 class="font-display text-lg font-semibold text-white">Typical deliverables</h3>
                        <ul class="mt-4 grid gap-3 sm:grid-cols-2">
                            {% for item in case.deliverables %}
                            <li class="rounded-2xl border border-white/[0.08] bg-white/5 px-4 py-3 text-sm text-slate-300">{{ item }}</li>
                            {% endfor %}
                        </ul>
                    </div>
                    <div class="rounded-2xl border border-brand-400/[0.15] bg-brand-400/10 p-5 text-sm leading-7 text-slate-200">
                        <span class="font-semibold text-white">Scope note:</span> {{ case.note }}
                    </div>
                </div>
            </article>
            {% endfor %}
        </div>
    </div>
</section>

<section class="mx-auto max-w-7xl px-6 py-10 lg:px-8 lg:py-16">
    {% include 'includes/cta_band.html' %}
</section>
{% endblock %}


============================================================
FILE: templates/includes/cta_band.html
============================================================
<section class="relative overflow-hidden rounded-[2rem] border border-white/10 bg-gradient-to-br from-brand-600/20 via-slate-950 to-accent-500/10 px-8 py-12 shadow-glow lg:px-10 lg:py-14">
    <div class="absolute -top-16 right-0 h-44 w-44 rounded-full bg-brand-500/[0.15] blur-3xl"></div>
    <div class="absolute -bottom-12 left-0 h-36 w-36 rounded-full bg-accent-400/[0.15] blur-3xl"></div>
    <div class="relative grid gap-8 lg:grid-cols-[1fr_.9fr] lg:items-center">
        <div class="max-w-3xl">
            <p class="eyebrow">Ready to talk?</p>
            <h2 class="mt-4 font-display text-3xl font-bold tracking-tight text-white sm:text-4xl">Build the right system, not just another idea deck.</h2>
            <p class="mt-5 text-base leading-7 text-slate-300">Whether you need a premium website, an internal tool, a product MVP, a knowledge assistant, or a deeper AI implementation, Axial Foundry can help shape and ship it.</p>
            <div class="mt-8 flex flex-wrap gap-4">
                <a href="{% url 'leads:contact' %}#contact-experience" class="button-primary">Start a project conversation</a>
                <a href="mailto:{{ contact_email }}" class="button-secondary">Email the studio</a>
            </div>
        </div>
        <div class="hidden lg:block">
            <div class="surface-card border-white/10 bg-white/5">
                {% include 'includes/service_graphic.html' with variant='product' %}
            </div>
        </div>
    </div>
</section>


============================================================
FILE: templates/includes/faq_item.html
============================================================
<div x-data="{open:false}" class="rounded-2xl border border-white/10 bg-slate-950/[0.55] p-5 shadow-lg backdrop-blur-sm">
    <button @click="open = !open" class="flex w-full items-start justify-between gap-4 text-left">
        <span class="font-display text-lg font-semibold text-white">{{ item.question }}</span>
        <span class="mt-1 inline-flex h-8 w-8 flex-none items-center justify-center rounded-full border border-white/10 bg-white/5 text-slate-300">
            <svg x-show="!open" xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="M12 5v14m7-7H5" /></svg>
            <svg x-show="open" x-cloak xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="M19 12H5" /></svg>
        </span>
    </button>
    <div x-show="open" x-transition.opacity.duration.200ms x-cloak>
        <p class="mt-4 text-sm leading-7 text-slate-400">{{ item.answer }}</p>
    </div>
</div>


============================================================
FILE: templates/includes/footer.html
============================================================
{% load static %}
<footer class="relative mt-24 border-t border-white/[0.08] bg-slate-950/80">
    <div class="mx-auto grid max-w-7xl gap-10 px-6 py-16 lg:grid-cols-[1.15fr_.75fr_.9fr] lg:px-8">
        <div>
            <div class="flex items-center gap-3">
                <img src="{% static 'svg/logo-mark.svg' %}" alt="{{ site_name }} mark" class="h-11 w-11 rounded-xl">
                <div>
                    <div class="font-display text-xl font-bold text-white">{{ site_name }}</div>
                    <div class="text-sm text-slate-400">Software, AI, and digital systems built to move business forward.</div>
                </div>
            </div>
            <p class="mt-5 max-w-xl text-sm leading-7 text-slate-400">
                Premium websites, custom software, automation, internal tools, knowledge systems, chatbots, speech workflows, and product delivery for teams that want execution.
            </p>
        </div>
        <div>
            <h2 class="text-sm font-semibold uppercase tracking-[0.22em] text-slate-400">Navigate</h2>
            <ul class="footer-nav-list mt-5 space-y-3 text-sm">
                {% for item in site_navigation %}
                    <li><a href="{{ item.url }}" class="footer-nav-link">{{ item.label }}</a></li>
                {% endfor %}
                <li><a href="{% url 'core:privacy' %}" class="footer-nav-link">Privacy Policy</a></li>
            </ul>
        </div>
        <div>
            <h2 class="text-sm font-semibold uppercase tracking-[0.22em] text-slate-400">Contact</h2>
            <div class="mt-5 grid gap-3 text-sm text-slate-300">
                <a href="mailto:{{ contact_email }}" class="footer-nav-link">{{ contact_email }}</a>
                <a href="tel:{{ contact_phone }}" class="footer-nav-link">{{ contact_phone }}</a>
                <p class="text-slate-400">{{ contact_location }}</p>
                <p class="text-slate-500">Working with international clients across startups, SMEs, agencies, and enterprise teams.</p>
            </div>
        </div>
    </div>
    <div class="border-t border-white/[0.08]">
        <div class="mx-auto flex max-w-7xl flex-col gap-3 px-6 py-5 text-xs text-slate-500 lg:flex-row lg:items-center lg:justify-between lg:px-8">
            <p>© {% now 'Y' %} {{ site_name }}. All rights reserved.</p>
            <p>Founder-led in Lahore, Pakistan. Built for international delivery.</p>
        </div>
    </div>
</footer>


============================================================
FILE: templates/includes/header.html
============================================================
{% load static %}
<header x-data="{open:false}" class="sticky top-0 z-50 border-b border-white/[0.08] bg-ink/80 backdrop-blur-xl">
    <div class="mx-auto flex max-w-7xl items-center justify-between gap-4 px-6 py-4 lg:px-8">
        <a href="{% url 'core:home' %}" class="flex items-center gap-3" aria-label="{{ site_name }} home">
            <img src="{% static 'svg/logo-mark.svg' %}" alt="{{ site_name }} logo" class="h-10 w-10 rounded-xl">
            <div>
                <span class="block font-display text-lg font-bold tracking-tight text-white">Axial Foundry</span>
                <span class="block text-[11px] uppercase tracking-[0.24em] text-slate-400">Software · AI · Systems</span>
            </div>
        </a>

        <div class="hidden items-center gap-3 lg:flex">
            <nav class="hidden items-center gap-7 xl:flex">
                {% for item in site_navigation %}
                    <a href="{{ item.url }}" class="text-sm font-medium transition {% if request.path == item.url %}text-white{% else %}text-slate-400 hover:text-white{% endif %}">{{ item.label }}</a>
                {% endfor %}
            </nav>
            {% include 'includes/theme_toggle.html' %}
            <a href="{% url 'leads:contact' %}#contact-experience" class="button-primary text-sm">Start a project</a>
        </div>

        <div class="flex items-center gap-3 lg:hidden">
            {% include 'includes/theme_toggle.html' %}
            <button @click="open = !open" class="nav-utility-button inline-flex h-11 w-11 items-center justify-center" :aria-expanded="open.toString()" aria-controls="mobile-nav" aria-label="Toggle navigation">
                <svg x-show="!open" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="M4 7h16M4 12h16M4 17h16" /></svg>
                <svg x-show="open" x-cloak xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" /></svg>
            </button>
        </div>
    </div>

    <div id="mobile-nav" x-show="open" x-cloak class="border-t border-white/[0.08] bg-slate-950/[0.96] lg:hidden">
        <div class="mx-auto flex max-w-7xl flex-col gap-2 px-6 py-5">
            {% for item in site_navigation %}
                <a @click="open = false" href="{{ item.url }}" class="rounded-2xl px-4 py-3 text-sm font-medium {% if request.path == item.url %}bg-white/[0.08] text-white{% else %}text-slate-300 hover:bg-white/5 hover:text-white{% endif %}">{{ item.label }}</a>
            {% endfor %}
            <a @click="open = false" href="{% url 'leads:contact' %}#contact-experience" class="button-primary mt-2 text-center text-sm">Start a project</a>
        </div>
    </div>
</header>


============================================================
FILE: templates/includes/hero_visual.html
============================================================
{% load static %}
<div class="hero-carousel-shell" data-reveal>
    <div class="hero-carousel-shell__glow"></div>
    <div class="media-carousel media-carousel--hero pointer-glow" data-media-carousel data-interval="6200">
        <div class="media-carousel__topbar">
            <div class="console-dots" aria-hidden="true"><span></span><span></span><span></span></div>
            <div class="status-chip status-chip-live">Founder-led delivery</div>
        </div>

        <div class="media-carousel__viewport">
            <article class="media-carousel__slide is-active" data-carousel-slide aria-hidden="false">
                <img src="{% static 'img/hero-network.jpg' %}" alt="Digital network visual" class="media-carousel__image">
                <div class="media-carousel__shade"></div>
                <div class="media-carousel__content">
                    <p class="media-carousel__eyebrow">Digital presence</p>
                    <h3 class="media-carousel__title">Premium websites and landing pages</h3>
                    <p class="media-carousel__text">Clear positioning, stronger trust, and conversion-focused customer journeys for modern companies.</p>
                    <div class="media-carousel__chips">
                        <span>Messaging</span><span>UX structure</span><span>Lead capture</span>
                    </div>
                </div>
            </article>

            <article class="media-carousel__slide" data-carousel-slide aria-hidden="true">
                <img src="{% static 'img/code-laptop.jpg' %}" alt="Software engineering and product build" class="media-carousel__image">
                <div class="media-carousel__shade"></div>
                <div class="media-carousel__content">
                    <p class="media-carousel__eyebrow">Product engineering</p>
                    <h3 class="media-carousel__title">Custom web apps, portals, and internal tools</h3>
                    <p class="media-carousel__text">Operational systems that fit how teams really work, from admin interfaces to client-facing products.</p>
                    <div class="media-carousel__chips">
                        <span>Web apps</span><span>Portals</span><span>Dashboards</span>
                    </div>
                </div>
            </article>

            <article class="media-carousel__slide" data-carousel-slide aria-hidden="true">
                <img src="https://images.unsplash.com/photo-1753907537890-f20de9e116cc?auto=format&fit=crop&fm=jpg&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&ixlib=rb-4.1.0&q=60&w=3000" alt="AI chatbot interface" class="media-carousel__image">
                <div class="media-carousel__shade"></div>
                <div class="media-carousel__content">
                    <p class="media-carousel__eyebrow">Applied AI</p>
                    <h3 class="media-carousel__title">Assistants, RAG, and workflow AI</h3>
                    <p class="media-carousel__text">Useful AI capability inside support, knowledge access, and product experiences — not just isolated demos.</p>
                    <div class="media-carousel__chips">
                        <span>Chatbots</span><span>RAG</span><span>LLM systems</span>
                    </div>
                </div>
            </article>

            <article class="media-carousel__slide" data-carousel-slide aria-hidden="true">
                <img src="{% static 'img/fiber-cables.jpg' %}" alt="Infrastructure and data systems" class="media-carousel__image">
                <div class="media-carousel__shade"></div>
                <div class="media-carousel__content">
                    <p class="media-carousel__eyebrow">Automation and data</p>
                    <h3 class="media-carousel__title">Backend systems, integrations, and pipelines</h3>
                    <p class="media-carousel__text">Automations and data flows that reduce manual work, improve visibility, and connect the tools a business depends on.</p>
                    <div class="media-carousel__chips">
                        <span>APIs</span><span>Automation</span><span>Pipelines</span>
                    </div>
                </div>
            </article>
        </div>

        <div class="media-carousel__footer">
            <div class="media-carousel__navlist">
                <button type="button" class="media-carousel__navitem is-active" data-carousel-jump="0">
                    <span class="media-carousel__navlabel">Websites</span>
                    <span class="media-carousel__navmeta">Premium business presence</span>
                </button>
                <button type="button" class="media-carousel__navitem" data-carousel-jump="1">
                    <span class="media-carousel__navlabel">Web apps</span>
                    <span class="media-carousel__navmeta">Products and internal tools</span>
                </button>
                <button type="button" class="media-carousel__navitem" data-carousel-jump="2">
                    <span class="media-carousel__navlabel">AI systems</span>
                    <span class="media-carousel__navmeta">Assistants and knowledge AI</span>
                </button>
                <button type="button" class="media-carousel__navitem" data-carousel-jump="3">
                    <span class="media-carousel__navlabel">Automation</span>
                    <span class="media-carousel__navmeta">Integrations and data flow</span>
                </button>
            </div>
            <div class="media-carousel__controls" aria-label="Hero visual controls">
                <button type="button" class="carousel-control" data-carousel-prev aria-label="Previous slide">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M14.5 6.5L9 12l5.5 5.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </button>
                <div class="media-carousel__dots" role="tablist" aria-label="Hero slides">
                    <button type="button" class="media-carousel__dot is-active" data-carousel-dot="0" aria-label="Go to slide 1"></button>
                    <button type="button" class="media-carousel__dot" data-carousel-dot="1" aria-label="Go to slide 2"></button>
                    <button type="button" class="media-carousel__dot" data-carousel-dot="2" aria-label="Go to slide 3"></button>
                    <button type="button" class="media-carousel__dot" data-carousel-dot="3" aria-label="Go to slide 4"></button>
                </div>
                <button type="button" class="carousel-control" data-carousel-next aria-label="Next slide">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M9.5 6.5L15 12l-5.5 5.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </button>
            </div>
        </div>

        <div class="hero-carousel-shell__badges">
            <div class="hero-floating-chip hero-floating-chip--one">Software + AI under one roof</div>
            <div class="hero-floating-chip hero-floating-chip--two">Startups · SMEs · Agencies · Enterprise</div>
            <div class="hero-floating-chip hero-floating-chip--three">Strategy → build → launch</div>
        </div>
    </div>
</div>


============================================================
FILE: templates/includes/owner_section.html
============================================================
<section class="rounded-[2rem] border border-white/10 bg-slate-950/60 p-8 shadow-glow backdrop-blur-xl lg:p-10">
    <div class="grid gap-8 lg:grid-cols-[1.02fr_.98fr] lg:items-center">
        <div>
            <p class="eyebrow">Meet the Owner</p>
            <h2 class="mt-4 font-display text-3xl font-bold tracking-tight text-white">Deep technical leadership that strengthens the studio brand.</h2>
            <p class="mt-5 text-base leading-7 text-slate-300">
                Led by {{ founder_name }}, a machine learning engineer with deep experience across AI systems, software delivery, and production-grade NLP and speech technologies.
            </p>
            <p class="mt-4 text-base leading-7 text-slate-400">
                The value for clients is not a founder showcase. It is tighter technical judgment, clearer scoping, and stronger delivery quality across websites, software, automation, and applied AI systems.
            </p>
        </div>
        <div class="grid gap-5 lg:grid-cols-[0.95fr_1.05fr]">
            <div class="surface-card h-full">
                {% include 'includes/service_graphic.html' with variant='strategy' %}
            </div>
            <div class="surface-card">
                <p class="text-sm uppercase tracking-[0.22em] text-slate-400">Founder credibility</p>
                <ul class="mt-5 space-y-4 text-sm text-slate-300">
                    <li>4+ years across AI systems, Python engineering, and product-oriented delivery</li>
                    <li>Experience spanning LLMs, prompt engineering, RAG, ASR, TTS, diarization, and deployment</li>
                    <li>Publications at LREC 2026, EACL 2026, and ChipSAL 2025</li>
                    <li>International research and training exposure in Germany and Sri Lanka</li>
                </ul>
                {% if owner_profile_url %}
                <a href="{{ owner_profile_url }}" target="_blank" rel="noopener noreferrer" class="button-secondary mt-7 inline-flex">View owner profile</a>
                {% endif %}
            </div>
        </div>
    </div>
</section>


============================================================
FILE: templates/includes/page_header.html
============================================================
<section class="relative overflow-hidden border-b border-white/[0.08] page-header-shell">
    <div class="absolute inset-0 bg-hero-radial opacity-80"></div>
    <div class="mx-auto grid max-w-7xl gap-12 px-6 py-20 lg:grid-cols-[0.95fr_1.05fr] lg:items-center lg:px-8 lg:py-24">
        <div class="relative z-10 max-w-3xl">
            {% if kicker %}<p class="eyebrow">{{ kicker }}</p>{% endif %}
            <h1 class="mt-4 font-display text-4xl font-bold tracking-tight text-white sm:text-5xl">{{ title }}</h1>
            <p class="mt-6 text-lg leading-8 text-slate-300">{{ intro }}</p>
            {% if supporting_copy %}
            <p class="mt-4 max-w-2xl text-base leading-7 text-slate-400">{{ supporting_copy }}</p>
            {% endif %}
        </div>
        <div class="relative z-10">
            {% include 'includes/page_visual.html' with visual=visual image=image image_alt=image_alt title=title %}
        </div>
    </div>
</section>


============================================================
FILE: templates/includes/page_visual.html
============================================================
{% load static %}
<div class="page-visual page-visual--{{ visual|default:'services' }}" data-reveal>
    <div class="media-carousel media-carousel--page pointer-glow" data-media-carousel data-interval="5600">
        <div class="media-carousel__viewport">
            {% if visual == 'services' %}
                <article class="media-carousel__slide is-active" data-carousel-slide aria-hidden="false">
                    <img src="{% static 'img/hero-network.jpg' %}" alt="Websites and digital presence" class="media-carousel__image">
                    <div class="media-carousel__shade"></div>
                    <div class="media-carousel__content media-carousel__content--page">
                        <p class="media-carousel__eyebrow">Websites</p>
                        <h3 class="media-carousel__title">Premium public-facing web experiences</h3>
                        <p class="media-carousel__text">Positioning, performance, conversion, and content structure that support growth.</p>
                        <div class="media-carousel__chips"><span>Company sites</span><span>Landing pages</span></div>
                    </div>
                </article>
                <article class="media-carousel__slide" data-carousel-slide aria-hidden="true">
                    <img src="{% static 'img/code-laptop.jpg' %}" alt="Custom applications and product delivery" class="media-carousel__image">
                    <div class="media-carousel__shade"></div>
                    <div class="media-carousel__content media-carousel__content--page">
                        <p class="media-carousel__eyebrow">Software products</p>
                        <h3 class="media-carousel__title">Apps, portals, and product engineering</h3>
                        <p class="media-carousel__text">Custom systems for recurring workflows, client access, reporting, and operations.</p>
                        <div class="media-carousel__chips"><span>Portals</span><span>Dashboards</span></div>
                    </div>
                </article>
                <article class="media-carousel__slide" data-carousel-slide aria-hidden="true">
                    <img src="https://images.unsplash.com/photo-1753907537890-f20de9e116cc?auto=format&fit=crop&fm=jpg&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&ixlib=rb-4.1.0&q=60&w=3000" alt="AI assistant interface" class="media-carousel__image">
                    <div class="media-carousel__shade"></div>
                    <div class="media-carousel__content media-carousel__content--page">
                        <p class="media-carousel__eyebrow">AI systems</p>
                        <h3 class="media-carousel__title">Assistants, chatbots, and knowledge access</h3>
                        <p class="media-carousel__text">Practical AI for search, support, lead handling, and internal knowledge workflows.</p>
                        <div class="media-carousel__chips"><span>RAG</span><span>Prompt systems</span></div>
                    </div>
                </article>
                <article class="media-carousel__slide" data-carousel-slide aria-hidden="true">
                    <img src="{% static 'img/fiber-cables.jpg' %}" alt="Backend infrastructure and data systems" class="media-carousel__image">
                    <div class="media-carousel__shade"></div>
                    <div class="media-carousel__content media-carousel__content--page">
                        <p class="media-carousel__eyebrow">Automation</p>
                        <h3 class="media-carousel__title">Integrations, backend systems, and data flow</h3>
                        <p class="media-carousel__text">Systems that connect tools, automate repetitive work, and provide cleaner visibility.</p>
                        <div class="media-carousel__chips"><span>APIs</span><span>Pipelines</span></div>
                    </div>
                </article>
            {% elif visual == 'about' %}
                <article class="media-carousel__slide is-active" data-carousel-slide aria-hidden="false">
                    <img src="https://images.unsplash.com/photo-1758873268745-dd2cf0d677b5?auto=format&fit=crop&fm=jpg&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&ixlib=rb-4.1.0&q=60&w=3000" alt="Collaborative product team working together" class="media-carousel__image">
                    <div class="media-carousel__shade"></div>
                    <div class="media-carousel__content media-carousel__content--page">
                        <p class="media-carousel__eyebrow">How the studio works</p>
                        <h3 class="media-carousel__title">Small-team clarity with technical depth</h3>
                        <p class="media-carousel__text">A delivery model designed to stay commercially sharp and technically grounded.</p>
                        <div class="media-carousel__chips"><span>Founder-led</span><span>Hands-on</span></div>
                    </div>
                </article>
                <article class="media-carousel__slide" data-carousel-slide aria-hidden="true">
                    <img src="https://images.unsplash.com/photo-1758873269035-aae0e1fd3422?auto=format&fit=crop&fm=jpg&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&ixlib=rb-4.1.0&q=60&w=3000" alt="Team workshop and planning session" class="media-carousel__image">
                    <div class="media-carousel__shade"></div>
                    <div class="media-carousel__content media-carousel__content--page">
                        <p class="media-carousel__eyebrow">Studio mindset</p>
                        <h3 class="media-carousel__title">Scope, structure, and collaborative planning</h3>
                        <p class="media-carousel__text">Projects move forward through practical scoping, system thinking, and delivery discipline.</p>
                        <div class="media-carousel__chips"><span>Planning</span><span>Execution</span></div>
                    </div>
                </article>
                <article class="media-carousel__slide" data-carousel-slide aria-hidden="true">
                    <img src="{% static 'img/code-laptop.jpg' %}" alt="Software engineering details" class="media-carousel__image">
                    <div class="media-carousel__shade"></div>
                    <div class="media-carousel__content media-carousel__content--page">
                        <p class="media-carousel__eyebrow">Capability</p>
                        <h3 class="media-carousel__title">Product, Python, AI, and backend delivery</h3>
                        <p class="media-carousel__text">The studio combines strategy and implementation rather than separating them too early.</p>
                        <div class="media-carousel__chips"><span>Python-first</span><span>Maintainable</span></div>
                    </div>
                </article>
            {% elif visual == 'solutions' %}
                <article class="media-carousel__slide is-active" data-carousel-slide aria-hidden="false">
                    <img src="https://images.unsplash.com/photo-1758873268745-dd2cf0d677b5?auto=format&fit=crop&fm=jpg&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&ixlib=rb-4.1.0&q=60&w=3000" alt="Teams collaborating around a workstation" class="media-carousel__image">
                    <div class="media-carousel__shade"></div>
                    <div class="media-carousel__content media-carousel__content--page">
                        <p class="media-carousel__eyebrow">Startups</p>
                        <h3 class="media-carousel__title">Fast-moving product and MVP delivery</h3>
                        <p class="media-carousel__text">Clearer launches, sharper scope, and working systems that support traction.</p>
                        <div class="media-carousel__chips"><span>MVPs</span><span>Launches</span></div>
                    </div>
                </article>
                <article class="media-carousel__slide" data-carousel-slide aria-hidden="true">
                    <img src="{% static 'img/fiber-cables.jpg' %}" alt="Connected business systems" class="media-carousel__image">
                    <div class="media-carousel__shade"></div>
                    <div class="media-carousel__content media-carousel__content--page">
                        <p class="media-carousel__eyebrow">SMEs</p>
                        <h3 class="media-carousel__title">Operational systems that reduce friction</h3>
                        <p class="media-carousel__text">Better lead handling, cleaner workflows, and more connected data across the business.</p>
                        <div class="media-carousel__chips"><span>Automation</span><span>CRM flow</span></div>
                    </div>
                </article>
                <article class="media-carousel__slide" data-carousel-slide aria-hidden="true">
                    <img src="https://images.unsplash.com/photo-1758518727401-53823b36c47b?auto=format&fit=crop&fm=jpg&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&ixlib=rb-4.1.0&q=60&w=3000" alt="Professional team discussion" class="media-carousel__image">
                    <div class="media-carousel__shade"></div>
                    <div class="media-carousel__content media-carousel__content--page">
                        <p class="media-carousel__eyebrow">Enterprise teams</p>
                        <h3 class="media-carousel__title">Internal tools, knowledge systems, and AI layers</h3>
                        <p class="media-carousel__text">Custom software and retrieval workflows for teams working with complexity and scale.</p>
                        <div class="media-carousel__chips"><span>Knowledge</span><span>Internal tools</span></div>
                    </div>
                </article>
            {% elif visual == 'work' %}
                <article class="media-carousel__slide is-active" data-carousel-slide aria-hidden="false">
                    <img src="https://images.unsplash.com/photo-1753907537890-f20de9e116cc?auto=format&fit=crop&fm=jpg&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&ixlib=rb-4.1.0&q=60&w=3000" alt="AI assistant interface" class="media-carousel__image">
                    <div class="media-carousel__shade"></div>
                    <div class="media-carousel__content media-carousel__content--page">
                        <p class="media-carousel__eyebrow">Conversational AI</p>
                        <h3 class="media-carousel__title">Assistants, QA systems, and CRM-connected workflows</h3>
                        <p class="media-carousel__text">Representative builds across support, knowledge access, and customer communication.</p>
                        <div class="media-carousel__chips"><span>Chatbots</span><span>WhatsApp</span></div>
                    </div>
                </article>
                <article class="media-carousel__slide" data-carousel-slide aria-hidden="true">
                    <img src="{% static 'img/fiber-cables.jpg' %}" alt="Data infrastructure" class="media-carousel__image">
                    <div class="media-carousel__shade"></div>
                    <div class="media-carousel__content media-carousel__content--page">
                        <p class="media-carousel__eyebrow">Data systems</p>
                        <h3 class="media-carousel__title">Scraping, pipelines, dashboards, and backend logic</h3>
                        <p class="media-carousel__text">Business infrastructure work that powers reporting, automation, and operational clarity.</p>
                        <div class="media-carousel__chips"><span>ETL</span><span>Dashboards</span></div>
                    </div>
                </article>
                <article class="media-carousel__slide" data-carousel-slide aria-hidden="true">
                    <img src="{% static 'img/hero-network.jpg' %}" alt="Networked digital systems" class="media-carousel__image">
                    <div class="media-carousel__shade"></div>
                    <div class="media-carousel__content media-carousel__content--page">
                        <p class="media-carousel__eyebrow">Research-backed AI</p>
                        <h3 class="media-carousel__title">Model adaptation, RAG, and evaluation work</h3>
                        <p class="media-carousel__text">Anonymized examples that show breadth without drifting into academic portfolio territory.</p>
                        <div class="media-carousel__chips"><span>Evaluation</span><span>LLMs</span></div>
                    </div>
                </article>
            {% elif visual == 'insights' %}
                <article class="media-carousel__slide is-active" data-carousel-slide aria-hidden="false">
                    <img src="{% static 'img/blue-beams.jpg' %}" alt="Technical research and systems theme" class="media-carousel__image">
                    <div class="media-carousel__shade"></div>
                    <div class="media-carousel__content media-carousel__content--page">
                        <p class="media-carousel__eyebrow">Implementation strategy</p>
                        <h3 class="media-carousel__title">Research thinking translated into delivery decisions</h3>
                        <p class="media-carousel__text">A practical view on when to use AI, how to evaluate it, and how to ship it well.</p>
                        <div class="media-carousel__chips"><span>Strategy</span><span>Evaluation</span></div>
                    </div>
                </article>
                <article class="media-carousel__slide" data-carousel-slide aria-hidden="true">
                    <img src="https://images.unsplash.com/photo-1753907537890-f20de9e116cc?auto=format&fit=crop&fm=jpg&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&ixlib=rb-4.1.0&q=60&w=3000" alt="AI system interface" class="media-carousel__image">
                    <div class="media-carousel__shade"></div>
                    <div class="media-carousel__content media-carousel__content--page">
                        <p class="media-carousel__eyebrow">AI systems</p>
                        <h3 class="media-carousel__title">LLM workflows, prompt design, and knowledge grounding</h3>
                        <p class="media-carousel__text">Topics that matter to teams building AI features that need to be reliable and useful.</p>
                        <div class="media-carousel__chips"><span>RAG</span><span>Prompting</span></div>
                    </div>
                </article>
                <article class="media-carousel__slide" data-carousel-slide aria-hidden="true">
                    <img src="{% static 'img/circuit-touch.jpg' %}" alt="Speech and system interfaces" class="media-carousel__image">
                    <div class="media-carousel__shade"></div>
                    <div class="media-carousel__content media-carousel__content--page">
                        <p class="media-carousel__eyebrow">Speech systems</p>
                        <h3 class="media-carousel__title">Speech AI, ASR, diarization, and voice-enabled workflows</h3>
                        <p class="media-carousel__text">Selected technical areas where the studio has deeper engineering credibility.</p>
                        <div class="media-carousel__chips"><span>ASR</span><span>Diarization</span></div>
                    </div>
                </article>
            {% elif visual == 'contact' %}
                <article class="media-carousel__slide is-active" data-carousel-slide aria-hidden="false">
                    <img src="https://images.unsplash.com/photo-1758873268745-dd2cf0d677b5?auto=format&fit=crop&fm=jpg&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&ixlib=rb-4.1.0&q=60&w=3000" alt="Team collaborating on a digital project" class="media-carousel__image">
                    <div class="media-carousel__shade"></div>
                    <div class="media-carousel__content media-carousel__content--page">
                        <p class="media-carousel__eyebrow">Project intake</p>
                        <h3 class="media-carousel__title">A guided first contact, not a dead-end form</h3>
                        <p class="media-carousel__text">Enough structure to qualify the work, keep it efficient, and make the next reply more useful.</p>
                        <div class="media-carousel__chips"><span>Guided</span><span>Fast</span></div>
                    </div>
                </article>
                <article class="media-carousel__slide" data-carousel-slide aria-hidden="true">
                    <img src="https://images.unsplash.com/photo-1758873269035-aae0e1fd3422?auto=format&fit=crop&fm=jpg&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&ixlib=rb-4.1.0&q=60&w=3000" alt="Project planning and discovery session" class="media-carousel__image">
                    <div class="media-carousel__shade"></div>
                    <div class="media-carousel__content media-carousel__content--page">
                        <p class="media-carousel__eyebrow">Discovery</p>
                        <h3 class="media-carousel__title">Clearer scope, timing, and service fit</h3>
                        <p class="media-carousel__text">The intake helps define whether the project needs a website, app, automation, AI system, or some combination.</p>
                        <div class="media-carousel__chips"><span>Scope</span><span>Fit</span></div>
                    </div>
                </article>
                <article class="media-carousel__slide" data-carousel-slide aria-hidden="true">
                    <img src="https://images.unsplash.com/photo-1758518727401-53823b36c47b?auto=format&fit=crop&fm=jpg&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&ixlib=rb-4.1.0&q=60&w=3000" alt="Business follow-up meeting" class="media-carousel__image">
                    <div class="media-carousel__shade"></div>
                    <div class="media-carousel__content media-carousel__content--page">
                        <p class="media-carousel__eyebrow">Follow-up</p>
                        <h3 class="media-carousel__title">Direct response with a practical next step</h3>
                        <p class="media-carousel__text">That may be a scoped follow-up, a discovery call, or a recommendation on where to start.</p>
                        <div class="media-carousel__chips"><span>Reply</span><span>Next step</span></div>
                    </div>
                </article>
            {% else %}
                <article class="media-carousel__slide is-active" data-carousel-slide aria-hidden="false">
                    <img src="{% static 'img/blue-beams.jpg' %}" alt="Privacy and system security theme" class="media-carousel__image">
                    <div class="media-carousel__shade"></div>
                    <div class="media-carousel__content media-carousel__content--page">
                        <p class="media-carousel__eyebrow">Responsible handling</p>
                        <h3 class="media-carousel__title">Contact information is handled with care</h3>
                        <p class="media-carousel__text">The site stores only the information needed to respond and manage enquiries appropriately.</p>
                        <div class="media-carousel__chips"><span>Privacy</span><span>Lead handling</span></div>
                    </div>
                </article>
                <article class="media-carousel__slide" data-carousel-slide aria-hidden="true">
                    <img src="{% static 'img/fiber-cables.jpg' %}" alt="Protected systems and infrastructure" class="media-carousel__image">
                    <div class="media-carousel__shade"></div>
                    <div class="media-carousel__content media-carousel__content--page">
                        <p class="media-carousel__eyebrow">System layer</p>
                        <h3 class="media-carousel__title">Python-first backend with protected lead access</h3>
                        <p class="media-carousel__text">Structured form handling, storage, and notification support for serious enquiry flow.</p>
                        <div class="media-carousel__chips"><span>Django</span><span>Admin</span></div>
                    </div>
                </article>
            {% endif %}
        </div>

        <div class="media-carousel__footer media-carousel__footer--page">
            <div class="media-carousel__dots" role="tablist" aria-label="Page visual slides">
                {% if visual == 'services' %}
                    <button type="button" class="media-carousel__dot is-active" data-carousel-dot="0" aria-label="Go to first slide"></button>
                    <button type="button" class="media-carousel__dot" data-carousel-dot="1" aria-label="Go to second slide"></button>
                    <button type="button" class="media-carousel__dot" data-carousel-dot="2" aria-label="Go to third slide"></button>
                    <button type="button" class="media-carousel__dot" data-carousel-dot="3" aria-label="Go to fourth slide"></button>
                {% elif visual == 'privacy' %}
                    <button type="button" class="media-carousel__dot is-active" data-carousel-dot="0" aria-label="Go to first slide"></button>
                    <button type="button" class="media-carousel__dot" data-carousel-dot="1" aria-label="Go to second slide"></button>
                {% else %}
                    <button type="button" class="media-carousel__dot is-active" data-carousel-dot="0" aria-label="Go to first slide"></button>
                    <button type="button" class="media-carousel__dot" data-carousel-dot="1" aria-label="Go to second slide"></button>
                    <button type="button" class="media-carousel__dot" data-carousel-dot="2" aria-label="Go to third slide"></button>
                {% endif %}
            </div>
            <div class="media-carousel__controls" aria-label="Page visual controls">
                <button type="button" class="carousel-control" data-carousel-prev aria-label="Previous slide">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M14.5 6.5L9 12l5.5 5.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </button>
                <button type="button" class="carousel-control" data-carousel-next aria-label="Next slide">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M9.5 6.5L15 12l-5.5 5.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </button>
            </div>
        </div>
    </div>
</div>


============================================================
FILE: templates/includes/service_graphic.html
============================================================
<div class="service-graphic service-graphic--{{ variant|default:'product' }}{% if compact %} service-graphic--compact{% endif %}" aria-hidden="true">
{% if variant == 'chatbot' %}
<svg viewBox="0 0 220 132" xmlns="http://www.w3.org/2000/svg" fill="none">
    <defs>
        <linearGradient id="sgChatA" x1="22" y1="14" x2="190" y2="118" gradientUnits="userSpaceOnUse">
            <stop stop-color="#4EE7C2"/>
            <stop offset="1" stop-color="#1870F8"/>
        </linearGradient>
    </defs>
    <rect x="18" y="14" width="184" height="104" rx="24" class="sg-panel"/>
    <circle cx="36" cy="30" r="3" class="sg-dot sg-pulse"/>
    <circle cx="48" cy="30" r="3" class="sg-dot sg-pulse"/>
    <circle cx="60" cy="30" r="3" class="sg-dot sg-pulse"/>
    <rect x="34" y="44" width="84" height="18" rx="9" fill="url(#sgChatA)" fill-opacity="0.95" class="sg-float"/>
    <rect x="34" y="71" width="116" height="15" rx="7.5" class="sg-soft"/>
    <rect x="156" y="76" width="30" height="30" rx="12" fill="url(#sgChatA)" fill-opacity="0.22"/>
    <path d="M168.5 87.5c0-4.1 3.4-7.5 7.5-7.5s7.5 3.4 7.5 7.5" stroke="url(#sgChatA)" stroke-width="2.4" stroke-linecap="round"/>
    <path d="M170 94h12" stroke="url(#sgChatA)" stroke-width="2.4" stroke-linecap="round"/>
    <rect x="84" y="94" width="72" height="10" rx="5" class="sg-soft"/>
</svg>
{% elif variant == 'knowledge' %}
<svg viewBox="0 0 220 132" xmlns="http://www.w3.org/2000/svg" fill="none">
    <defs>
        <linearGradient id="sgKnowA" x1="40" y1="24" x2="178" y2="112" gradientUnits="userSpaceOnUse">
            <stop stop-color="#1870F8"/>
            <stop offset="1" stop-color="#4EE7C2"/>
        </linearGradient>
    </defs>
    <rect x="24" y="18" width="96" height="78" rx="18" class="sg-panel"/>
    <rect x="38" y="34" width="54" height="8" rx="4" class="sg-soft"/>
    <rect x="38" y="51" width="68" height="8" rx="4" class="sg-soft"/>
    <rect x="38" y="68" width="58" height="8" rx="4" class="sg-soft"/>
    <circle cx="158" cy="58" r="26" stroke="url(#sgKnowA)" stroke-width="2.6" class="sg-orbit"/>
    <circle cx="158" cy="58" r="10" fill="url(#sgKnowA)" fill-opacity="0.28" class="sg-pulse"/>
    <path d="M176 76l16 16" stroke="url(#sgKnowA)" stroke-width="3" stroke-linecap="round"/>
    <circle cx="132" cy="30" r="4" fill="#4EE7C2" class="sg-pulse"/>
    <circle cx="187" cy="38" r="4" fill="#1870F8" class="sg-pulse"/>
    <circle cx="194" cy="88" r="4" fill="#4EE7C2" class="sg-pulse"/>
</svg>
{% elif variant == 'automation' %}
<svg viewBox="0 0 220 132" xmlns="http://www.w3.org/2000/svg" fill="none">
    <defs>
        <linearGradient id="sgAutoA" x1="26" y1="34" x2="194" y2="82" gradientUnits="userSpaceOnUse">
            <stop stop-color="#4EE7C2"/>
            <stop offset="1" stop-color="#1870F8"/>
        </linearGradient>
    </defs>
    <rect x="20" y="28" width="36" height="36" rx="14" class="sg-panel"/>
    <rect x="92" y="18" width="36" height="36" rx="14" class="sg-panel"/>
    <rect x="164" y="58" width="36" height="36" rx="14" class="sg-panel"/>
    <path d="M56 46h36M128 36h24c18 0 24 14 24 28" stroke="url(#sgAutoA)" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" class="sg-dash"/>
    <path d="M77 42l15 4-15 4" stroke="url(#sgAutoA)" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M176 50l10 14-16 4" stroke="url(#sgAutoA)" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="38" cy="46" r="8" fill="#4EE7C2" fill-opacity="0.23" class="sg-pulse"/>
    <circle cx="110" cy="36" r="8" fill="#1870F8" fill-opacity="0.23" class="sg-pulse"/>
    <circle cx="182" cy="76" r="8" fill="#4EE7C2" fill-opacity="0.23" class="sg-pulse"/>
    <rect x="26" y="84" width="110" height="22" rx="11" class="sg-soft"/>
</svg>
{% elif variant == 'speech' %}
<svg viewBox="0 0 220 132" xmlns="http://www.w3.org/2000/svg" fill="none">
    <defs>
        <linearGradient id="sgSpeechA" x1="34" y1="66" x2="192" y2="66" gradientUnits="userSpaceOnUse">
            <stop stop-color="#1870F8"/>
            <stop offset="1" stop-color="#4EE7C2"/>
        </linearGradient>
    </defs>
    <rect x="24" y="24" width="172" height="84" rx="24" class="sg-panel"/>
    <path d="M42 66h8l8-20 12 40 14-58 14 76 14-52 12 28 10-14 10 0 12-10 16 0" stroke="url(#sgSpeechA)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="sg-dash"/>
    <circle cx="166" cy="48" r="14" fill="url(#sgSpeechA)" fill-opacity="0.24" class="sg-pulse"/>
    <path d="M166 42v12M160 47c0-3.2 2.6-5.8 5.8-5.8S171.6 43.8 171.6 47" stroke="url(#sgSpeechA)" stroke-width="2.2" stroke-linecap="round"/>
</svg>
{% elif variant == 'website' %}
<svg viewBox="0 0 220 132" xmlns="http://www.w3.org/2000/svg" fill="none">
    <defs>
        <linearGradient id="sgWebA" x1="28" y1="20" x2="190" y2="102" gradientUnits="userSpaceOnUse">
            <stop stop-color="#1870F8"/>
            <stop offset="1" stop-color="#4EE7C2"/>
        </linearGradient>
    </defs>
    <rect x="22" y="16" width="176" height="100" rx="26" class="sg-panel"/>
    <circle cx="42" cy="34" r="3" class="sg-dot"/>
    <circle cx="54" cy="34" r="3" class="sg-dot"/>
    <circle cx="66" cy="34" r="3" class="sg-dot"/>
    <rect x="40" y="50" width="68" height="34" rx="14" fill="url(#sgWebA)" fill-opacity="0.22"/>
    <rect x="118" y="50" width="44" height="10" rx="5" class="sg-soft"/>
    <rect x="118" y="68" width="52" height="10" rx="5" class="sg-soft"/>
    <rect x="118" y="88" width="38" height="12" rx="6" fill="url(#sgWebA)" fill-opacity="0.85" class="sg-float"/>
</svg>
{% elif variant == 'dashboard' %}
<svg viewBox="0 0 220 132" xmlns="http://www.w3.org/2000/svg" fill="none">
    <defs>
        <linearGradient id="sgDashA" x1="26" y1="20" x2="190" y2="108" gradientUnits="userSpaceOnUse">
            <stop stop-color="#4EE7C2"/>
            <stop offset="1" stop-color="#1870F8"/>
        </linearGradient>
    </defs>
    <rect x="20" y="16" width="180" height="100" rx="24" class="sg-panel"/>
    <path d="M42 88V54M70 88V42M98 88V60M126 88V34" stroke="url(#sgDashA)" stroke-width="8" stroke-linecap="round"/>
    <path d="M44 40c18 10 32 10 46 0 13-9 29-9 44 3 12 9 26 11 44 4" stroke="url(#sgDashA)" stroke-width="3" stroke-linecap="round" class="sg-dash"/>
    <circle cx="168" cy="42" r="12" fill="#4EE7C2" fill-opacity="0.18" class="sg-pulse"/>
</svg>
{% elif variant == 'llm' %}
<svg viewBox="0 0 220 132" xmlns="http://www.w3.org/2000/svg" fill="none">
    <defs>
        <linearGradient id="sgLlmA" x1="34" y1="20" x2="186" y2="100" gradientUnits="userSpaceOnUse">
            <stop stop-color="#1870F8"/>
            <stop offset="1" stop-color="#4EE7C2"/>
        </linearGradient>
    </defs>
    <rect x="28" y="20" width="52" height="80" rx="18" class="sg-panel"/>
    <rect x="84" y="26" width="52" height="68" rx="18" class="sg-panel"/>
    <rect x="140" y="34" width="52" height="52" rx="18" class="sg-panel"/>
    <path d="M80 38h4c8 0 14 6 14 14v0c0 8 6 14 14 14h28" stroke="url(#sgLlmA)" stroke-width="2.6" stroke-linecap="round" class="sg-dash"/>
    <path d="M80 82h4c8 0 14-6 14-14v0c0-8 6-14 14-14h28" stroke="url(#sgLlmA)" stroke-width="2.6" stroke-linecap="round" class="sg-dash"/>
    <circle cx="54" cy="60" r="8" fill="#1870F8" fill-opacity="0.24" class="sg-pulse"/>
    <circle cx="110" cy="60" r="8" fill="#4EE7C2" fill-opacity="0.24" class="sg-pulse"/>
    <circle cx="166" cy="60" r="8" fill="#1870F8" fill-opacity="0.24" class="sg-pulse"/>
</svg>
{% elif variant == 'portal' or variant == 'webapp' or variant == 'product' %}
<svg viewBox="0 0 220 132" xmlns="http://www.w3.org/2000/svg" fill="none">
    <defs>
        <linearGradient id="sgProdA" x1="26" y1="20" x2="188" y2="110" gradientUnits="userSpaceOnUse">
            <stop stop-color="#1870F8"/>
            <stop offset="1" stop-color="#4EE7C2"/>
        </linearGradient>
    </defs>
    <rect x="20" y="16" width="118" height="98" rx="24" class="sg-panel"/>
    <rect x="146" y="28" width="54" height="34" rx="16" class="sg-panel"/>
    <rect x="146" y="70" width="54" height="26" rx="14" fill="url(#sgProdA)" fill-opacity="0.18"/>
    <rect x="38" y="34" width="82" height="12" rx="6" class="sg-soft"/>
    <rect x="38" y="54" width="60" height="28" rx="14" fill="url(#sgProdA)" fill-opacity="0.9" class="sg-float"/>
    <rect x="104" y="54" width="16" height="28" rx="8" class="sg-soft"/>
    <rect x="38" y="90" width="82" height="8" rx="4" class="sg-soft"/>
</svg>
{% elif variant == 'strategy' %}
<svg viewBox="0 0 220 132" xmlns="http://www.w3.org/2000/svg" fill="none">
    <defs>
        <linearGradient id="sgStrategyA" x1="44" y1="16" x2="170" y2="110" gradientUnits="userSpaceOnUse">
            <stop stop-color="#4EE7C2"/>
            <stop offset="1" stop-color="#1870F8"/>
        </linearGradient>
    </defs>
    <circle cx="110" cy="66" r="32" stroke="url(#sgStrategyA)" stroke-width="2.6" class="sg-orbit"/>
    <circle cx="110" cy="66" r="54" stroke="rgba(24,112,248,0.22)" stroke-width="1.4"/>
    <circle cx="110" cy="66" r="16" fill="url(#sgStrategyA)" fill-opacity="0.24" class="sg-pulse"/>
    <rect x="28" y="22" width="54" height="18" rx="9" class="sg-soft"/>
    <rect x="150" y="92" width="42" height="18" rx="9" class="sg-soft"/>
    <rect x="32" y="90" width="46" height="18" rx="9" fill="url(#sgStrategyA)" fill-opacity="0.84" class="sg-float"/>
    <circle cx="162" cy="34" r="6" fill="#1870F8" class="sg-pulse"/>
    <circle cx="58" cy="62" r="6" fill="#4EE7C2" class="sg-pulse"/>
    <circle cx="168" cy="80" r="6" fill="#4EE7C2" class="sg-pulse"/>
</svg>
{% elif variant == 'lock' %}
<svg viewBox="0 0 220 132" xmlns="http://www.w3.org/2000/svg" fill="none">
    <defs>
        <linearGradient id="sgLockA" x1="56" y1="18" x2="164" y2="116" gradientUnits="userSpaceOnUse">
            <stop stop-color="#1870F8"/>
            <stop offset="1" stop-color="#4EE7C2"/>
        </linearGradient>
    </defs>
    <rect x="58" y="44" width="104" height="60" rx="22" class="sg-panel"/>
    <path d="M82 48V38c0-16 12-28 28-28s28 12 28 28v10" stroke="url(#sgLockA)" stroke-width="3" stroke-linecap="round"/>
    <circle cx="110" cy="72" r="11" fill="url(#sgLockA)" fill-opacity="0.2" class="sg-pulse"/>
    <path d="M110 68v10" stroke="url(#sgLockA)" stroke-width="2.6" stroke-linecap="round"/>
    <path d="M102 72c0-4.4 3.6-8 8-8s8 3.6 8 8" stroke="url(#sgLockA)" stroke-width="2.6" stroke-linecap="round"/>
</svg>
{% else %}
<svg viewBox="0 0 220 132" xmlns="http://www.w3.org/2000/svg" fill="none">
    <defs>
        <linearGradient id="sgDefaultA" x1="30" y1="22" x2="188" y2="108" gradientUnits="userSpaceOnUse">
            <stop stop-color="#1870F8"/>
            <stop offset="1" stop-color="#4EE7C2"/>
        </linearGradient>
    </defs>
    <rect x="22" y="18" width="176" height="96" rx="24" class="sg-panel"/>
    <path d="M42 90c26-30 54-46 84-46s42 7 52 16" stroke="url(#sgDefaultA)" stroke-width="3" stroke-linecap="round" class="sg-dash"/>
    <circle cx="72" cy="70" r="10" fill="#1870F8" fill-opacity="0.24" class="sg-pulse"/>
    <circle cx="128" cy="54" r="10" fill="#4EE7C2" fill-opacity="0.24" class="sg-pulse"/>
    <circle cx="170" cy="78" r="10" fill="#1870F8" fill-opacity="0.24" class="sg-pulse"/>
</svg>
{% endif %}
</div>


============================================================
FILE: templates/includes/theme_toggle.html
============================================================
<button type="button" class="theme-toggle-switch" data-theme-toggle role="switch" aria-checked="false" aria-label="Toggle color theme">
    <span class="theme-toggle-switch__track" aria-hidden="true">
        <span class="theme-toggle-switch__icon theme-toggle-switch__icon--sun">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 3V5.5M12 18.5V21M4.93 4.93L6.7 6.7M17.3 17.3L19.07 19.07M3 12H5.5M18.5 12H21M4.93 19.07L6.7 17.3M17.3 6.7L19.07 4.93" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/>
                <circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/>
            </svg>
        </span>
        <span class="theme-toggle-switch__icon theme-toggle-switch__icon--moon">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M20.2 14.2A8.2 8.2 0 1 1 9.8 3.8a6.8 6.8 0 1 0 10.4 10.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/>
            </svg>
        </span>
        <span class="theme-toggle-switch__thumb"></span>
    </span>
    <span class="theme-toggle-switch__label" data-theme-label>Dark</span>
</button>


============================================================
FILE: templates/leads/contact.html
============================================================
{% extends 'base.html' %}

{% block content %}
{% include 'includes/page_header.html' with kicker='Contact' title='Start with a guided project intake.' intro='This contact experience is designed like a lightweight product flow: one question at a time, clear progress, and enough structure to turn a good enquiry into a useful next step.' supporting_copy='It is intentionally more guided than a generic contact form, while still staying quick for serious buyers.' visual='contact' image='img/circuit-touch.jpg' image_alt='Interactive circuit interface' %}

<section class="section-shell">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        {% if submitted %}
        <div class="confirmation-inline-panel mb-8" id="contact-confirmation">
            <div class="flex flex-col gap-5 md:flex-row md:items-center md:justify-between">
                <div>
                    <p class="eyebrow">Enquiry received</p>
                    <h2 class="mt-4 font-display text-3xl font-semibold text-white">Your information has been submitted.</h2>
                    <p class="mt-3 max-w-2xl text-sm leading-7 text-slate-300">{{ success_message }}</p>
                </div>
                <div class="rounded-3xl border border-accent-400/20 bg-accent-400/10 px-5 py-4 text-sm text-accent-100">
                    <div class="font-semibold text-white">Next step</div>
                    <div class="mt-1 text-accent-100/85">Our team will review the brief and contact you directly.</div>
                </div>
            </div>
        </div>
        {% endif %}

        <div x-data="contactExperience()" id="contact-experience" class="grid gap-8 lg:grid-cols-[1.08fr_.92fr]">
            <div class="surface-card pointer-glow relative overflow-hidden contact-flow-shell">
                <div class="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-brand-300/60 to-transparent"></div>
                <div class="absolute -right-10 top-10 h-40 w-40 rounded-full bg-brand-500/10 blur-3xl"></div>
                <div class="absolute -left-8 bottom-0 h-36 w-36 rounded-full bg-accent-400/10 blur-3xl"></div>

                <div class="relative z-10">
                    <div class="flex flex-col gap-6 border-b border-white/10 pb-6 lg:flex-row lg:items-end lg:justify-between">
                        <div class="max-w-2xl">
                            <p class="eyebrow">Guided intake</p>
                            <h2 class="mt-4 font-display text-3xl font-bold tracking-tight text-white">Tell us what you need in a few focused steps.</h2>
                            <p class="mt-4 text-sm leading-7 text-slate-400">This is the recommended route for the studio. It qualifies scope quickly, reduces vague back-and-forth, and helps us respond with a practical next step.</p>
                        </div>
                        <div class="wizard-status-card">
                            <div class="wizard-status-card__top">
                                <span class="font-medium text-white">Progress</span>
                                <span class="text-sm text-slate-300" x-text="`${step}/${steps.length}`"></span>
                            </div>
                            <div class="stepper-bar mt-4"><div class="stepper-bar__progress" :style="`width:${progress}%`"></div></div>
                            <div class="mt-4 text-sm text-slate-400" x-text="currentStep.hint"></div>
                        </div>
                    </div>

                    <form x-ref="wizardForm" method="post" action="{% url 'leads:contact' %}" @submit.prevent="submit($refs.wizardForm)" class="mt-8 grid gap-8">
                        {% csrf_token %}
                        <input type="hidden" name="referrer" value="" data-referrer-field>
                        <input type="hidden" name="inquiry_type" :value="form.inquiry_type">
                        <input type="hidden" name="submission_mode" value="guided">
                        <input type="hidden" name="website" value="">
                        <input type="hidden" name="service_interest" :value="form.service_interest">
                        <input type="hidden" name="budget" :value="form.budget">
                        <input type="hidden" name="timeline" :value="form.timeline">
                        <input type="hidden" name="name" :value="form.name">
                        <input type="hidden" name="email" :value="form.email">
                        <input type="hidden" name="company" :value="form.company">
                        <input type="hidden" name="phone" :value="form.phone">
                        <input type="hidden" name="message" :value="form.message">

                        <div class="wizard-steps" aria-label="Project intake steps">
                            <template x-for="item in steps" :key="item.index">
                                <button type="button" class="step-chip text-left" :class="step >= item.index ? 'is-current' : ''" @click="goTo(item.index)">
                                    <span class="step-chip__index" x-text="item.index"></span>
                                    <span>
                                        <span class="block text-sm font-medium text-white" x-text="item.label"></span>
                                        <span class="step-chip__hint mt-1 block text-xs leading-5 text-slate-400" x-text="item.hint"></span>
                                    </span>
                                </button>
                            </template>
                        </div>

                        <div class="wizard-panel-stack">
                            <section x-show="step === 1" x-transition.opacity.duration.250ms class="wizard-panel">
                                <div>
                                    <p class="wizard-panel__eyebrow">Step 1</p>
                                    <h3 class="wizard-panel__title">What do you need us to help with?</h3>
                                    <p class="wizard-panel__text">Choose the closest fit. You can add detail later.</p>
                                </div>
                                <div class="choice-grid choice-grid--services mt-8">
                                    {% for value, label in service_choices %}
                                    <button type="button" class="choice-card" :class="form.service_interest === '{{ value }}' ? 'is-selected' : ''" @click="pickService('{{ value }}')">
                                        <span class="choice-card__title">{{ label }}</span>
                                        <span class="choice-card__meta">
                                            {% if value == 'ai-strategy' %}Roadmap and implementation direction{% elif value == 'ai-chatbot' %}Support, lead capture, or assistant flows{% elif value == 'rag-knowledge' %}Knowledge access grounded in your content{% elif value == 'llm-fine-tuning' %}Model adaptation and evaluation{% elif value == 'speech-ai' %}ASR, diarization, TTS, voice workflows{% elif value == 'website-development' %}Premium public-facing web presence{% elif value == 'web-application-development' %}Custom portals, SaaS, and internal apps{% elif value == 'automation-backend-systems' %}Integrations, rules, and backend logic{% elif value == 'data-pipelines-scraping' %}Pipelines, reporting, and structured data{% elif value == 'product-mvp-build' %}Product delivery from concept to launch{% elif value == 'research-collaboration' %}Technical collaboration and research-led work{% else %}Something adjacent or still being shaped{% endif %}
                                        </span>
                                    </button>
                                    {% endfor %}
                                </div>
                                <p class="error-text" x-cloak x-show="serverErrors.service_interest" x-text="serverErrors.service_interest"></p>
                            </section>

                            <section x-show="step === 2" x-transition.opacity.duration.250ms class="wizard-panel">
                                <div>
                                    <p class="wizard-panel__eyebrow">Step 2</p>
                                    <h3 class="wizard-panel__title">What budget range are you working with?</h3>
                                    <p class="wizard-panel__text">A realistic range helps us recommend the right delivery shape.</p>
                                </div>
                                <div class="choice-grid mt-8">
                                    {% for value, label in budget_choices %}
                                    <button type="button" class="choice-card choice-card--compact" :class="form.budget === '{{ value }}' ? 'is-selected' : ''" @click="pickBudget('{{ value }}')">
                                        <span class="choice-card__title">{{ label }}</span>
                                    </button>
                                    {% endfor %}
                                </div>
                            </section>

                            <section x-show="step === 3" x-transition.opacity.duration.250ms class="wizard-panel">
                                <div>
                                    <p class="wizard-panel__eyebrow">Step 3</p>
                                    <h3 class="wizard-panel__title">What timeline are you aiming for?</h3>
                                    <p class="wizard-panel__text">Select a starting point or type a custom timeframe.</p>
                                </div>
                                <div class="choice-grid mt-8">
                                    <button type="button" class="choice-card choice-card--compact" :class="form.timeline === 'As soon as possible' ? 'is-selected' : ''" @click="pickTimeline('As soon as possible')"><span class="choice-card__title">As soon as possible</span></button>
                                    <button type="button" class="choice-card choice-card--compact" :class="form.timeline === 'Within 2–4 weeks' ? 'is-selected' : ''" @click="pickTimeline('Within 2–4 weeks')"><span class="choice-card__title">Within 2–4 weeks</span></button>
                                    <button type="button" class="choice-card choice-card--compact" :class="form.timeline === 'This quarter' ? 'is-selected' : ''" @click="pickTimeline('This quarter')"><span class="choice-card__title">This quarter</span></button>
                                    <button type="button" class="choice-card choice-card--compact" :class="form.timeline === 'Next quarter' ? 'is-selected' : ''" @click="pickTimeline('Next quarter')"><span class="choice-card__title">Next quarter</span></button>
                                    <button type="button" class="choice-card choice-card--compact" :class="form.timeline === 'Flexible' ? 'is-selected' : ''" @click="pickTimeline('Flexible')"><span class="choice-card__title">Flexible</span></button>
                                </div>
                                <div class="mt-6">
                                    <label class="label-field" for="wizard_timeline">Custom timeline</label>
                                    <input id="wizard_timeline" type="text" class="field-control" x-model="form.timeline" placeholder="For example: after funding, next month, or after internal approval">
                                </div>
                            </section>

                            <section x-show="step === 4" x-transition.opacity.duration.250ms class="wizard-panel">
                                <div>
                                    <p class="wizard-panel__eyebrow">Step 4</p>
                                    <h3 class="wizard-panel__title">Who should we reply to?</h3>
                                    <p class="wizard-panel__text">Add the main contact details for the conversation.</p>
                                </div>
                                <div class="mt-8 grid gap-5 md:grid-cols-2">
                                    <div>
                                        <label class="label-field" for="wizard_name">Name *</label>
                                        <input id="wizard_name" type="text" class="field-control" x-model="form.name" placeholder="Your name">
                                        <p class="error-text" x-cloak x-show="serverErrors.name" x-text="serverErrors.name"></p>
                                    </div>
                                    <div>
                                        <label class="label-field" for="wizard_email">Email *</label>
                                        <input id="wizard_email" type="email" class="field-control" x-model="form.email" placeholder="you@company.com">
                                        <p class="error-text" x-cloak x-show="serverErrors.email" x-text="serverErrors.email"></p>
                                    </div>
                                </div>
                            </section>

                            <section x-show="step === 5" x-transition.opacity.duration.250ms class="wizard-panel">
                                <div>
                                    <p class="wizard-panel__eyebrow">Step 5</p>
                                    <h3 class="wizard-panel__title">Add a little business context.</h3>
                                    <p class="wizard-panel__text">These fields are optional, but they help us respond more practically.</p>
                                </div>
                                <div class="mt-8 grid gap-5 md:grid-cols-2">
                                    <div>
                                        <label class="label-field" for="wizard_company">Company</label>
                                        <input id="wizard_company" type="text" class="field-control" x-model="form.company" placeholder="Company or organization">
                                    </div>
                                    <div>
                                        <label class="label-field" for="wizard_phone">Phone</label>
                                        <input id="wizard_phone" type="text" class="field-control" x-model="form.phone" placeholder="+1 555 123 4567">
                                    </div>
                                </div>
                            </section>

                            <section x-show="step === 6" x-transition.opacity.duration.250ms class="wizard-panel">
                                <div>
                                    <p class="wizard-panel__eyebrow">Step 6</p>
                                    <h3 class="wizard-panel__title">What should we know about the project?</h3>
                                    <p class="wizard-panel__text">Share the goal, what needs to be built or improved, and anything that matters for scope.</p>
                                </div>
                                <div class="mt-8">
                                    <label class="label-field" for="wizard_message">Project brief *</label>
                                    <textarea id="wizard_message" rows="7" class="field-control field-control--textarea" x-model="form.message" placeholder="Tell us what you want to build, improve, automate, or launch."></textarea>
                                    <p class="error-text" x-cloak x-show="serverErrors.message" x-text="serverErrors.message"></p>
                                </div>
                            </section>

                            <section x-show="step === 7" x-transition.opacity.duration.250ms class="wizard-panel">
                                <div>
                                    <p class="wizard-panel__eyebrow">Final step</p>
                                    <h3 class="wizard-panel__title">Review and submit.</h3>
                                    <p class="wizard-panel__text">Make sure the summary looks right, then send it through.</p>
                                </div>
                                <div class="wizard-review mt-8 grid gap-4 md:grid-cols-2">
                                    <div class="wizard-review__item"><span class="wizard-review__label">Service</span><span class="wizard-review__value" x-text="readableService"></span></div>
                                    <div class="wizard-review__item"><span class="wizard-review__label">Budget</span><span class="wizard-review__value" x-text="readableBudget"></span></div>
                                    <div class="wizard-review__item"><span class="wizard-review__label">Timeline</span><span class="wizard-review__value" x-text="form.timeline || 'Not specified' "></span></div>
                                    <div class="wizard-review__item"><span class="wizard-review__label">Contact</span><span class="wizard-review__value" x-text="`${form.name || '—'} · ${form.email || '—'}`"></span></div>
                                    <div class="wizard-review__item md:col-span-2"><span class="wizard-review__label">Message</span><span class="wizard-review__value wizard-review__value--block" x-text="form.message || 'No project brief added yet.'"></span></div>
                                </div>
                                <div x-cloak x-show="errorMessage" class="mt-6 rounded-2xl border border-rose-400/20 bg-rose-500/10 px-4 py-3 text-sm text-rose-100" x-text="errorMessage"></div>
                            </section>
                        </div>

                        <div class="wizard-actions">
                            <button type="button" class="button-secondary" x-show="step > 1" x-cloak @click="goBack()">Back</button>
                            <div class="ml-auto flex flex-wrap gap-3">
                                <a href="mailto:{{ contact_email }}" class="button-secondary">Email instead</a>
                                <button type="button" class="button-primary" x-show="step < steps.length" @click="goNext()">Continue</button>
                                <button type="submit" class="button-primary" x-show="step === steps.length" :disabled="submitting" :class="{'opacity-70 cursor-not-allowed': submitting}">
                                    <span x-show="!submitting">Submit project intake</span>
                                    <span x-show="submitting" x-cloak>Submitting…</span>
                                </button>
                            </div>
                        </div>
                    </form>
                </div>

                <div x-cloak x-show="successOpen" class="fixed inset-0 z-[70] flex items-center justify-center bg-slate-950/78 px-5 backdrop-blur-md" @click.self="successOpen = false" @keydown.escape.window="successOpen = false">
                    <div class="success-panel relative w-full max-w-2xl overflow-hidden rounded-[2rem] border border-white/12 bg-slate-950/95 p-7 shadow-glow md:p-8">
                        <div class="absolute right-0 top-0 h-44 w-44 rounded-full bg-accent-400/12 blur-3xl"></div>
                        <button type="button" class="absolute right-5 top-5 inline-flex h-10 w-10 items-center justify-center rounded-full border border-white/10 bg-white/5 text-slate-300 hover:bg-white/10 hover:text-white" @click="successOpen = false" aria-label="Close confirmation panel">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" /></svg>
                        </button>
                        <div class="relative z-10">
                            <div class="icon-chip success-icon mb-5">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" /></svg>
                            </div>
                            <p class="eyebrow">Submission confirmed</p>
                            <h3 class="mt-4 font-display text-3xl font-bold text-white">Your information has been submitted.</h3>
                            <p class="mt-4 max-w-2xl text-base leading-8 text-slate-300" x-text="successMessage"></p>
                            <div class="mt-6 grid gap-3">
                                <template x-for="item in successSteps" :key="item">
                                    <div class="rounded-2xl border border-white/10 bg-white/5 px-4 py-3 text-sm text-slate-200" x-text="item"></div>
                                </template>
                            </div>
                            <div class="mt-8 flex flex-wrap gap-3">
                                <a href="mailto:{{ contact_email }}" class="button-secondary">Email the studio directly</a>
                                <button type="button" class="button-primary" @click="successOpen = false">Close panel</button>
                            </div>
                        </div>
                    </div>
                </div>

                <noscript>
                    <div class="mt-8 rounded-[1.6rem] border border-white/10 bg-slate-950/55 p-5 md:p-6">
                        <p class="text-xs uppercase tracking-[0.22em] text-slate-400">JavaScript fallback</p>
                        <h3 class="mt-3 font-display text-2xl font-semibold text-white">Use the standard enquiry form.</h3>
                        <form method="post" action="{% url 'leads:contact' %}" class="mt-6 grid gap-6 md:grid-cols-2">
                            {% csrf_token %}
                            <input type="hidden" name="referrer" value="">
                            <input type="hidden" name="inquiry_type" value="project">
                            <input type="hidden" name="submission_mode" value="guided">
                            <input type="text" name="website" tabindex="-1" autocomplete="off" class="hidden" aria-hidden="true">
                            <div>
                                <label for="fallback_name" class="label-field">Name *</label>
                                <input id="fallback_name" type="text" name="name" class="field-control" required>
                            </div>
                            <div>
                                <label for="fallback_email" class="label-field">Email *</label>
                                <input id="fallback_email" type="email" name="email" class="field-control" required>
                            </div>
                            <div>
                                <label for="fallback_company" class="label-field">Company</label>
                                <input id="fallback_company" type="text" name="company" class="field-control">
                            </div>
                            <div>
                                <label for="fallback_service_interest" class="label-field">Service interest *</label>
                                <select id="fallback_service_interest" name="service_interest" class="field-control" required>
                                    <option value="">Select a service</option>
                                    {% for value, label in service_choices %}
                                        <option value="{{ value }}">{{ label }}</option>
                                    {% endfor %}
                                </select>
                            </div>
                            <div>
                                <label for="fallback_budget" class="label-field">Budget range</label>
                                <select id="fallback_budget" name="budget" class="field-control">
                                    <option value="">Select a budget range</option>
                                    {% for value, label in budget_choices %}
                                        <option value="{{ value }}">{{ label }}</option>
                                    {% endfor %}
                                </select>
                            </div>
                            <div>
                                <label for="fallback_timeline" class="label-field">Timeline</label>
                                <input id="fallback_timeline" type="text" name="timeline" class="field-control">
                            </div>
                            <div>
                                <label for="fallback_phone" class="label-field">Phone</label>
                                <input id="fallback_phone" type="text" name="phone" class="field-control">
                            </div>
                            <div class="md:col-span-2">
                                <label for="fallback_message" class="label-field">Message *</label>
                                <textarea id="fallback_message" name="message" rows="6" class="field-control field-control--textarea" required></textarea>
                            </div>
                            <div class="md:col-span-2">
                                <button type="submit" class="button-primary">Submit enquiry</button>
                            </div>
                        </form>
                    </div>
                </noscript>
            </div>

            <div class="grid gap-5">
                <article class="surface-card">
                    <p class="eyebrow">What happens next</p>
                    <h2 class="mt-4 font-display text-2xl font-semibold text-white">A clear follow-up sequence, not a black box.</h2>
                    <div class="timeline-list mt-6">
                        <div class="timeline-item">
                            <span class="timeline-item__index">01</span>
                            <div>
                                <h3 class="font-medium text-white">Brief review</h3>
                                <p class="mt-2 text-sm leading-7 text-slate-400">We review the project type, scope, and technical fit across software, websites, automation, and AI.</p>
                            </div>
                        </div>
                        <div class="timeline-item">
                            <span class="timeline-item__index">02</span>
                            <div>
                                <h3 class="font-medium text-white">Practical next-step response</h3>
                                <p class="mt-2 text-sm leading-7 text-slate-400">You get a direct reply with a recommended route, whether that is a discovery call, scoped follow-up, or a clearer implementation starting point.</p>
                            </div>
                        </div>
                        <div class="timeline-item">
                            <span class="timeline-item__index">03</span>
                            <div>
                                <h3 class="font-medium text-white">Scope shaping</h3>
                                <p class="mt-2 text-sm leading-7 text-slate-400">If the fit is right, the studio moves into clearer scoping, system planning, and delivery structure.</p>
                            </div>
                        </div>
                    </div>
                </article>

                <article class="surface-card">
                    <p class="eyebrow">Direct contact</p>
                    <h2 class="mt-4 font-display text-2xl font-semibold text-white">Prefer email or phone?</h2>
                    <div class="mt-6 grid gap-4 text-sm text-slate-300">
                        <a href="mailto:{{ contact_email }}" class="contact-row">{{ contact_email }}</a>
                        <a href="tel:{{ contact_phone }}" class="contact-row">{{ contact_phone }}</a>
                        <div class="contact-row">{{ contact_location }}</div>
                    </div>
                </article>

                <article class="surface-card">
                    <p class="eyebrow">Good fit projects</p>
                    <div class="mt-5 grid gap-3">
                        <div class="contact-tile">
                            <div class="font-medium text-white">Premium websites and conversion-led pages</div>
                            <div class="mt-1 text-sm leading-6 text-slate-400">For businesses that need stronger digital positioning and lead capture.</div>
                        </div>
                        <div class="contact-tile">
                            <div class="font-medium text-white">Custom apps, portals, and internal systems</div>
                            <div class="mt-1 text-sm leading-6 text-slate-400">For recurring workflows that need a better interface and backend logic.</div>
                        </div>
                        <div class="contact-tile">
                            <div class="font-medium text-white">Automation, dashboards, and data pipelines</div>
                            <div class="mt-1 text-sm leading-6 text-slate-400">For operations that need less manual work and more visibility.</div>
                        </div>
                        <div class="contact-tile">
                            <div class="font-medium text-white">Assistants, RAG systems, and speech workflows</div>
                            <div class="mt-1 text-sm leading-6 text-slate-400">For teams that want practical AI capability wrapped in working software.</div>
                        </div>
                    </div>
                </article>
            </div>
        </div>
    </div>
</section>
{% endblock %}


============================================================
FILE: templates/leads/contact_email.html
============================================================
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>New lead</title>
</head>
<body style="margin:0; padding:32px; background:#08111f; color:#e2e8f0; font-family:Inter, Arial, sans-serif;">
    <div style="max-width:680px; margin:0 auto; background:#0f172a; border:1px solid rgba(255,255,255,0.08); border-radius:24px; overflow:hidden;">
        <div style="padding:28px 28px 8px;">
            <p style="margin:0; font-size:12px; letter-spacing:0.22em; text-transform:uppercase; color:#85c0ff;">{{ site_name }}</p>
            <h1 style="margin:16px 0 0; font-size:28px; line-height:1.2; color:#ffffff;">New lead received</h1>
        </div>
        <div style="padding:24px 28px 32px;">
            <table style="width:100%; border-collapse:collapse; font-size:14px; line-height:1.6; color:#cbd5e1;">
                <tr><td style="padding:6px 0; width:170px; color:#94a3b8;">Name</td><td style="padding:6px 0; color:#ffffff;">{{ lead.name }}</td></tr>
                <tr><td style="padding:6px 0; color:#94a3b8;">Email</td><td style="padding:6px 0; color:#ffffff;">{{ lead.email }}</td></tr>
                <tr><td style="padding:6px 0; color:#94a3b8;">Phone</td><td style="padding:6px 0; color:#ffffff;">{{ lead.phone|default:'—' }}</td></tr>
                <tr><td style="padding:6px 0; color:#94a3b8;">Company</td><td style="padding:6px 0; color:#ffffff;">{{ lead.company|default:'—' }}</td></tr>
                <tr><td style="padding:6px 0; color:#94a3b8;">Service interest</td><td style="padding:6px 0; color:#ffffff;">{{ lead.get_service_interest_display }}</td></tr>
                <tr><td style="padding:6px 0; color:#94a3b8;">Budget</td><td style="padding:6px 0; color:#ffffff;">{{ lead.get_budget_display|default:'—' }}</td></tr>
                <tr><td style="padding:6px 0; color:#94a3b8;">Timeline</td><td style="padding:6px 0; color:#ffffff;">{{ lead.timeline|default:'—' }}</td></tr>
                <tr><td style="padding:6px 0; color:#94a3b8;">Inquiry type</td><td style="padding:6px 0; color:#ffffff;">{{ lead.get_inquiry_type_display }}</td></tr>
                <tr><td style="padding:6px 0; color:#94a3b8;">Submitted</td><td style="padding:6px 0; color:#ffffff;">{{ lead.created_at|date:'Y-m-d H:i' }}</td></tr>
            </table>
            <div style="margin-top:24px; border:1px solid rgba(255,255,255,0.08); border-radius:18px; background:rgba(255,255,255,0.03); padding:18px;">
                <p style="margin:0 0 10px; color:#ffffff; font-size:14px; font-weight:700;">Message</p>
                <p style="margin:0; color:#cbd5e1; font-size:14px; line-height:1.7; white-space:pre-line;">{{ lead.message }}</p>
            </div>
        </div>
    </div>
</body>
</html>


============================================================
FILE: templates/leads/contact_email.txt
============================================================
New lead received for {{ site_name }}.

Name: {{ lead.name }}
Email: {{ lead.email }}
Phone: {{ lead.phone|default:'—' }}
Company: {{ lead.company|default:'—' }}
Service interest: {{ lead.get_service_interest_display }}
Budget: {{ lead.get_budget_display|default:'—' }}
Timeline: {{ lead.timeline|default:'—' }}
Inquiry type: {{ lead.get_inquiry_type_display }}
Submitted: {{ lead.created_at|date:'Y-m-d H:i' }}
IP address: {{ lead.ip_address|default:'—' }}

Message:
{{ lead.message }}


============================================================
FILE: templates/leads/dashboard.html
============================================================
{% extends 'base.html' %}

{% block content %}
<section class="section-shell">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="flex flex-col gap-6 lg:flex-row lg:items-end lg:justify-between">
            <div>
                <p class="eyebrow">Internal view</p>
                <h1 class="section-title">Leads dashboard</h1>
                <p class="section-intro">Protected internal list of contact submissions.</p>
            </div>
            <div class="rounded-2xl border border-white/10 bg-slate-950/[0.55] px-4 py-3 text-sm text-slate-300">
                {{ lead_count }} lead{{ lead_count|pluralize }}
            </div>
        </div>

        <div class="mt-8 surface-card">
            <form method="get" class="flex flex-col gap-4 md:flex-row">
                <input type="text" name="q" value="{{ query }}" placeholder="Search leads by name, email, company, phone, or message" class="mt-0 w-full rounded-2xl border border-white/[0.12] bg-slate-950/50 px-4 py-3 text-sm text-slate-100 placeholder:text-slate-500 focus:border-brand-500 focus:outline-none focus:ring-2 focus:ring-brand-500/30">
                <button type="submit" class="button-secondary justify-center">Search</button>
            </form>

            <div class="mt-8 overflow-x-auto">
                <table class="min-w-full divide-y divide-white/10 text-left text-sm">
                    <thead>
                        <tr class="text-slate-400">
                            <th class="pb-4 pr-6 font-medium">Name</th>
                            <th class="pb-4 pr-6 font-medium">Company</th>
                            <th class="pb-4 pr-6 font-medium">Service</th>
                            <th class="pb-4 pr-6 font-medium">Budget</th>
                            <th class="pb-4 pr-6 font-medium">Submitted</th>
                            <th class="pb-4 font-medium">Details</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-white/[0.08] text-slate-300">
                        {% for lead in page_obj %}
                        <tr>
                            <td class="py-5 pr-6 align-top">
                                <div class="font-medium text-white">{{ lead.name }}</div>
                                <a href="mailto:{{ lead.email }}" class="mt-1 block text-slate-400 hover:text-white">{{ lead.email }}</a>
                                {% if lead.phone %}<a href="tel:{{ lead.phone }}" class="mt-1 block text-slate-500 hover:text-white">{{ lead.phone }}</a>{% endif %}
                            </td>
                            <td class="py-5 pr-6 align-top">{{ lead.company|default:'—' }}</td>
                            <td class="py-5 pr-6 align-top">{{ lead.get_service_interest_display }}</td>
                            <td class="py-5 pr-6 align-top">{{ lead.get_budget_display|default:'—' }}</td>
                            <td class="py-5 pr-6 align-top">{{ lead.created_at|date:'M j, Y · H:i' }}</td>
                            <td class="py-5 align-top">
                                <div class="max-w-sm text-slate-400">{{ lead.message|truncatechars:180 }}</div>
                                {% if lead.is_spam %}<span class="mt-2 inline-flex rounded-full border border-rose-400/20 bg-rose-500/10 px-3 py-1 text-xs text-rose-200">Spam flag</span>{% endif %}
                            </td>
                        </tr>
                        {% empty %}
                        <tr>
                            <td colspan="6" class="py-10 text-center text-slate-500">No leads found.</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>

            {% if page_obj.paginator.num_pages > 1 %}
            <div class="mt-6 flex flex-wrap items-center justify-between gap-4 text-sm text-slate-400">
                <p>Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}</p>
                <div class="flex gap-2">
                    {% if page_obj.has_previous %}
                    <a href="?page={{ page_obj.previous_page_number }}{% if query %}&q={{ query }}{% endif %}" class="button-secondary">Previous</a>
                    {% endif %}
                    {% if page_obj.has_next %}
                    <a href="?page={{ page_obj.next_page_number }}{% if query %}&q={{ query }}{% endif %}" class="button-secondary">Next</a>
                    {% endif %}
                </div>
            </div>
            {% endif %}
        </div>
    </div>
</section>
{% endblock %}


============================================================
FILE: templates/robots.txt
============================================================
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /studio/
Sitemap: {{ site_url }}/sitemap.xml

