from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import UserCreationForm, UserChangeForm
from utils import http
from .models import User
from django.contrib.auth.decorators import login_required

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
@login_required(login_url='/accounts/login/')
def profile(request, context): 

    instance = get_object_or_404(User, id=request.user.id)
    form = UserChangeForm(request.POST or None, instance=instance)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

    context['form'] = form
    return render(request, 'profile.html', context)
    