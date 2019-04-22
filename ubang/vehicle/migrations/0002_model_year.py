# Generated by Django 2.2 on 2019-04-21 17:53

from django.db import migrations, models
import ubang.vehicle.models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='year',
            field=models.IntegerField(choices=[(2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019)], default=ubang.vehicle.models.current_year),
        ),
    ]
