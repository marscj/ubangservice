# Generated by Django 2.2 on 2019-06-20 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20190620_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='currency',
            field=models.CharField(choices=[('AED', 'AED')], default='AED', max_length=10),
        ),
    ]
