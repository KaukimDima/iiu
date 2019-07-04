from django.contrib import admin
from .models import (
    Advantage,
    Contacts,
    Social, 
)

admin.site.register([
    Advantage, Contacts, Social
])
