# Generated by Django 2.2 on 2019-05-08 13:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_auto_20190501_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='change_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]