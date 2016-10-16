# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-15 07:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('radiotracking', '0009_auto_20161013_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radiotracking.Station'),
        ),
    ]