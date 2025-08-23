from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Service, Project, Testimonial, ContactMessage, CompanyInfo, QuoteRequest
from .forms import ContactForm, TestimonialForm, QuoteRequestForm
import json
from django.utils.text import slugify

def home(request):
    """Home page view"""
    services = Service.objects.all()[:6]
    projects = Project.objects.all()[:6]
    testimonials = Testimonial.objects.all()[:3]
    company_info = CompanyInfo.objects.first()
    
    context = {
        'services': services,
        'projects': projects,
        'testimonials': testimonials,
        'company_info': company_info,
    }
    return render(request, 'core/home.html', context)

def services(request):
    """Services page view"""
    services = Service.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'core/services.html', context)

def projects(request):
    """Projects page view"""
    projects = Project.objects.all()

    # Only include categories that have at least one project
    categories = []
    used = set()
    for project in projects:
        slug = slugify(project.category.lower())
        if slug not in used:
            categories.append((slug, project.category))
            used.add(slug)

    context = {
        'projects': projects,
        'categories': categories,
    }
    return render(request, 'core/projects.html', context)

def about(request):
    """About page view"""
    company_info = CompanyInfo.objects.first()
    context = {
        'company_info': company_info,
    }
    return render(request, 'core/about.html', context)

def contact(request):
    """Contact page view"""
    company_info = CompanyInfo.objects.first()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'company_info': company_info,
    }
    return render(request, 'core/contact.html', context)

def quote_request(request):
    """Quote request page view"""
    company_info = CompanyInfo.objects.first()
    
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your quote request! We will review your project details and get back to you within 24-48 hours.')
            return redirect('quote_request')
    else:
        form = QuoteRequestForm()
    
    context = {
        'form': form,
        'company_info': company_info,
    }
    return render(request, 'core/quote_request.html', context)

def testimonials(request):
    """Testimonials page view"""
    testimonials = Testimonial.objects.all()
    
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your testimonial! It has been submitted successfully.')
            return redirect('testimonials')
    else:
        form = TestimonialForm()
    
    context = {
        'testimonials': testimonials,
        'form': form,
    }
    return render(request, 'core/testimonials.html', context)

@login_required
def admin_dashboard(request):
    """Admin dashboard view"""
    services_count = Service.objects.count()
    projects_count = Project.objects.count()
    messages_count = ContactMessage.objects.filter(is_read=False).count()
    testimonials_count = Testimonial.objects.count()
    
    recent_projects = Project.objects.all()[:5]
    recent_messages = ContactMessage.objects.all()[:5]
    
    context = {
        'services_count': services_count,
        'projects_count': projects_count,
        'messages_count': messages_count,
        'testimonials_count': testimonials_count,
        'recent_projects': recent_projects,
        'recent_messages': recent_messages,
    }
    return render(request, 'core/admin_dashboard.html', context)

@csrf_exempt
def submit_contact_ajax(request):
    """AJAX contact form submission"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            ContactMessage.objects.create(
                name=data['name'],
                email=data['email'],
                phone=data.get('phone', ''),
                subject=data['subject'],
                message=data['message']
            )
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@csrf_exempt
def submit_testimonial_ajax(request):
    """AJAX testimonial form submission"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            Testimonial.objects.create(
                name=data['name'],
                rating=data['rating'],
                comment=data['comment']
            )
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
