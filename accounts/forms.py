from django import forms
from django.utils import timezone
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import *

from django.utils.safestring import mark_safe


# class PictureWidget(forms.widgets.Widget):
#     def render(self, name, value, attrs=None):
#         html = Template("""<img src="$link"/>""")
#         return mark_safe(html.substitute(link=value)


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'name', 'surname', 'patronymic', 'phone')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

# class UserProfilePasswordForm(forms.ModelForm):

#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=False)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput, required=False)
#     password3 = forms.CharField(label='Current password', widget=forms.PasswordInput, required=False)
 
#     class Meta:
#         model = User
#         fields = ('')

#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2

#     def clean_password3(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password3")
#         return password3

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user
        

# class UserProfile(models.Model):
   

#     email = forms.CharField(widget=forms.TextInput, required=False)
#     name = forms.CharField(widget=forms.TextInput, required=False)
#     surname = forms.CharField(widget=forms.TextInput, required=False)
#     patronymic = forms.CharField(widget=forms.TextInput, required=False)
#     phone = forms.CharField(widget=forms.TextInput, required=False)

#     class Meta:
#         model = User
#         fields = ('email', 'name', 'surname', 'patronymic', 'phone')



class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    # password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'name', 'surname', 'patronymic', 'phone',)

    # def clean_password(self):
    #     return self.initial["password"]


# class UserRegisterForm(forms.ModelForm):

