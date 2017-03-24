# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0011_source_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='object_type',
            field=models.CharField(blank=True, choices=[('new construction', 'Obra Nueva'), ('house', 'Vivienda'), ('office', 'Oficina'), ('comercial', 'Locales o Naves'), ('parking', 'Garajes'), ('land', 'Terrenos')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='attic_url',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='comercial_url',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='duplex_url',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='flat_url',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='holliday_url',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='house_url',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='land_url',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='new_construction_url',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='office_url',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='parking_url',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='rent_url',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='rustic_url',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='sale_url',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='sepatator_url',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='share_url',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='conditions',
            field=models.CharField(blank=True, choices=[('good', 'Buena'), ('bad', 'A reformar')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='house_type',
            field=models.CharField(blank=True, choices=[('flat', 'Piso'), ('house', 'Chalet'), ('rustic', 'Rústico'), ('duplex', 'Duplex'), ('attic', 'Ático')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='transaction_type',
            field=models.CharField(choices=[('rent', 'Alquiler'), ('sale', 'Venta'), ('share', 'Compartir'), ('holliday', 'Vacaciones')], max_length=8, null=True),
        ),
    ]