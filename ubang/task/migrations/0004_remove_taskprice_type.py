# Generated by Django 2.2 on 2019-04-24 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20190424_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskprice',
            name='type',
        ),
    ]
