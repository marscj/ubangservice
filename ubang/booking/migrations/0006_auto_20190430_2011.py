# Generated by Django 2.2 on 2019-04-30 20:11

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20190430_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='discount_name',
            field=models.CharField(blank=True, default='no discount', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='discount_value',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=3, null=True),
        ),
    ]
