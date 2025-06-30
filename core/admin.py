from django.contrib import admin
from .models import Service, Project, Testimonial, ContactMessage, CompanyInfo, QuoteRequest

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'created_at']
    list_filter = ['category', 'status', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['name', 'comment']
    readonly_fields = ['created_at']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    actions = ['mark_as_read', 'mark_as_unread']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"

    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Mark selected messages as unread"

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'tagline', 'description')
        }),
        ('Contact Information', {
            'fields': ('address', 'phone', 'email')
        }),
        ('Social Media', {
            'fields': ('facebook', 'twitter', 'linkedin', 'instagram')
        }),
        ('Statistics', {
            'fields': ('projects_completed', 'years_experience', 'client_satisfaction')
        }),
    )

    def has_add_permission(self, request):
        # Only allow one company info record
        return not CompanyInfo.objects.exists()

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'project_type', 'budget_range', 'timeline', 'created_at', 'is_processed']
    list_filter = ['project_type', 'budget_range', 'timeline', 'is_processed', 'created_at']
    search_fields = ['name', 'email', 'company', 'project_description', 'location']
    readonly_fields = ['created_at']
    list_editable = ['is_processed']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'email', 'phone', 'company')
        }),
        ('Project Information', {
            'fields': ('project_type', 'project_description', 'location')
        }),
        ('Budget & Timeline', {
            'fields': ('budget_range', 'timeline')
        }),
        ('Additional Information', {
            'fields': ('additional_requirements',)
        }),
        ('Status', {
            'fields': ('is_processed', 'created_at')
        }),
    )
