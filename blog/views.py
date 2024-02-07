from django.shortcuts import render
from django.utils import timezone
from .models import Project
from django.core.handlers.wsgi import WSGIRequest
from django.conf import settings
from django.http.response import HttpResponse

def GetPage(fullPath: str) -> str:

    return '/home' if fullPath == '/' else fullPath    

def GetTemplateName(page: str) -> str:

    """
    
    TemplateName is the page path which will be rendered.
    
    """

    if not page.startswith('/'):
        
        page = '/' + page

    return settings.TEMPLATE+page+'.html'

def GetTitle(page: str) -> str:

    try:
        
        if page.startswith('/'):

            page = page[1:]

        return page.replace('_', ' ').title()

    except:

        return 'Home'

def Custom404(request, exception) -> HttpResponse:

    return render(request, GetTemplateName('404'), {'title': settings.TITLE, 'pageTitle': 'Page Not Found !'}, status=404)

def Render(request: WSGIRequest) -> HttpResponse:

    page = GetPage(request.get_full_path())
    projects = Project.objects.all() # Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    return render(request, GetTemplateName(page), {'title': settings.TITLE, 'pageTitle': GetTitle(page), 'aboutSubtitle': settings.ABOUT_SUBTITLE, 'projects': projects, 'TEMPLATE': settings.TEMPLATE})