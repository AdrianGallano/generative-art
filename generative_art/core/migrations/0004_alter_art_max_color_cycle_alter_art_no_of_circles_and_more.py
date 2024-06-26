# Generated by Django 4.2.11 on 2024-04-10 11:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_art_parameter_1_art_parameter_2_art_parameter_3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='max_color_cycle',
            field=models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4000000)]),
        ),
        migrations.AlterField(
            model_name='art',
            name='no_of_circles',
            field=models.IntegerField(default=1000000, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4000000)]),
        ),
        migrations.AlterField(
            model_name='art',
            name='parameter_1',
            field=models.IntegerField(default=14, validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='art',
            name='parameter_2',
            field=models.IntegerField(default=14, validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='art',
            name='parameter_3',
            field=models.IntegerField(default=20, validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='art',
            name='parameter_4',
            field=models.IntegerField(default=24, validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='art',
            name='parameter_5',
            field=models.IntegerField(default=54, validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='art',
            name='resolution_height',
            field=models.IntegerField(default=500, validators=[django.core.validators.MinValueValidator(20), django.core.validators.MaxValueValidator(4000)]),
        ),
        migrations.AlterField(
            model_name='art',
            name='resolution_width',
            field=models.IntegerField(default=500, validators=[django.core.validators.MinValueValidator(20), django.core.validators.MaxValueValidator(4000)]),
        ),
    ]
