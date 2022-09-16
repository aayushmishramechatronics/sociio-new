from django.contrib import admin
from .models import Team
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ('first_name','position')
    search_fields = ['first_name', 'position']
    
    
admin.site.register(Team, TeamAdmin) 
