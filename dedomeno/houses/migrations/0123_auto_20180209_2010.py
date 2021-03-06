# Generated by Django 2.0.1 on 2018-02-09 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0122_auto_20180209_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='address_geocode',
        ),
        migrations.AddField(
            model_name='property',
            name='geocode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='property', to='houses.TerritorialEntity'),
        ),
        migrations.AddField(
            model_name='property',
            name='geocode_raw',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='territorialentity',
            name='depth',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='geocode',
            field=models.ManyToManyField(to='houses.TerritorialEntity'),
        ),
    ]
