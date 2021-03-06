# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 17:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0095_auto_20170109_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commercial',
            fields=[
                ('property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='houses.Property')),
                ('transfer_price', models.IntegerField(blank=True, null=True)),
                ('m2_total', models.IntegerField(blank=True, null=True)),
                ('m2_to_use', models.IntegerField(blank=True, null=True)),
                ('m2_terrain', models.IntegerField(blank=True, null=True)),
                ('num_of_floors', models.IntegerField(blank=True, null=True)),
                ('distribution', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('corner', models.NullBooleanField()),
                ('show_windows', models.IntegerField(blank=True, null=True)),
                ('last_activity', models.CharField(blank=True, max_length=200, null=True)),
                ('preservation', models.CharField(blank=True, max_length=100, null=True)),
                ('wc', models.IntegerField(blank=True, null=True)),
                ('floor_num', models.CharField(blank=True, max_length=200, null=True)),
                ('facade', models.CharField(blank=True, max_length=200, null=True)),
                ('air_conditioning', models.NullBooleanField()),
                ('alarm_system', models.NullBooleanField()),
                ('store_room', models.NullBooleanField()),
                ('heating', models.NullBooleanField()),
                ('kitchen', models.NullBooleanField()),
                ('security_door', models.NullBooleanField()),
                ('smoke_extractor', models.NullBooleanField()),
            ],
            bases=('houses.property',),
        ),
        migrations.RenameField(
            model_name='office',
            old_name='warehouse',
            new_name='store_room',
        ),
    ]
