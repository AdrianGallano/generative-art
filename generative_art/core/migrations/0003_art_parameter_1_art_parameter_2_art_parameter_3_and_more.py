# Generated by Django 5.0.4 on 2024-04-09 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_art_description_art_max_color_cycle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='parameter_1',
            field=models.IntegerField(default=14),
        ),
        migrations.AddField(
            model_name='art',
            name='parameter_2',
            field=models.IntegerField(default=14),
        ),
        migrations.AddField(
            model_name='art',
            name='parameter_3',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='art',
            name='parameter_4',
            field=models.IntegerField(default=24),
        ),
        migrations.AddField(
            model_name='art',
            name='parameter_5',
            field=models.IntegerField(default=54),
        ),
    ]