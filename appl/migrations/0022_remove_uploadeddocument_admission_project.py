# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 07:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appl', '0021_projectuploadeddocument_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadeddocument',
            name='admission_project',
        ),
    ]
