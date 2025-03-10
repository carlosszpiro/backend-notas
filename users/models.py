from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(_("Endereço de e-mail"), unique=True)

  ##################################
  ### --- PERMISSÕES PADRÕES --- ###
  ##################################
  is_active = models.BooleanField(_("Usuário ativo"), default=True)
  is_superuser = models.BooleanField(_("Superusuário"), default=False)

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = []

  objects = CustomUserManager()

  @property
  def is_staff(self):
    return self.is_superuser

  class Meta:
    db_table = "users"
    verbose_name = "Usuário"
    verbose_name_plural = "Usuários"

  def __str__(self):
    return self.email
