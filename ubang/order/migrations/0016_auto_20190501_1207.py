# Generated by Django 2.2 on 2019-05-01 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_order_apply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='apply',
            new_name='applyId',
        ),
    ]