from django.shortcuts import render
from django.utils import timezone
from .models import Post, Project
from django.core.handlers.wsgi import WSGIRequest
from django.conf import settings

def GetTemplateName(page: str):

    """
    
    TemplateName is the page path which will be rendered.
    
    """

    if not page.startswith('/'):
        
        page = '/' + page

    return settings.TEMPLATE+page+'.html'

def GetTitle(page: str):

    try:
        
        if page.startswith('/'):

            page = page[1:]

        return page.replace('_', ' ').title()

    except:

        return 'Home'

def post_list(request: WSGIRequest):

    fullPath = request.get_full_path()
    page = '/home' if fullPath == '/' else fullPath

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    projects = Project.objects.all()
    
    return render(request, GetTemplateName(page), {'title': settings.TITLE, 'pageTitle': GetTitle(page), 'aboutSubtitle': settings.ABOUT_SUBTITLE, 'projects': projects})

def Custom404(request, exception):

    return render(request, GetTemplateName('404'), {'title': settings.TITLE, 'pageTitle': 'Page Not Found !'}, status=404)