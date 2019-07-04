from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('blog/', views.home, name='home'),
    path('blog/<slug:slug>/', views.home, name='filter'),
    path('blog/<slug:slug>/<slug:post_slug>', views.detail, name='detail'),
]
