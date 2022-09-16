from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('blog/', views.BlogList.as_view(), name='blog-list'),
    path('blog/<slug:slug>/', views.detail_view, name='blog-detail')
]