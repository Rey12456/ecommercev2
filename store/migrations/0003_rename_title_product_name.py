# Generated by Django 4.2 on 2023-05-16 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_author_product_manufacturer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
    ]
