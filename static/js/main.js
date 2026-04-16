(function () {
    const THEME_KEY = 'axial-theme';

    function currentTheme() {
        return document.documentElement.getAttribute('data-theme') || 'dark';
    }

    function applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        try {
            localStorage.setItem(THEME_KEY, theme);
        } catch (error) {}

        const meta = document.querySelector('meta[name="theme-color"]');
        if (meta) meta.setAttribute('content', theme === 'light' ? '#eef5fb' : '#08111f');

        document.querySelectorAll('[data-theme-toggle]').forEach((button) => {
            const nextTheme = theme === 'dark' ? 'light' : 'dark';
            button.setAttribute('aria-label', `Switch to ${nextTheme} mode`);
            button.setAttribute('aria-checked', theme === 'light' ? 'true' : 'false');
            button.dataset.themeState = theme;
            const label = button.querySelector('[data-theme-label]');
            if (label) label.textContent = theme === 'light' ? 'Light' : 'Dark';
        });

        window.dispatchEvent(new CustomEvent('axial-theme-change', { detail: { theme } }));
    }

    function initThemeToggle() {
        let storedTheme = null;
        try { storedTheme = localStorage.getItem(THEME_KEY); } catch (error) {}
        applyTheme(storedTheme || currentTheme());
        document.querySelectorAll('[data-theme-toggle]').forEach((button) => {
            button.addEventListener('click', () => applyTheme(currentTheme() === 'dark' ? 'light' : 'dark'));
        });
    }

    function initAnimatedBackground() {
        const canvas = document.querySelector('[data-animated-bg]');
        if (!canvas) return;
        const context = canvas.getContext('2d');
        if (!context) return;

        const prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        let width = 0;
        let height = 0;
        let nodes = [];
        let animationFrame = null;

        function palette() {
            return currentTheme() === 'light'
                ? {
                    dot: 'rgba(24,112,248,0.16)',
                    line: 'rgba(24,112,248,0.08)',
                    glowA: 'rgba(71,153,255,0.10)',
                    glowB: 'rgba(78,231,194,0.08)',
                }
                : {
                    dot: 'rgba(78,231,194,0.26)',
                    line: 'rgba(71,153,255,0.10)',
                    glowA: 'rgba(24,112,248,0.10)',
                    glowB: 'rgba(78,231,194,0.08)',
                };
        }

        function resize() {
            width = window.innerWidth;
            height = window.innerHeight;
            const ratio = Math.min(window.devicePixelRatio || 1, 1.5);
            canvas.width = Math.floor(width * ratio);
            canvas.height = Math.floor(height * ratio);
            canvas.style.width = width + 'px';
            canvas.style.height = height + 'px';
            context.setTransform(ratio, 0, 0, ratio, 0, 0);
            const count = Math.max(20, Math.min(36, Math.floor((width * height) / 56000)));
            nodes = Array.from({ length: count }, () => ({
                x: Math.random() * width,
                y: Math.random() * height,
                vx: (Math.random() - 0.5) * 0.18,
                vy: (Math.random() - 0.5) * 0.18,
                r: Math.random() * 1.8 + 0.8,
            }));
        }

        function renderFrame() {
            const colors = palette();
            context.clearRect(0, 0, width, height);

            const glowA = context.createRadialGradient(width * 0.2, height * 0.18, 0, width * 0.2, height * 0.18, width * 0.34);
            glowA.addColorStop(0, colors.glowA);
            glowA.addColorStop(1, 'rgba(0,0,0,0)');
            context.fillStyle = glowA;
            context.fillRect(0, 0, width, height);

            const glowB = context.createRadialGradient(width * 0.82, height * 0.8, 0, width * 0.82, height * 0.8, width * 0.28);
            glowB.addColorStop(0, colors.glowB);
            glowB.addColorStop(1, 'rgba(0,0,0,0)');
            context.fillStyle = glowB;
            context.fillRect(0, 0, width, height);

            nodes.forEach((node) => {
                node.x += node.vx;
                node.y += node.vy;
                if (node.x < -16) node.x = width + 16;
                if (node.x > width + 16) node.x = -16;
                if (node.y < -16) node.y = height + 16;
                if (node.y > height + 16) node.y = -16;
            });

            for (let i = 0; i < nodes.length; i += 1) {
                for (let j = i + 1; j < nodes.length; j += 1) {
                    const a = nodes[i];
                    const b = nodes[j];
                    const distance = Math.hypot(a.x - b.x, a.y - b.y);
                    if (distance < 148) {
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

            if (!prefersReducedMotion) animationFrame = window.requestAnimationFrame(renderFrame);
        }

        resize();
        renderFrame();
        window.addEventListener('resize', resize);
        window.addEventListener('axial-theme-change', () => {
            if (animationFrame) window.cancelAnimationFrame(animationFrame);
            resize();
            renderFrame();
        });
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
            element.addEventListener('pointerleave', () => element.classList.remove('is-active'));
        });
    }

    function initMediaCarousels() {
        const prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        document.querySelectorAll('[data-media-carousel]').forEach((carousel) => {
            const slides = Array.from(carousel.querySelectorAll('[data-carousel-slide]'));
            if (!slides.length) return;
            const dots = Array.from(carousel.querySelectorAll('[data-carousel-dot]'));
            const jumps = Array.from(carousel.querySelectorAll('[data-carousel-jump]'));
            const nextButton = carousel.querySelector('[data-carousel-next]');
            const prevButton = carousel.querySelector('[data-carousel-prev]');
            const interval = Number.parseInt(carousel.dataset.interval || '5600', 10);
            let activeIndex = Math.max(0, slides.findIndex((slide) => slide.classList.contains('is-active')));
            let timer = null;
            let touchStartX = 0;

            function show(index) {
                activeIndex = (index + slides.length) % slides.length;
                slides.forEach((slide, slideIndex) => {
                    const active = slideIndex === activeIndex;
                    slide.classList.toggle('is-active', active);
                    slide.hidden = !active;
                    slide.setAttribute('aria-hidden', active ? 'false' : 'true');
                });
                dots.forEach((dot, dotIndex) => dot.classList.toggle('is-active', dotIndex === activeIndex));
                jumps.forEach((jump, jumpIndex) => jump.classList.toggle('is-active', jumpIndex === activeIndex));
            }

            function stopTimer() {
                if (timer) {
                    window.clearInterval(timer);
                    timer = null;
                }
            }

            function startTimer() {
                stopTimer();
                if (prefersReducedMotion || slides.length <= 1) return;
                timer = window.setInterval(() => show(activeIndex + 1), interval);
            }

            slides.forEach((slide, idx) => {
                slide.hidden = idx !== activeIndex;
                slide.setAttribute('aria-hidden', idx === activeIndex ? 'false' : 'true');
            });
            dots.forEach((dot, idx) => dot.classList.toggle('is-active', idx === activeIndex));
            jumps.forEach((jump, idx) => jump.classList.toggle('is-active', idx === activeIndex));

            dots.forEach((dot, idx) => dot.addEventListener('click', () => { show(idx); startTimer(); }));
            jumps.forEach((jump, idx) => jump.addEventListener('click', () => { show(idx); startTimer(); }));
            if (nextButton) nextButton.addEventListener('click', () => { show(activeIndex + 1); startTimer(); });
            if (prevButton) prevButton.addEventListener('click', () => { show(activeIndex - 1); startTimer(); });

            carousel.addEventListener('mouseenter', stopTimer);
            carousel.addEventListener('mouseleave', startTimer);
            carousel.addEventListener('touchstart', (event) => {
                if (event.touches && event.touches[0]) touchStartX = event.touches[0].clientX;
            }, { passive: true });
            carousel.addEventListener('touchend', (event) => {
                if (!(event.changedTouches && event.changedTouches[0])) return;
                const deltaX = event.changedTouches[0].clientX - touchStartX;
                if (Math.abs(deltaX) < 36) return;
                show(deltaX < 0 ? activeIndex + 1 : activeIndex - 1);
                startTimer();
            }, { passive: true });

            startTimer();
        });
    }

    function initReveals() {
        const revealTargets = Array.from(document.querySelectorAll('[data-reveal], .surface-card, .section-title, .section-intro, .confirmation-inline-panel'));
        revealTargets.forEach((element, index) => {
            element.classList.add('reveal-ready');
            element.style.transitionDelay = `${Math.min(index % 6, 5) * 45}ms`;
        });
        if ('IntersectionObserver' in window) {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-visible');
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.12, rootMargin: '0px 0px -5% 0px' });
            revealTargets.forEach((element) => observer.observe(element));
        } else {
            revealTargets.forEach((element) => element.classList.add('is-visible'));
        }
    }

    function syncReferrerFields() {
        document.querySelectorAll('[data-referrer-field]').forEach((field) => {
            if (document.referrer) field.value = document.referrer;
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
                { index: 1, label: 'Service', hint: 'Choose the main service fit' },
                { index: 2, label: 'Budget', hint: 'Set a commercial range' },
                { index: 3, label: 'Timeline', hint: 'Define delivery timing' },
                { index: 4, label: 'Contact', hint: 'Add who we should reply to' },
                { index: 5, label: 'Company', hint: 'Optional business context' },
                { index: 6, label: 'Brief', hint: 'Describe the project clearly' },
                { index: 7, label: 'Review', hint: 'Check and submit' },
            ],
            form: {
                inquiry_type: 'project', service_interest: '', budget: '', timeline: '', name: '', email: '', company: '', phone: '', message: '',
            },
            serviceLabels: {
                'ai-strategy': 'AI Strategy', 'ai-chatbot': 'AI Chatbot / Assistant', 'rag-knowledge': 'RAG / Knowledge Assistant', 'llm-fine-tuning': 'LLM Fine-tuning',
                'speech-ai': 'Speech AI', 'website-development': 'Website Development', 'web-application-development': 'Web Application Development',
                'automation-backend-systems': 'Automation / Backend Systems', 'data-pipelines-scraping': 'Data Pipelines / Scraping', 'product-mvp-build': 'Product / MVP Build',
                'research-collaboration': 'Research Collaboration', other: 'Other',
            },
            budgetLabels: {
                'under-3000': 'Under $3,000', '3000-10000': '$3,000 – $10,000', '10000-25000': '$10,000 – $25,000', '25000-plus': '$25,000+', discuss: "Let's discuss",
            },
            get progress() { return (this.step / this.steps.length) * 100; },
            get currentStep() { return this.steps[this.step - 1] || this.steps[0]; },
            get readableService() { return this.serviceLabels[this.form.service_interest] || 'Not selected'; },
            get readableBudget() { return this.budgetLabels[this.form.budget] || 'Not specified'; },
            clearError(name) {
                if (this.serverErrors[name]) {
                    delete this.serverErrors[name];
                    this.serverErrors = { ...this.serverErrors };
                }
            },
            pickService(value) { this.form.service_interest = value; this.clearError('service_interest'); this.errorMessage = ''; setTimeout(() => this.goNext(), 90); },
            pickBudget(value) { this.form.budget = value; this.clearError('budget'); this.errorMessage = ''; setTimeout(() => this.goNext(), 90); },
            pickTimeline(value) { this.form.timeline = value; this.clearError('timeline'); this.errorMessage = ''; setTimeout(() => this.goNext(), 90); },
            goTo(index) {
                if (index < this.step) { this.step = index; return; }
                for (let current = this.step; current < index; current += 1) { if (!this.validateStep(current)) return; }
                this.step = index;
            },
            goNext() { if (this.validateStep(this.step)) this.step = Math.min(this.step + 1, this.steps.length); },
            goBack() { this.step = Math.max(this.step - 1, 1); },
            validateEmail(value) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value); },
            focusById(id) { const target = document.getElementById(id); if (target) target.focus({ preventScroll: false }); },
            validateStep(index) {
                const name = (this.form.name || '').trim();
                const email = (this.form.email || '').trim();
                const message = (this.form.message || '').trim();
                if (index === 1 && !this.form.service_interest) {
                    this.serverErrors = { ...this.serverErrors, service_interest: 'Please choose the closest service fit.' };
                    return false;
                }
                if (index === 4) {
                    if (name.length < 2) { this.serverErrors = { ...this.serverErrors, name: 'Please enter a valid name.' }; this.focusById('wizard_name'); return false; }
                    if (!this.validateEmail(email)) { this.serverErrors = { ...this.serverErrors, email: 'Please enter a valid email address.' }; this.focusById('wizard_email'); return false; }
                }
                if (index === 6 && message.length < 20) {
                    this.serverErrors = { ...this.serverErrors, message: 'Please share a little more detail so we can respond usefully.' }; this.focusById('wizard_message'); return false;
                }
                return true;
            },
            validateBeforeSubmit() {
                for (let i = 1; i <= this.steps.length; i += 1) {
                    if (!this.validateStep(i)) { this.step = i; return false; }
                }
                return true;
            },
            syncReferrers(formElement) {
                formElement.querySelectorAll('[data-referrer-field]').forEach((field) => { if (document.referrer) field.value = document.referrer; });
            },
            applyServerErrors(errors = {}) {
                this.serverErrors = errors;
                const firstField = Object.keys(errors)[0];
                if (!firstField) return;
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
                if (!this.validateBeforeSubmit()) return;
                this.submitting = true;
                try {
                    const response = await fetch(formElement.action || window.location.pathname, {
                        method: 'POST',
                        headers: { Accept: 'application/json', 'X-Requested-With': 'XMLHttpRequest' },
                        credentials: 'same-origin',
                        body: new FormData(formElement),
                    });
                    const payload = await response.json();
                    if (!response.ok || !payload.ok) {
                        this.errorMessage = payload.message || 'Please review the highlighted fields and try again.';
                        this.applyServerErrors(payload.errors || {});
                        return;
                    }
                    this.form = { inquiry_type: 'project', service_interest: '', budget: '', timeline: '', name: '', email: '', company: '', phone: '', message: '' };
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
        syncReferrerFields();
        initPointerGlow();
        initMediaCarousels();
        initReveals();
    });
}());
