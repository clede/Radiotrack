# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radiotracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='channel',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='program',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
