from django.contrib import admin
from .models import Post, Project

admin.site.register([Post, Project])