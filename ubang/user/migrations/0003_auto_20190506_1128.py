# Generated by Django 2.2 on 2019-05-06 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customuser_is_actived'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='photo',
            new_name='avatar',
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default='', max_length=128),
        ),
    ]
