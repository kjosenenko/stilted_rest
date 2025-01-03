from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile
from .forms import CustomUserCreationForm, CustomUserChangeForm

class UserProfileInline(admin.StackedInline):  # new
    model = UserProfile
    can_delete = False
    verbose_name_plural = "User Profile"

class CustomUserAdmin(UserAdmin):
  add_form = CustomUserCreationForm
  form = CustomUserChangeForm
  model = CustomUser
  list_display = [
    "email",
    "username",
  ]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
