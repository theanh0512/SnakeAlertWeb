# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-29 15:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snake',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='snake',
            name='location',
        ),
    ]