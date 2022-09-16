from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Team
# Create your views here.

class TeamListView(ListView):
    model=Team
    template_name = 'team/team.html'
    queryset=Team.objects.all()
    context_object_name='team'
