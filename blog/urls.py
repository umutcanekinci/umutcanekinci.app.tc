from django.urls import path
from . import views

urlpatterns = [

    path('', views.post_list, name='post_list'),
    path('home', views.post_list, name='post_list'),
    path('projects', views.post_list, name='post_list'),
    path('useful_links', views.post_list, name='post_list'),
    path('about', views.post_list, name='post_list'),

]