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
