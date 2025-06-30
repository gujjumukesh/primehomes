from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('quote-request/', views.quote_request, name='quote_request'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('submit-contact/', views.submit_contact_ajax, name='submit_contact_ajax'),
    path('submit-testimonial/', views.submit_testimonial_ajax, name='submit_testimonial_ajax'),
] 