# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findspot', '0005_auto_20170407_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='space',
            name='booked_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
