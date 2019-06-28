# Generated by Django 2.2 on 2019-06-28 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='booking',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='booking.Booking'),
        ),
    ]