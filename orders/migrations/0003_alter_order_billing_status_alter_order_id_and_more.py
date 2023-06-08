# Generated by Django 4.2 on 2023-06-04 19:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0002_remove_order_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="billing_status",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]