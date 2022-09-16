from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import BloodRequest, DonorRequest, cities, states, BankRequest
# from django_summernote.admin import SummernoteModelAdmin

class BloodRequestAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display=('blood_request_id','time_stamp', 'hospital_initials', 'blood_group', 'status',)
    list_filter = ('blood_group', 'blood_type', 'time_stamp')
    # summernote_fields = ('note',)
    prepopulated_fields = {'slug': ('hospital_initials',)}  

admin.site.register(BloodRequest, BloodRequestAdmin)


class DonorRequestAdmin(admin.ModelAdmin):
    list_display=('full_name', 'phone','city' ,'blood_group')
    list_filter=('blood_group','city', 'state', )
    formfield_overrides = {
        DonorRequest.date_of_birth: {'input_formats': ('%d/%m/%Y',)},
    }
    search_fields=('blood_group', 'city','state', 'pin_code', 'full_name')
    
admin.site.register(DonorRequest, DonorRequestAdmin)
    

class BankRequestAdmin(admin.ModelAdmin):
    list_display=('bloodbank_name', 'phone','city' )
    list_filter=('city', 'state', )
    formfield_overrides = {
        DonorRequest.date_of_birth: {'input_formats': ('%d/%m/%Y',)},
    }
    search_fields=('city','state', 'pin_code', 'contact_name')
    
admin.site.register(BankRequest, BankRequestAdmin)
    



class citiesAdmin(admin.ModelAdmin):
    list_display=['city_name']
    search_fields=['city_name']

admin.site.register(cities, citiesAdmin)

class statesAdmin(admin.ModelAdmin):
    list_display=['name']
    search_fields=['name']

admin.site.register(states, statesAdmin)
