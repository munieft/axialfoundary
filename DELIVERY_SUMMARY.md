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
