# Generated by Django 2.2 on 2019-05-08 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_auto_20190501_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='order.Order'),
        ),
    ]
