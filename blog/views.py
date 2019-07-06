from django.shortcuts import render
from .models import (
    BlogCategory, 
    Blog,
    Comments
)
from utils import http
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


@http.base_data()
@login_required(login_url='/accounts/login/')
def home(request, context, slug=None):

    categories = BlogCategory.objects.all()
    
    try:
        category = categories.first() if not slug else categories.get(slug=slug)
    except: 
        return render(request, 'page_404.html', context)

    blogs = Blog.objects.filter(category=category).order_by('-id')

    context.update({
        'category' : category,
        'categories' : categories,
        'blogs' : blogs
    })


    return render(request, 'blog.html', context)

@http.base_data()
@login_required(login_url='/accounts/login/')
def detail(request, context, slug, post_slug):

    try:
        blog = Blog.objects.get(slug=post_slug)
    except:
        return render(request, 'page_404.html', context)
    
    blog_prev = Blog.objects.filter(id__lt=blog.id).order_by('-id').first()
    blog_next = Blog.objects.filter(id__gt=blog.id).order_by('id').first()
    
    context.update({
        'blog_prev' : blog_prev,
        'blog_next' : blog_next,
        'blog' : blog,
    })

    form = CommentForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
    comments = Comments.objects.filter(blog=blog).order_by('-id')
    context['form'] = form
    context['comments'] = comments
    context['comments_count'] = comments.count()

    return render(request, 'blog_detail.html', context)
    