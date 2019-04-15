# Generated by Django 2.1.5 on 2019-04-10 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_profile', '0041_auto_20190409_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='hdi',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='risk',
            name='remoteness',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='risk',
            name='riskScore',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]