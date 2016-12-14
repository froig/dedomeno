# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0006_auto_20161123_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='conditions',
            field=models.CharField(blank=True, choices=[('good', 'good'), ('bad', 'bad')], max_length=4),
        ),
        migrations.AlterField(
            model_name='house',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]