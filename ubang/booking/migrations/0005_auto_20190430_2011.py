# Generated by Django 2.2 on 2019-04-30 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20190430_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='discount_name',
            field=models.CharField(default='no discount', max_length=128),
        ),
    ]