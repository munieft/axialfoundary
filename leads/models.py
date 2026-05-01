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
