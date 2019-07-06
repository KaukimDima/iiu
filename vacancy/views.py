from django.shortcuts import render
from .models import Vacancy 
from utils import http
from django.contrib.auth.decorators import login_required
from django.urls import reverse 


@http.base_data()
@login_required(login_url='/accounts/login/')
def home(request, context):
    
    vacancies = Vacancy.objects.all().order_by('-id')
    context['vacancies']=  vacancies
    print()
    return render(request, 'vacancy.html', context)


@http.base_data()
@login_required(login_url='/accounts/login/')
def detail(request, context, slug):
    
    try:
        vacancy = Vacancy.objects.get(slug=slug)
    except:
        return render(request, 'page_404.html', context)


    vacancy_prev = Vacancy.objects.filter(id__lt=vacancy.id).order_by('-id').first()
    vacancy_next = Vacancy.objects.filter(id__gt=vacancy.id).order_by('id').first()
    context.update({
        'vacancy' : vacancy,
        'vacancy_prev' : vacancy_prev,
        'vacancy_next' : vacancy_next,
    })
    
    return render(request, 'vacancy_detail.html', context)