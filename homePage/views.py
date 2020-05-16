from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Skill, Experience, Project


# Create your views here.
def index(request):
    skills_list = Skill.objects.order_by('name')
    project_list = Project.objects.order_by('name')
    experience_list = Experience.objects.order_by('-start_date')

    context = {
        'skills_list': skills_list,
        'project_list': project_list,
        'experience_list': experience_list
    }

    return render(request, 'homePage/index.html', context)
