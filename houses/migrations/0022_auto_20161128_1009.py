# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0021_auto_20161128_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='agency',
        ),
        migrations.AddField(
            model_name='house',
            name='agency',
            field=models.ManyToManyField(blank=True, help_text='If blank there is not an agency involved', null=True, to='houses.Agency'),
        ),
        migrations.RemoveField(
            model_name='house',
            name='source',
        ),
        migrations.AddField(
            model_name='house',
            name='source',
            field=models.ManyToManyField(blank=True, null=True, to='houses.Source'),
        ),
    ]