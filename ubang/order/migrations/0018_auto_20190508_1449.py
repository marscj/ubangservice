# Generated by Django 2.2 on 2019-05-08 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0017_order_change_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'Open'), (1, 'Padding'), (2, 'Cancel'), (3, 'Complete'), (4, 'Delete')], default=0),
        ),
    ]
