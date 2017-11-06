# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appl', '0035_admissionprojectround_accepted_for_interview_result_shown'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admissionprojectround',
            options={'ordering': ['admission_round', 'admission_project']},
        ),
        migrations.AddField(
            model_name='admissionprojectround',
            name='accepted_for_interview_instructions',
            field=models.TextField(blank=True, verbose_name='รายละเอียดแสดงกับผู้สมัครที่ผ่านการคัดเลือก'),
        ),
    ]
