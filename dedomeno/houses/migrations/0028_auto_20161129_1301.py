# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0027_urlsourceterritory_url_source_territory_name_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='transaction_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_transition_house', to='houses.Transaction'),
        ),
        migrations.RemoveField(
            model_name='territorialentity',
            name='near_brothers',
        ),
        migrations.AddField(
            model_name='territorialentity',
            name='near_brothers',
            field=models.ManyToManyField(blank=True, null=True, related_name='_territorialentity_near_brothers_+', to='houses.TerritorialEntity'),
        ),
    ]