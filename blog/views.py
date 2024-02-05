from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.core.handlers.wsgi import WSGIRequest
TITLE = "Umutcan Ekinci"
SUBTITLE = "Software Engineer"
TEMPLATE = 'default'

def post_list(request: WSGIRequest):
    
    fullPath = request.get_full_path()
    path = TEMPLATE+'/'+'home.html' if fullPath == '/' else TEMPLATE+'/'+fullPath+'.html'
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, path, {'title': TITLE, 'subtitle': SUBTITLE, 'page': fullPath.capitalize()})
