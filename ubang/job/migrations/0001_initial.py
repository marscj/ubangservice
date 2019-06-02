# Generated by Django 2.2 on 2019-06-01 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('itinerary', models.CharField(max_length=128)),
                ('full_day', models.BooleanField(default=False)),
                ('freedom_day', models.BooleanField(default=False)),
                ('remark', models.CharField(blank=True, max_length=256, null=True)),
                ('checkin_time', models.DateTimeField(blank=True, default=None, null=True)),
                ('checkout_time', models.DateTimeField(blank=True, default=None, null=True)),
                ('checkin_long', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('checkin_lat', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('checkout_long', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('checkout_lat', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('checkin_picture', models.ImageField(blank=True, null=True, upload_to='job/%Y/%m/%d')),
                ('checkout_picture', models.ImageField(blank=True, null=True, upload_to='job/%Y/%m/%d')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job', to='booking.Booking')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
    ]