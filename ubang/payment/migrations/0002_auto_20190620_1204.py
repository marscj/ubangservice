# Generated by Django 2.2 on 2019-06-20 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='captured_amount',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='captured_amount_currency',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='extra_data',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='gateway',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='token',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='total',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='total_currency',
        ),
    ]
