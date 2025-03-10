from django.contrib import admin

from .models import Nota


class NotaAdmin(admin.ModelAdmin):
  list_display = ("titulo", "usuario", "criado_em",)
  model = Nota


admin.site.register(Nota, NotaAdmin)
