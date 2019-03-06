# Generated by Django 2.1.5 on 2019-02-24 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loss', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livestocktype',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='infrastructuretype',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='livestocktype',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]