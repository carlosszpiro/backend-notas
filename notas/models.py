from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import CustomUser


class Nota(models.Model):
  CATEGORIAS = (
      ("PES", "Pessoal"),
      ("COR", "Corporativo"),
      ("EST", "Estudantil"),
      ("OUT", "Outros"),
  )

  titulo = models.CharField(_("Título"), max_length=100)
  conteudo = models.TextField(_("Conteúdo"))

  categoria = models.CharField(
      _("Categoria"), max_length=3, choices=CATEGORIAS)

  usuario = models.ForeignKey(
      CustomUser, on_delete=models.CASCADE, related_name="user")

  criado_em = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.titulo
