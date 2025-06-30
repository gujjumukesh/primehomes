from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, help_text="FontAwesome icon class (e.g., fas fa-home)")
    color = models.CharField(max_length=7, default='#0d6efd', help_text="Hex color code")
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
        ('Industrial', 'Industrial'),
        ('Landscaping', 'Landscaping'),
        ('Interior Design', 'Interior Design'),
    ]
    
    STATUS_CHOICES = [
        ('Planning', 'Planning'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='In Progress')
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def category_code(self):
        """Generate a consistent slug for the category"""
        return slugify(self.category.lower())

    class Meta:
        ordering = ['-created_at']

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating} stars"

    class Meta:
        ordering = ['-created_at']

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']

class QuoteRequest(models.Model):
    PROJECT_TYPE_CHOICES = [
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
        ('Industrial', 'Industrial'),
        ('Renovation', 'Renovation'),
        ('Landscaping', 'Landscaping'),
        ('Interior Design', 'Interior Design'),
        ('Other', 'Other'),
    ]
    
    BUDGET_RANGE_CHOICES = [
        ('Under $50k', 'Under $50,000'),
        ('$50k-$100k', '$50,000 - $100,000'),
        ('$100k-$250k', '$100,000 - $250,000'),
        ('$250k-$500k', '$250,000 - $500,000'),
        ('$500k-$1M', '$500,000 - $1,000,000'),
        ('Over $1M', 'Over $1,000,000'),
    ]
    
    TIMELINE_CHOICES = [
        ('Immediate', 'Immediate (Within 1 month)'),
        ('1-3 months', '1-3 months'),
        ('3-6 months', '3-6 months'),
        ('6-12 months', '6-12 months'),
        ('Over 1 year', 'Over 1 year'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=200, blank=True)
    project_type = models.CharField(max_length=50, choices=PROJECT_TYPE_CHOICES)
    project_description = models.TextField()
    budget_range = models.CharField(max_length=20, choices=BUDGET_RANGE_CHOICES)
    timeline = models.CharField(max_length=20, choices=TIMELINE_CHOICES)
    location = models.CharField(max_length=200)
    additional_requirements = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.project_type} Project"

    class Meta:
        ordering = ['-created_at']

class CompanyInfo(models.Model):
    name = models.CharField(max_length=200, default="PrimeHomes Constructions")
    tagline = models.CharField(max_length=300, default="Building Your Dreams Into Reality")
    description = models.TextField(default="With over 15 years of experience in the construction industry, PrimeHomes Constructions has established itself as a trusted name in building excellence.")
    address = models.TextField(default="123 Construction Ave, Building City, BC 12345")
    phone = models.CharField(max_length=20, default="(555) 123-4567")
    email = models.EmailField(default="info@primehomes.com")
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    projects_completed = models.IntegerField(default=500)
    years_experience = models.IntegerField(default=15)
    client_satisfaction = models.IntegerField(default=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Company Info"
