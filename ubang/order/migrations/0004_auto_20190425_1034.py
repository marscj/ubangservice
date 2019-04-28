# Generated by Django 2.2 on 2019-04-25 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20190424_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderId',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='vehicle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='vehicle.Vehicle'),
        ),
    ]