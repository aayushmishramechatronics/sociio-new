from . import views
from django.urls import path

app_name = 'home'

urlpatterns = [
    
    path('sociio/', views.base, name='sociio'),
    path('', views.home, name='home'),
    path('donate/', views.BloodListView.as_view(), name='donate'),
    path('search-blood/', views.BloodSearchView.as_view(), name='search-blood'),
    path('donate/detail/<slug:name_slug>/', views.detail_view , name='details'),
    path('register/individual/', views.donor_form, name='donor'),
    path('register/NGO/', views.bank_form, name='bank-donor'),
    path('blood-donation-guidelines/', views.guidelines, name='guidelines'),
    path('register/', views.preform, name='preform'),
    path('contactus/', views.contactus, name = 'contact'),

]
