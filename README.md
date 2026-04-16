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
