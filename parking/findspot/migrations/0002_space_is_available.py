# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findspot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='space',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]