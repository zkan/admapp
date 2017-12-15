# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-15 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appl', '0042_major_study_type'),
        ('regis', '0004_logitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='confirmed_application',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirmed_applicant', to='appl.ProjectApplication'),
        ),
    ]
