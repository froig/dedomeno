# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0091_auto_20170109_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='warehouse',
            field=models.NullBooleanField(),
        ),
    ]