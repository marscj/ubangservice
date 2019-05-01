# Generated by Django 2.2 on 2019-04-30 17:13

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0011_auto_20190430_1713'),
        ('vehicle', '0002_auto_20190428_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookingId', models.CharField(editable=False, max_length=64, unique=True)),
                ('arrival_time', models.DateTimeField()),
                ('departure_time', models.DateTimeField()),
                ('pick_up_addr', models.CharField(blank=True, max_length=128, null=True, verbose_name='Pick up address')),
                ('drop_off_addr', models.CharField(blank=True, max_length=128, null=True, verbose_name='Drop off address')),
                ('contact_name', models.CharField(max_length=64)),
                ('contact_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('remark', models.TextField(blank=True, max_length=256, null=True)),
                ('discount_name', models.CharField(max_length=128)),
                ('discount_value', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=3)),
                ('company_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booking', to='company.Company', verbose_name='Company')),
                ('create_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booking_customer', to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
                ('guide', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booking_guide', to=settings.AUTH_USER_MODEL)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booking', to='vehicle.Vehicle')),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Bookings',
            },
        ),
    ]
