# Generated by Django 3.2.8 on 2024-10-31 19:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("postafacil", "0004_remove_city_cep"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="client",
            name="state",
        ),
    ]
