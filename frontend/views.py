from django.shortcuts import render
from blog.models import Blog
from .models import ContactDetail
from events.models import Events
from django.contrib.auth.decorators import login_required
from utils import http
import datetime

@http.base_data()
def home(request, context): 

    events = Events.objects.filter(time__gte=datetime.datetime.now())
    blogs = Blog.objects.order_by('-id')[:3]
    context['blogs'] = blogs
    context['events'] = events
    context['register'] if request.GET.get('register') else None
    return render(request, 'home.html', context)

@http.base_data()
def contacts(request, context):

    contact_details = ContactDetail.objects.all()
    context['contact_details'] = contact_details


    return render(request, 'contacts.html', context)
