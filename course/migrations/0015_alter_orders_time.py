# Generated by Django 4.1.5 on 2023-01-23 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0014_alter_orders_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orders",
            name="time",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]