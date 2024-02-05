from django.shortcuts import render
from django.utils import timezone
from .models import Post, Project
from django.core.handlers.wsgi import WSGIRequest
TITLE = "Umutcan Ekinci"
SUBTITLE = "Software Engineer"
TEMPLATE = 'default'

def post_list(request: WSGIRequest):
    
    fullPath = request.get_full_path()
    page = '/home' if fullPath == '/' else fullPath

    try:
        
        pageTitle = page.replace('_', ' ').title()

        if pageTitle.startswith('/'):

            pageTitle = pageTitle[1:]

    except:

        pageTitle = 'Home'

    path = TEMPLATE+page+'.html'

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    projects = Project.objects.all()
    
    return render(request, path, {'title': TITLE, 'subtitle': SUBTITLE, 'page': pageTitle, 'projects': projects})
