# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tethys_config.init
from ..init import initial_settings, reverse_init

class Migration(migrations.Migration):

    replaces = [(b'tethys_config', '0001_initial'), (b'tethys_config', '0002_auto_20141029_1848'), (b'tethys_config', '0003_auto_20141223_2244'), (b'tethys_config', '0004_auto_20150424_2050'), (b'tethys_config', '0005_auto_20151023_1720')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=500)),
                ('date_modified', models.DateTimeField(verbose_name=b'date modified')),
            ],
        ),
        migrations.CreateModel(
            name='SettingsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='setting',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tethys_config.SettingsCategory'),
        ),
        migrations.RunPython(
            code=tethys_config.init.initial_settings,
            reverse_code=tethys_config.init.reverse_init,
        ),
        migrations.AlterModelOptions(
            name='settingscategory',
            options={'verbose_name': 'Settings Category', 'verbose_name_plural': 'Site Settings'},
        ),
        migrations.AlterField(
            model_name='setting',
            name='content',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='setting',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, verbose_name=b'date modified'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='name',
            field=models.TextField(max_length=30),
        ),
        migrations.RunPython(initial_settings, reverse_init),
    ]
