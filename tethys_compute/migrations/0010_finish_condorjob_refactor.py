# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 14:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

import tethys_compute


class Migration(migrations.Migration):

    dependencies = [
        ('tethys_compute', '0009_condorjob_data_migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='tethysjob',
            name='_process_results_function',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='tethysjob',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='condorjob',
            name='cluster_id',
        ),
        migrations.RemoveField(
            model_name='condorjob',
            name='remote_id',
        ),
        migrations.RemoveField(
            model_name='condorjob',
            name='scheduler',
        ),
        migrations.RemoveField(
            model_name='condorjob',
            name='attributes',
        ),
        migrations.RemoveField(
            model_name='condorjob',
            name='num_jobs',
        ),
        migrations.RemoveField(
            model_name='condorjob',
            name='remote_input_files',
        ),
        migrations.RemoveField(
            model_name='condorjob',
            name='condorpy_template_name',
        ),
        migrations.RemoveField(
            model_name='condorjob',
            name='executable',
        ),
        migrations.RenameField(
            model_name='condorjob',
            old_name='tethys_job',
            new_name='condorbase_ptr',
        ),
        migrations.AlterField(
            model_name='condorjob',
            name='condorbase_ptr',
            field=models.OneToOneField(auto_created=True, primary_key=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, serialize=False, to='tethys_compute.CondorBase'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='condorjob',
            name='condorpyjob_ptr',
            field=models.OneToOneField(auto_created=True, null=False, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tethys_compute.CondorPyJob'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CondorPyWorkflow',
            fields=[
                ('condorpyworkflow_id', models.AutoField(primary_key=True, serialize=False)),
                ('_max_jobs', tethys_compute.utilities.DictionaryField(blank=True, default=b'')),
                ('_config', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CondorWorkflow',
            fields=[
                ('condorpyworkflow_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tethys_compute.CondorPyWorkflow')),
                ('condorbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tethys_compute.CondorBase')),
            ],
            bases=('tethys_compute.condorbase', 'tethys_compute.condorpyworkflow'),
        ),
        migrations.CreateModel(
            name='CondorWorkflowNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='node_set', to='tethys_compute.CondorPyWorkflow')),
                ('pre_script', models.CharField(blank=True, max_length=1024, null=True)),
                ('pre_script_args', models.CharField(blank=True, max_length=1024, null=True)),
                ('post_script', models.CharField(blank=True, max_length=1024, null=True)),
                ('post_script_args', models.CharField(blank=True, max_length=1024, null=True)),
                ('variables', tethys_compute.utilities.DictionaryField(blank=True, default=b'')),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=128, null=True)),
                ('retry', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('retry_unless_exit_value', models.IntegerField(blank=True, null=True)),
                ('pre_skip', models.IntegerField(blank=True, null=True)),
                ('abort_dag_on', models.IntegerField(blank=True, null=True)),
                ('abort_dag_on_return_value', models.IntegerField(blank=True, null=True)),
                ('dir', models.CharField(blank=True, max_length=1024, null=True)),
                ('noop', models.BooleanField(default=False)),
                ('done', models.BooleanField(default=False)),
                ('parent_nodes', models.ManyToManyField(related_name='children_nodes', to='tethys_compute.CondorWorkflowNode')),
            ],
        ),
        migrations.CreateModel(
            name='CondorWorkflowJobNode',
            fields=[
                ('condorpyjob_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tethys_compute.CondorPyJob')),
                ('condorworkflownode_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tethys_compute.CondorWorkflowNode')),
            ],
            bases=('tethys_compute.condorworkflownode', 'tethys_compute.condorpyjob'),
        ),
    ]
