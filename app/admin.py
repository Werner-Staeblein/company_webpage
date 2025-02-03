from django.contrib import admin
from app.models import (
    GeneralInfo, 
    Service, 
    Testimonial, 
    FrequentlyAskedQuestion, 
    ContactFormLog, 
    Blog,
    Author
)

# Register your models here.

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = [
        'company_name',
        'location',
        'email',
        'phone',
        'open_hours'
    ]
    
@admin.register(Service)

class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
    ]
    
    search_fields = [
        "title"
    ]
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'user_job_title',
        'display_rating_count',
    ]

    def display_rating_count(self, obj):
        return '*' * obj.rating_count
    
    display_rating_count.short_description = "Rating"
    
    
@admin.register(FrequentlyAskedQuestion)
class FAQAdmin(admin.ModelAdmin):
    list_display = [
        'question',
        'answer',
    ]
    
@admin.register(ContactFormLog)
class ContactFormLogAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'is_success',
        'is_error',
        'action_time',        
    ]
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'category',
        'author',
        'title',
        'blog_image',
        'created_at',
    ]
    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name'
    ]