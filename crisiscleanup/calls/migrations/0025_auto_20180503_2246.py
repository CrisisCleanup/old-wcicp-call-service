# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-03 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0024_Replace user join tables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='call_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='call',
            name='call_type',
            field=models.CharField(choices=[('INBOUND', 'Inbound'), ('UNKNOWN', 'Unknown'), ('INBOUND_MISSED', 'Inbound Missed'), ('INBOUND_ANSWERED', 'Inbound Answered'), ('OUTBOUND', 'Outbound')], default='UNKNOWN', max_length=30),
        ),
        migrations.AlterField(
            model_name='call',
            name='duration',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
