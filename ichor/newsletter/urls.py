from django.urls import path
from . import views

app_name = 'newsletter'

urlpatterns = [
    path('subscribe', views.index, name='letter-index'),
    path('mail_letter/', views.mail_letter, name='mail-letter'),
    path('unsubscribe/', views.newsletter_unsubscribe, name='unsubscribe')

]