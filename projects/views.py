from django.shortcuts import render
from .models import Project


def index(request):
    projects = Project.objects.all()
    context = { 'projects': projects }

    return render(request, 'projects/index.html', context)

def project(request, slug):
    project = Project.objects.get(slug=slug)
    context = { 'project': project }

    return render(request, 'projects/project_details.html', context)