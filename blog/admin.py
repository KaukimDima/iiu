from django.contrib import admin

from .models import (
    Blog, 
    BlogCategory, 
    Comments
)


admin.site.register([
    Blog, 
    BlogCategory, 
    Comments
])