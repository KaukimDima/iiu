from . import views
from django.urls import path

app_name = 'fronted'

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
]
