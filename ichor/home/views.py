
from re import template
import re
from django.db.models import query
from django.db.models.query import RawQuerySet
from django.shortcuts import render, redirect
from .models import BloodRequest, DonorRequest, STATUS_DRAFT
from django.views.generic import ListView, DetailView
from django.views import generic
from django.shortcuts import render,get_object_or_404
from .forms import ContactForm, BankForm
from django.template import RequestContext


from django.core.mail import send_mail, BadHeaderError
from .models import STATUS_PUBLISH, STATUS_DRAFT
from home.forms import DonorForm
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.
def base(request):
    return render(request, 'home/base.html')


    
def guidelines(request):
    return render(request, 'home/guidelines.html')


def home(request):
    return render(request, 'home/home.html')
def preform(request):
    return render(request, 'home/preform.html')

def error_404(request, exception):
        data = {}
        return render(request,'home/404.html', data)

def error_500(request, *args):
        data = {}
        return render(request,'home/500.html', data)


class BloodListView(ListView):
    model=BloodRequest
    template_name = 'home/request.html'
    queryset=BloodRequest.objects.filter(status=STATUS_PUBLISH).order_by('-time_stamp')
    context_object_name='blood'
     

class BloodSearchView(ListView):
    model=BloodRequest
    template_name='home/request.html'
    context_object_name='blood'
    
    def get_queryset(self):
        query=self.request.GET.get('q')
        return BloodRequest.objects.filter(blood_group__icontains=query, status=STATUS_PUBLISH)
    

class BloodDetailView(DetailView):
    model = BloodRequest
    template_name = 'home/request.html'
    
    
def detail_view(request, name_slug):
    blood = get_object_or_404(BloodRequest.objects.filter(status=STATUS_PUBLISH), slug=name_slug)
    return render(request, 'home/detail.html', {'blood':blood,})


def donor_form(request):
    form = DonorForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home:donor_confirm')
    context = {'form':form}
        
    return render(request, 'home/donor.html', context)

def bank_form(request):
    bank_form = BankForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        bank_form = BankForm(request.POST)
        if bank_form.is_valid():
            bank_form.save()
            return redirect ('home:bank_confirm')
    context = {'bank_form':bank_form}
        
    return render(request, 'home/bank_donor.html', context)


def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Subject Inquiry"
            body = {
                'name': form.cleaned_data['name'], 
			    'company': form.cleaned_data['company'], 
			    'email': form.cleaned_data['email_address'], 
			    'message':form.cleaned_data['message'], 
			    'phone':form.cleaned_data['phone'], 
       
                }
            message = "\n".join(body.values())
            recepient = str(form['email_address'].value())

            try:
                send_mail(subject, message, recepient, ['sociio.organisation@gmail.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("home:donate")
    
    form = ContactForm(request.POST)
    return render(request, "home/contactus.html", {'contact_form':form})
