from rest_framework import serializers

from .models import Nota


class NotaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Nota
    fields = ["id", "titulo", "conteudo", "categoria", "usuario", "criado_em",]
    read_only_fields = ["id", "usuario", "criado_em",]
