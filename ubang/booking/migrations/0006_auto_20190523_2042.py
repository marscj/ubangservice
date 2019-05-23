# Generated by Django 2.2 on 2019-05-23 20:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20190523_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='comment',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='guide_score',
            field=models.FloatField(default=5.0, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AddField(
            model_name='booking',
            name='is_comment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='vehicle_score',
            field=models.FloatField(default=5.0, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Created', 'Created'), ('Cancel', 'Cancel'), ('Delete', 'Delete'), ('Complete', 'Complete')], default='Created', max_length=16),
        ),
    ]
