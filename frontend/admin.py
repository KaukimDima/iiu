from django.contrib import admin
from .models import (
    Advantage,
    Contacts,
    Social, 
    ContactDetail
)

admin.site.register([
    Advantage, Contacts, Social, ContactDetail
])
