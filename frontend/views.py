from django.shortcuts import render
from blog.models import Blog
from events.models import Events
from utils import http
import datetime

@http.base_data()
def home(request, context): 

    events = Events.objects.filter(time__gte=datetime.datetime.now())
    blogs = Blog.objects.order_by('-id')[:3]
    context['blogs'] = blogs
    context['events'] = events
    
    return render(request, 'home.html', context)


def contacts(request):

    context = {}    

    return render(request, 'base.html', context)