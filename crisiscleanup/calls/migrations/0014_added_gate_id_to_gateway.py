# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-30 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0013_updated_gateway_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='gateway',
            name='gate_id',
            field=models.IntegerField(null=True),
        ),
    ]
