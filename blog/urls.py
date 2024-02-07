from django.urls import path
from . import views

urlpatterns = [

    path('', views.Render, name='Render'),
    path('home', views.Render, name='Render'),
    path('projects', views.Render, name='Render'),
    path('useful_links', views.Render, name='Render'),
    path('about', views.Render, name='Render'),

]