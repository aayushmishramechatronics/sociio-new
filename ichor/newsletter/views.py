from django.shortcuts import render, redirect
from . forms import SubscibersForm, MailMessageForm
from . models import Subscribers
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = SubscibersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription Successful')
            return redirect('newsletter:letter-index')
    else:
        form = SubscibersForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/letter.html', context)

@login_required
def mail_letter(request):
    emails = Subscribers.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    print(mail_list)
    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            send_mail(
                subject,
                message,
                '',
                mail_list,
                fail_silently=False,
            )
            messages.success(request, 'Message has been sent to the Mail List')
            return redirect('newsletter:mail-letter')
    else:
        form = MailMessageForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/mail_letter.html', context)

def newsletter_unsubscribe(request):
    form = SubscibersForm(request.POST or None)
    emailx=''
    if request.method =='POST':


        emailx=request.POST['email']
    
    if Subscribers.objects.filter(email=emailx).exists():
        Subscribers.objects.filter(email=emailx).delete()
        
    else:
        print('no email found')
            
    context= {
                'form':form
            }
    template='newsletter/unsub.html'
    return render(request, template, context)

