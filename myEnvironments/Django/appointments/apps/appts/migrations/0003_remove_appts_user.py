# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-23 19:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appts', '0002_auto_20180223_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appts',
            name='user',
        ),
    ]
