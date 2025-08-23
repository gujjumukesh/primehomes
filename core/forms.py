from django import forms
from .models import ContactMessage, Testimonial, QuoteRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number (Optional)'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Your Message'}),
        }

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'rating', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'rating': forms.Select(attrs={'class': 'form-control'}, choices=[(i, f"{'★' * i} ({i} stars)") for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Share your experience with us...'}),
        }

class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ['name', 'email', 'phone', 'company', 'project_type', 'project_description', 'budget_range', 'timeline', 'location', 'additional_requirements']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name *'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email Address *'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number *'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name (Optional)'}),
            'project_type': forms.Select(attrs={'class': 'form-control'}),
            'project_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Please describe your project in detail *'}),
            'budget_range': forms.Select(attrs={'class': 'form-control'}),
            'timeline': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Location *'}),
            'additional_requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Any additional requirements or special considerations (Optional)'}),
        } 