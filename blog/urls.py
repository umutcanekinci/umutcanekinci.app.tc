from django.urls import path
from . import views

urlpatterns = [

    path('', views.Render, name='base_root'),
    path('home', views.Render, name='home'),

    path('projects', views.Projects, name='projects'),
    path('projects/<slug:slug>/', views.ProjectDetail, name='project_detail'),
    path('projects/tag/<slug:slug>/', views.TaggedProjects, name='projects_tagged'),
    path('projects/add_project', views.AddProject, name='project_new'),

    path('useful_links', views.Render, name='useful_links'),
    path('about', views.About, name='about'),
    
    

]