from django import forms
from django.forms import widgets
from django.forms.models import ModelForm
from home.models import DonorRequest, BankRequest
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget
# from localflavor.in.forms import INStateSelect




class ContactForm(forms.Form):
    name = forms.CharField(max_length = 150)
    company =forms.CharField(max_length=200)
    email_address = forms.EmailField(max_length = 150)
    phone = forms.CharField(max_length=10)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)

        
         
class DonorForm(forms.ModelForm):
    
    class Meta:
        model = DonorRequest
        fields = ['full_name', 'email_id', 'date_of_birth', 'phone','state', 'city', 'pin_code', 'blood_group','I_agree_to_the_terms_and_conditions_stated_below']
        widgets = {
            'full_name': forms.TextInput(attrs = {'class':'form-control'}),
            #'city': INStateSelect(attrs=None),
            #'state': forms.TextInput(attrs = {'class':'form-control'}),
            'pin_code': forms.NumberInput(attrs = {'class':'form-control'}),
            'phone': forms.TextInput(attrs = {'class':'form-control'}),
            'date_of_birth':forms.DateInput(format = '%Y-%m-%d', attrs={'type': 'date'}),
            'email_id': forms.EmailInput(attrs = {'class':'form-control'}),
            #'weight': forms.NumberInput(attrs = {'class':'form-control', 'placeholder':'Body weight'}),
        }
        
         
class BankForm(forms.ModelForm):
    
    class Meta:
        model = BankRequest
        fields = '__all__'
        widgets = {
            'bloodbank_name': forms.TextInput(attrs = {'class':'form-control'}),
            #'city': INStateSelect(attrs=None),
            #'state': forms.TextInput(attrs = {'class':'form-control'}),
            'pin_code': forms.NumberInput(attrs = {'class':'form-control'}),
            'phone': forms.TextInput(attrs = {'class':'form-control'}),
            'email_id': forms.EmailInput(attrs = {'class':'form-control'}),
            #'weight': forms.NumberInput(attrs = {'class':'form-control', 'placeholder':'Body weight'}),
        }
        
        
        
    
class ContactForm(forms.Form):
    name = forms.CharField(max_length = 150)
    company =forms.CharField(max_length=200)
    email_address = forms.EmailField(max_length = 150)
    phone = forms.CharField(max_length=10)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)

        