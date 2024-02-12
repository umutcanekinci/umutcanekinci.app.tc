from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):

    list_display = ('name', 'body',)
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register([Project])