# Generated by Django 2.2 on 2019-05-22 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0024_auto_20190522_0918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itinerary',
            old_name='gross_price',
            new_name='charge',
        ),
        migrations.RemoveField(
            model_name='itinerary',
            name='cost_price',
        ),
    ]
