# Generated by Django 2.2 on 2019-04-20 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('itinerary', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0002_order_customer'),
        ('task', '0001_initial'),
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='guide',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='itinerary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task', to='itinerary.Itinerary'),
        ),
        migrations.AddField(
            model_name='task',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task', to='order.Order'),
        ),
        migrations.AddField(
            model_name='task',
            name='vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task', to='vehicle.Vehicle'),
        ),
    ]
