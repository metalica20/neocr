# Generated by Django 2.1.5 on 2019-03-07 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_profile', '0017_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=550, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=550, null=True),
        ),
    ]
