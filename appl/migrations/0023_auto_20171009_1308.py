# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appl', '0022_remove_uploadeddocument_admission_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalprofile',
            name='avenue',
            field=models.CharField(blank=True, max_length=100, verbose_name='ซอย'),
        ),
        migrations.AlterField(
            model_name='personalprofile',
            name='road',
            field=models.CharField(blank=True, max_length=100, verbose_name='ถนน'),
        ),
        migrations.AlterField(
            model_name='personalprofile',
            name='village_number',
            field=models.CharField(blank=True, max_length=10, verbose_name='หมู่'),
        ),
    ]