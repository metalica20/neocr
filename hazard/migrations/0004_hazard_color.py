# Generated by Django 2.1.5 on 2019-03-19 15:42

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hazard', '0003_remove_hazard_style'),
    ]

    operations = [
        migrations.AddField(
            model_name='hazard',
            name='color',
            field=colorfield.fields.ColorField(blank=True, default=None, max_length=18, null=True),
        ),
    ]