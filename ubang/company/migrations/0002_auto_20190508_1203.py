# Generated by Django 2.2 on 2019-05-08 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='discount',
        ),
        migrations.DeleteModel(
            name='Discount',
        ),
    ]
