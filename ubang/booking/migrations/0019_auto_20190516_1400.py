# Generated by Django 2.2 on 2019-05-16 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0018_auto_20190508_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Darft', 'darf'), ('Confirm', 'confirm'), ('Cancel', 'cancel'), ('Delete', 'delete')], default='Darft', max_length=16),
        ),
    ]
