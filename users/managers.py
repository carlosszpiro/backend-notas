from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
  def create_user(self, email, password=None, **extra_fields):
    if not email:
      raise ValueError(_("O campo e-mail não pode ser vazio."))

    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save()

    return user

  def create_superuser(self, email, password=None, **extra_fields):
    extra_fields.setdefault("is_superuser", True)

    if not extra_fields.get("is_superuser"):
      raise ValueError(_("Superusuários devem ser 'is_superuser=True'."))

    return self.create_user(email, password, **extra_fields)
