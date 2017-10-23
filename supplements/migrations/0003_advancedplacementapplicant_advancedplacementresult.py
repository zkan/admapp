# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 10:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplements', '0002_projectsupplement'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvancedPlacementApplicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('national_id', models.CharField(max_length=16, unique=True)),
                ('student_id', models.CharField(max_length=12, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdvancedPlacementResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_id', models.CharField(max_length=10)),
                ('section_id', models.IntegerField()),
                ('grade', models.CharField(max_length=5)),
                ('ap_applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='supplements.AdvancedPlacementApplicant')),
            ],
        ),
    ]
