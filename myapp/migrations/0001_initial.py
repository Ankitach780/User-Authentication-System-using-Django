# Generated by Django 4.2.11 on 2024-03-10 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("firstname", models.CharField(max_length=50)),
                ("lastname", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=50)),
                ("contact", models.CharField(max_length=50)),
                ("password", models.CharField(max_length=50)),
            ],
        ),
    ]