# Generated by Django 2.2 on 2019-04-30 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_auto_20190430_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='bookingId',
            field=models.CharField(editable=False, max_length=64),
        ),
    ]
