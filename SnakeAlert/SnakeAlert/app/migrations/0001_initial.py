# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-29 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('specification', models.TextField()),
                ('first_aid', models.TextField()),
                ('image_path', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Snake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.TextField()),
                ('location', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Kind')),
            ],
        ),
    ]