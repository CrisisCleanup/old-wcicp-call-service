# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-15 17:43
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0002_auto_20171109_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_trained',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_up_to_date',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='call',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_used_state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='willing_to_be_call_hero',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='willing_to_be_pin_hero',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='willing_to_receive_calls',
            field=models.BooleanField(default=False),
        ),
    ]
