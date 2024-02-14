from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.core.handlers.wsgi import WSGIRequest
from django.conf import settings
from django.http.response import HttpResponse

from .models import Project
from .forms import ProjectForm
from taggit.models import Tag

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

def Render(request: WSGIRequest, page: str=None, **kwargs) -> HttpResponse:

    page = GetPage(request.get_full_path()) if not page else page
    context = {
        'title': settings.TITLE,
        'pageTitle': GetTitle(page),
        'TEMPLATE': settings.TEMPLATE,
        **kwargs
    }

    return render(request, GetTemplateName(page), context)

def Projects(request: WSGIRequest) -> HttpResponse:

    projects = Project.objects.all() # Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    tags = Project.tags.order_by('slug') #.most_common()[:4]
    
    return Render(request, projects=projects, tags=tags)

def TaggedProjects(request: WSGIRequest, slug):

    tag = get_object_or_404(Tag, slug=slug)
    tags = Project.tags.order_by('slug') #.most_common()[:4]

    projects = Project.objects.filter(tags=tag)
    
    return Render(request, 'projects', projects=projects, tags=tags, currentTag=tag)

def AddProject(request: WSGIRequest) -> HttpResponse:

    projects = Project.objects.all() # Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    commonTags = Project.tags.most_common()[:4],
    
    form = ProjectForm(request.POST)

    if form.is_valid():

        newPro = form.save(commit=False)
    
    return Render(request, 'add_project', form=form, projects=projects)

def ProjectDetail(request: WSGIRequest, slug) -> HttpResponse:

    project = get_object_or_404(Project, slug=slug)
    return Render(request, 'project_detail', pageTitle=project.name, project= project)

def About(request: WSGIRequest) -> HttpResponse:

    return Render(request, aboutSubtitle=settings.ABOUT_SUBTITLE)
