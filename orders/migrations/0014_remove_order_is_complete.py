# Generated by Django 5.0.6 on 2024-07-03 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_remove_order_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_complete',
        ),
    ]