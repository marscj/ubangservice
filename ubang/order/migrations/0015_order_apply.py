# Generated by Django 2.2 on 2019-05-01 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_auto_20190501_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='apply',
            field=models.CharField(blank=True, editable=False, max_length=64, null=True),
        ),
    ]
