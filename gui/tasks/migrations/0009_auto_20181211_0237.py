# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-11 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_auto_20180826_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='smarttest',
            name='smarttest_all_disks',
            field=models.BooleanField(default=False, help_text='Use this SMART test for all disks', verbose_name='All Disks'),
        ),
    ]
