# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-02 02:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tethys_compute', '0010_finish_condorjob_refactor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cluster',
        ),
    ]
