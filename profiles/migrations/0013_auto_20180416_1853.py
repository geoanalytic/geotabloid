# Generated by Django 2.0.3 on 2018-04-16 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_auto_20180415_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='otherfiles',
            name='size',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='project',
            name='size',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='tag',
            name='size',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='basemap',
            name='size',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='spatialitedbs',
            name='size',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]