# Generated by Django 2.2 on 2019-05-21 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0021_order_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='change_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='create_at',
        ),
    ]
