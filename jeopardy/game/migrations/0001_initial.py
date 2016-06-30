# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('air_date', models.CharField(max_length=10)),
                ('question', models.TextField()),
                ('value', models.IntegerField()),
                ('answer', models.CharField(max_length=255)),
                ('show_number', models.CharField(max_length=6)),
                ('current_round', models.CharField(max_length=50)),
            ],
        ),
    ]