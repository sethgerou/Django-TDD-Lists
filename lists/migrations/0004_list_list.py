# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='list',
            field=models.TextField(default=''),
        ),
    ]
