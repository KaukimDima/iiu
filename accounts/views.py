from django.shortcuts import render, HttpResponseRedirect
from .forms import UserCreationForm, UserProfileForm
from utils import http

@http.base_data()
def register(request, context):
    
    form = UserCreationForm(request.POST or None)
    context['form'] = form
    context['register'] = True
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return http.custom_redirect('login', register=1)
    return render(request, 'register_user.html', context)

@http.base_data()
def profile(request, context): 

    data = {
        'email' : request.user.email,
        'surname' : request.user.surname,
        'name' : request.user.name,
        'patronymic' : request.user.patronymic,
        'phone' : request.user.phone,
    }
    form = UserProfileForm(initial=data)
    context['form'] = form
    return render(request, 'profile.html', context)