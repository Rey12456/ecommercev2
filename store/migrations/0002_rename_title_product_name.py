# Generated by Django 4.2 on 2023-05-30 19:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="title",
            new_name="name",
        ),
    ]
