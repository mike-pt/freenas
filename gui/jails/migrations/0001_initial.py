# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-27 21:43


from django.db import migrations, models
import freenasUI.freeadmin.models.fields
from freenasUI import choices


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jail_host', models.CharField(max_length=120, verbose_name='Jail Name')),
                ('jail_type', models.CharField(max_length=120, verbose_name='Type')),
                ('jail_ipv4', models.CharField(blank=True, max_length=120, null=True, verbose_name='IPv4 address')),
                ('jail_ipv4_netmask', models.CharField(blank=True, choices=choices.v4NetmaskBitList, default='', max_length=3, verbose_name='IPv4 netmask')),
                ('jail_alias_ipv4', models.CharField(blank=True, max_length=120, null=True, verbose_name='IPv4 aliases')),
                ('jail_bridge_ipv4', models.CharField(blank=True, max_length=120, null=True, verbose_name='IPv4 bridge address')),
                ('jail_bridge_ipv4_netmask', models.CharField(blank=True, choices=choices.v4NetmaskBitList, default='', max_length=3, verbose_name='IPv4 bridge netmask')),
                ('jail_alias_bridge_ipv4', models.CharField(blank=True, max_length=120, null=True, verbose_name='IPv4 bridge aliases')),
                ('jail_defaultrouter_ipv4', models.GenericIPAddressField(blank=True, null=True, protocol='IPv4', verbose_name='IPv4 default gateway')),
                ('jail_ipv6', models.CharField(blank=True, max_length=120, null=True, verbose_name='IPv6 address')),
                ('jail_ipv6_prefix', models.CharField(blank=True, choices=choices.v6NetmaskBitList, default='', max_length=4, verbose_name='IPv6 prefix length')),
                ('jail_alias_ipv6', models.CharField(blank=True, max_length=120, null=True, verbose_name='IPv6 aliases')),
                ('jail_bridge_ipv6', models.CharField(blank=True, max_length=120, null=True, verbose_name='IPv6 bridge address')),
                ('jail_bridge_ipv6_prefix', models.CharField(blank=True, choices=choices.v6NetmaskBitList, default='', max_length=4, verbose_name='IPv6 bridge prefix length')),
                ('jail_alias_bridge_ipv6', models.CharField(blank=True, max_length=120, null=True, verbose_name='IPv6 bridge aliases')),
                ('jail_defaultrouter_ipv6', models.GenericIPAddressField(blank=True, null=True, protocol='IPv6', verbose_name='IPv6 default gateway')),
                ('jail_mac', models.CharField(blank=True, max_length=120, null=True, verbose_name='MAC')),
                ('jail_iface', models.CharField(blank=True, choices=choices.NICChoices(exclude_configured=False), default='', max_length=300, verbose_name='NIC')),
                ('jail_flags', models.TextField(blank=True, help_text="Comma delimited list of sysctl's", verbose_name='Sysctls')),
                ('jail_autostart', models.BooleanField(default=True, max_length=120, verbose_name='Autostart')),
                ('jail_status', models.CharField(max_length=120, verbose_name='Status')),
                ('jail_vnet', models.BooleanField(default=True, max_length=120, verbose_name='VIMAGE')),
                ('jail_nat', models.BooleanField(default=False, verbose_name='NAT')),
            ],
            options={
                'verbose_name': 'Jail',
                'verbose_name_plural': 'Jails',
            },
        ),
        migrations.CreateModel(
            name='JailMountPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jail', models.CharField(max_length=120, verbose_name='Jail')),
                ('source', models.CharField(max_length=300, verbose_name='Source')),
                ('destination', models.CharField(max_length=300, verbose_name='Destination')),
                ('readonly', models.BooleanField(default=False, verbose_name='Read-Only')),
            ],
            options={
                'verbose_name': 'Storage',
                'verbose_name_plural': 'Storage',
            },
        ),
        migrations.CreateModel(
            name='JailsConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jc_path', models.CharField(help_text='Path where to store jail data', max_length=1024, verbose_name='Jail Root')),
                ('jc_ipv4_dhcp', models.BooleanField(default=False, help_text='When enabled, use DHCP to obtain IPv4 address as well as default router, etc.', verbose_name='IPv4 DHCP')),
                ('jc_ipv4_network', freenasUI.freeadmin.models.fields.Network4Field(blank=True, help_text='IPv4 network range for jails and plugins', max_length=18, null=True, verbose_name='IPv4 Network')),
                ('jc_ipv4_network_start', freenasUI.freeadmin.models.fields.Network4Field(blank=True, help_text='IPv4 network start address for jails and plugins', max_length=18, null=True, verbose_name='IPv4 Network Start Address')),
                ('jc_ipv4_network_end', freenasUI.freeadmin.models.fields.Network4Field(blank=True, help_text='IPv4 network end address for jails and plugins', max_length=18, null=True, verbose_name='IPv4 Network End Address')),
                ('jc_ipv6_autoconf', models.BooleanField(default=False, help_text='When enabled, automatically configurate IPv6 address via rtsol(8).', verbose_name='IPv6 Autoconfigure')),
                ('jc_ipv6_network', freenasUI.freeadmin.models.fields.Network6Field(blank=True, help_text='IPv6 network range for jails and plugins', max_length=43, null=True, verbose_name='IPv6 Network')),
                ('jc_ipv6_network_start', freenasUI.freeadmin.models.fields.Network6Field(blank=True, help_text='IPv6 network start address for jails and plugins', max_length=43, null=True, verbose_name='IPv6 Network Start Address')),
                ('jc_ipv6_network_end', freenasUI.freeadmin.models.fields.Network6Field(blank=True, help_text='IPv6 network end address for jails and plugins', max_length=43, null=True, verbose_name='IPv6 Network End Address')),
                ('jc_collectionurl', models.CharField(blank=True, help_text='URL for the jails index', max_length=255, verbose_name='Collection URL')),
            ],
            options={
                'verbose_name': 'Jails Configuration',
                'verbose_name_plural': 'Jails Configuration',
            },
        ),
        migrations.CreateModel(
            name='JailTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jt_name', models.CharField(max_length=120, unique=True, verbose_name='Name')),
                ('jt_os', models.CharField(choices=choices.JAIL_TEMPLATE_OS_CHOICES, max_length=120, verbose_name='OS')),
                ('jt_arch', models.CharField(choices=choices.JAIL_TEMPLATE_ARCH_CHOICES, max_length=120, verbose_name='Architecture')),
                ('jt_url', models.CharField(max_length=255, verbose_name='URL')),
                ('jt_mtree', models.CharField(blank=True, help_text='The mtree file for the template', max_length=255, verbose_name='mtree')),
                ('jt_system', models.BooleanField(default=False, help_text='If this is a system template, it will not be visible in the UI and will only be used internally.', verbose_name='System')),
                ('jt_readonly', models.BooleanField(default=False, verbose_name='Read-only')),
            ],
            options={
                'verbose_name': 'Jail Template',
                'verbose_name_plural': 'Jail Templates',
            },
        ),
    ]
