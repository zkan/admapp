# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 17:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regis', '0004_logitem'),
        ('appl', '0033_admissionprojectround_applicant_info_viewable'),
        ('backoffice', '0002_auto_20170906_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckMarkGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_marks', models.CharField(default='', max_length=20)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regis.Applicant')),
                ('project_application', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='check_mark_group', to='appl.ProjectApplication')),
            ],
        ),
        migrations.CreateModel(
            name='JudgeComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regis.Applicant')),
                ('project_application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='judge_comment_set', to='appl.ProjectApplication')),
            ],
        ),
    ]
