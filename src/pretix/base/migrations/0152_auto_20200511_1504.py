# Generated by Django 3.0.5 on 2020-05-11 15:04

import django.db.models.deletion
import django_countries.fields
from django.db import migrations, models

import pretix.helpers.countries


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0151_auto_20200421_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='checkins', to='pretixbase.Device'),
        ),
        migrations.AddField(
            model_name='checkin',
            name='forced',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checkin',
            name='type',
            field=models.CharField(default='entry', max_length=100),
        ),
        migrations.AddField(
            model_name='checkinlist',
            name='allow_entry_after_exit',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='checkinlist',
            name='allow_multiple_entries',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checkinlist',
            name='rules',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterUniqueTogether(
            name='checkin',
            unique_together=set(),
        ),
    ]
