# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-03 19:15
from __future__ import unicode_literals

import crisiscleanup.calls.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0015_add_connect_first_event'),
    ]

    def add_initial_languages(apps, schema_editor):
        Language = apps.get_model('calls', 'Language')
        db_alias = schema_editor.connection.alias
        Language.objects.using(db_alias).bulk_create([
            Language(name="English", code="en"),
            Language(name="Spanish", code="es"),
            Language(name="Mandarin", code="zh"),
        ])

    def remove_initial_languages(apps, schema_editor):
        Language = apps.get_model('calls', 'Language')
        db_alias = schema_editor.connection.alias
        Language.objects.using(db_alias).filter(name="English", code="en").delete()
        Language.objects.using(db_alias).filter(name="Spanish", code="es").delete()
        Language.objects.using(db_alias).filter(name="Mandarin", code="zh").delete()

    operations = [
        migrations.CreateModel(
            name='CallerWorksite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worksite', models.UUIDField()),
            ],
            options={
                'db_table': 'caller_worksite',
            },
        ),
        migrations.CreateModel(
            name='CallWorksite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worksite', models.UUIDField()),
            ],
            options={
                'db_table': 'call_worksite',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'language',
            },
        ),
        migrations.RunPython(add_initial_languages, remove_initial_languages),
        migrations.RenameField('user', 'gateway', 'last_used_gateway'),
        migrations.RemoveField(
            model_name='call',
            name='caller_number',
        ),
        migrations.RemoveField(
            model_name='call',
            name='status',
        ),
        migrations.RemoveField(
            model_name='caller',
            name='address_city',
        ),
        migrations.RemoveField(
            model_name='caller',
            name='address_state',
        ),
        migrations.RemoveField(
            model_name='caller',
            name='address_street',
        ),
        migrations.RemoveField(
            model_name='caller',
            name='address_unit',
        ),
        migrations.RemoveField(
            model_name='caller',
            name='address_zipcode',
        ),
        migrations.RemoveField(
            model_name='caller',
            name='calls',
        ),
        migrations.RemoveField(
            model_name='user',
            name='supported_languages',
        ),
        migrations.RemoveField(
            model_name='call',
            name='id'
        ),
        migrations.AddField(
            model_name='call',
            name='call_result',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='call',
            name='call_type',
            field=models.CharField(choices=[('UNKNOWN', 'Unknown'), ('INBOUND_MISSED', 'Inbound Missed'), ('INBOUND_ANSWERED', 'Inbound Answered'), ('OUTBOUND', 'Outbound')], default=crisiscleanup.calls.models.Call.UNKNOWN, max_length=30),
        ),
        migrations.AddField(
            model_name='call',
            name='caller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calls.Caller'),
        ),
        migrations.AddField(
            model_name='call',
            name='ccu_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='call',
            name='call_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='call',
            name='duration',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='call',
            name='external_id',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='call',
            name='gateway',
            field=models.ForeignKey(default='00000000-0000-0000-0000-000000000000', on_delete=django.db.models.deletion.CASCADE, to='calls.Gateway'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='call',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='connectfirstevent',
            name='call_result',
            field=models.CharField(choices=[('UNKNOWN', 'Unknown'), ('CONNECTED', 'Connected'), ('ABANDON', 'Abandoned'), ('DEFLECTED', 'Deflected')], default=crisiscleanup.calls.models.ConnectFirstEvent.UNKNOWN, max_length=100),
        ),
        migrations.AddField(
            model_name='call',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='connectfirstevent',
            name='agent_phone',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='connectfirstevent',
            name='call_start',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='connectfirstevent',
            name='dequeue_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='connectfirstevent',
            name='duration',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='connectfirstevent',
            name='enqueue_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='connectfirstevent',
            name='sess_duration',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterModelTable(
            name='connectfirstevent',
            table='connectfirst_event',
        ),
        migrations.AddField(
            model_name='callworksite',
            name='call',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calls.Call'),
        ),
        migrations.AddField(
            model_name='callerworksite',
            name='caller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calls.Caller'),
        ),
        migrations.AddField(
            model_name='call',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='calls.Language'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='caller',
            name='preferred_language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='calls.Language'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gateway',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='calls.Language'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='languages',
            field=models.ManyToManyField(to='calls.Language'),
        ),
    ]
