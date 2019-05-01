# Generated by Django 2.2 on 2019-04-30 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20190429_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='drop_off_addr',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Drop off address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pick_up_addr',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Pick up address'),
        ),
    ]
