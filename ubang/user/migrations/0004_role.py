# Generated by Django 2.2 on 2019-05-06 14:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190506_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('user', models.ManyToManyField(blank=True, related_name='roles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
