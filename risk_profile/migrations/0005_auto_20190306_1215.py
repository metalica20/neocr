# Generated by Django 2.1.5 on 2019-03-06 12:15

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_profile', '0004_layertable'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('name', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('district', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('vdc', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('ward', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('wholesale', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('commodity', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('lat', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('long', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, default=None, null=True, srid=4326)),
            ],
        ),
        migrations.AlterField(
            model_name='layertable',
            name='hazard',
            field=models.CharField(choices=[('flood', 'Flood'), ('landslide', 'Landslide'), ('fire', 'Fire'), ('earthquake', 'Earthquake'), ('light', 'Lightening'), ('lights', 'Lightenings')], max_length=35),
        ),
    ]
