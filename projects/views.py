from django.shortcuts import render
from .models import Project, Gallery


def index(request):
    projects = Project.objects.all().order_by('year').values()
    context = { 'projects': projects }

    return render(request, 'projects/index.html', context)

def project(request, slug):
    project = Project.objects.get(slug=slug)
    galleries = Gallery.objects.filter(project_id=project.id)
    context = { 'project': project, 'galleries': galleries }

    return render(request, 'projects/project_details.html', context)