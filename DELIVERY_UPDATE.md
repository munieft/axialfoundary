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
