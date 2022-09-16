from django.contrib import admin
from .models import Blog, BlogContent
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class BlogContentAdmin(admin.StackedInline):
    model = BlogContent

class BlogAdmin(admin.ModelAdmin):
    list_display = ('author', 'publish_date', 'title')
    list_filter = ('title', 'author')
    prepopulated_fields={'slug':('title',)}
    inlines = [BlogContentAdmin]
    

@admin.register(BlogContent)
class BlogContentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, BlogAdmin)