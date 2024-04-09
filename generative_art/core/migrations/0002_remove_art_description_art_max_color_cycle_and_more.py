# Generated by Django 5.0.4 on 2024-04-09 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='art',
            name='description',
        ),
        migrations.AddField(
            model_name='art',
            name='max_color_cycle',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='art',
            name='no_of_circles',
            field=models.IntegerField(default=100000),
        ),
        migrations.AddField(
            model_name='art',
            name='resolution_height',
            field=models.IntegerField(default=500),
        ),
        migrations.AddField(
            model_name='art',
            name='resolution_width',
            field=models.IntegerField(default=500),
        ),
    ]
