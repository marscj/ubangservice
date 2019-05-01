# Generated by Django 2.2 on 2019-04-24 13:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0002_auto_20190422_1659'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='task',
            unique_together=set(),
            # unique_together={('day', 'guide'), ('day', 'vehicle')},
        ),
        migrations.RemoveField(
            model_name='task',
            name='end_datetime',
        ),
        migrations.RemoveField(
            model_name='task',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='task',
            name='is_fullday',
        ),
        migrations.RemoveField(
            model_name='task',
            name='start_datetime',
        ),
        migrations.RemoveField(
            model_name='task',
            name='start_time',
        ),
    ]
