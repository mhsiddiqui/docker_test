# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-23 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='test',
            field=models.BooleanField(default=True),
        ),
    ]