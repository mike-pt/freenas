# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-04-22 04:56
from __future__ import unicode_literals

from django.db import migrations, models
import freenasUI.freeadmin.models.fields


def enable_snmp_zilstat(apps, schema_editor):
    snmp_service = apps.get_model("services", "services").objects.get(srv_service="snmp")
    snmp_settings = apps.get_model("services", "snmp").objects.latest("id")
    if snmp_service.srv_enable:
        snmp_settings.snmp_zilstat = True
        snmp_settings.save()


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0024_add_admin_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='snmp',
            name='snmp_zilstat',
            field=models.BooleanField(default=False, verbose_name='Expose zilstat via SNMP'),
        ),
        migrations.RunPython(
            enable_snmp_zilstat,
        )
    ]
