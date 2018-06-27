# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-01 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0003_auto_20180228_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='mov_descript',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='mov_director',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='mov_img',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='mov_release',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='mov_title',
        ),
        migrations.AddField(
            model_name='movie',
            name='mov_id',
            field=models.IntegerField(default=-3),
            preserve_default=False,
        ),
    ]