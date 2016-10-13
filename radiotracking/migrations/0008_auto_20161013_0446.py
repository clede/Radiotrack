# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radiotracking', '0007_program_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='location',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='station',
            name='freq',
            field=models.CharField(blank=True, default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='station',
            name='stream_url',
            field=models.URLField(blank=True, default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='station',
            name='website',
            field=models.URLField(blank=True, default='', max_length=300),
        ),
    ]
