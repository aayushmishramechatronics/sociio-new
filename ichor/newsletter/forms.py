from django import forms
from . models import Subscribers, MailMessage


class SubscibersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['email', ]

        def clean_email(self):
            email = self.cleaned_data.get('email')

            return email


    

class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = '__all__'