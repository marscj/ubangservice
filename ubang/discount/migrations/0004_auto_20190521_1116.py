# Generated by Django 2.2 on 2019-05-21 11:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0003_auto_20190508_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
