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
