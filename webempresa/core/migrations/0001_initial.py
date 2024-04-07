# Generated by Django 4.2.11 on 2024-04-07 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="Título")),
                (
                    "subtitle",
                    models.CharField(max_length=200, verbose_name="Subtítulo"),
                ),
                ("description", models.TextField(verbose_name="Descripción")),
                (
                    "image",
                    models.ImageField(upload_to="services", verbose_name="Imagen"),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de creación"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Fecha de actualización"
                    ),
                ),
            ],
            options={
                "verbose_name": "servicio",
                "verbose_name_plural": "servicios",
                "ordering": ["-created"],
            },
        ),
    ]
