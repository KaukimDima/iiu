from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import *



class RolesInline(admin.StackedInline):
    model = UserRole
    extra = 0
class RolesInline(admin.StackedInline):
    model = UserRole
    extra = 0


class UserAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'name', 'surname', 'patronymic','phone', 'is_admin', 'is_enabled')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Личные данные', {'fields': ('name', 'surname', 'patronymic','phone')}),
        ('Активен', {'fields': ('is_enabled',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    inlines = [
    ]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


class ActionInline(admin.StackedInline):
    model = RoleAction
    extra = 0



class RoleAdmin(admin.ModelAdmin):
    inlines = [ActionInline]


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

admin.site.register(Role, RoleAdmin)
