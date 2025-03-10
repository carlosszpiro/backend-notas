from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
  add_form = CustomUserCreationForm
  form = CustomUserChangeForm
  model = CustomUser
  
  list_display = ("email", "is_superuser", "is_active",)
  list_filter = ("email", "is_superuser", "is_active",)

  fieldsets = (
      (None, {"fields": ("email", "password")}),
      ("Permissões", {"fields": (
          "is_superuser", "is_active", "groups", "user_permissions")}),
  )

  add_fieldsets = (
      (None, {
          "classes": ("wide",),
          "fields": (
              "email", "password1", "password2", "is_superuser",
              "is_active", "groups", "user_permissions"
          )}
       ),
  )

  search_fields = ("email",)
  ordering = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)
