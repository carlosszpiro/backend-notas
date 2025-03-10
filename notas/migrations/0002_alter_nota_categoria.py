# Generated by Django 4.2 on 2025-03-09 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notas", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nota",
            name="categoria",
            field=models.CharField(
                choices=[
                    ("PES", "Pessoal"),
                    ("COR", "Corporativo"),
                    ("EST", "Estudantil"),
                    ("OUT", "Outros"),
                ],
                max_length=3,
                verbose_name="Categoria",
            ),
        ),
    ]
