from . import views
from django.urls import path

app_name = 'team'

urlpatterns = [
    path('team/', views.TeamListView.as_view(), name='team')
]