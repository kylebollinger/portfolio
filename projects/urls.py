from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='projects'),
    path('<str:slug>', views.project, name='project'),
]