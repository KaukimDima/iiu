from . import views
from django.urls import path

app_name = 'vacancy'

urlpatterns = [
    path('vacancy/', views.home, name='home'),
]
