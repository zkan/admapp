# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-23 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regis', '0008_auto_20180131_1151'),
        ('appl', '0055_auto_20180523_0259'),
        ('backoffice', '0013_remove_applicantmajorresult_exam_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantMajorScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appl.AdmissionProject')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regis.Applicant')),
                ('exam_score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appl.ExamScore')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appl.Major')),
            ],
        ),
        migrations.AddIndex(
            model_name='applicantmajorscore',
            index=models.Index(fields=['major', 'admission_project'], name='backoffice__major_i_9b6816_idx'),
        ),
        migrations.AddIndex(
            model_name='applicantmajorscore',
            index=models.Index(fields=['applicant'], name='backoffice__applica_9e909c_idx'),
        ),
        migrations.AddIndex(
            model_name='applicantmajorscore',
            index=models.Index(fields=['major', 'admission_project', 'applicant'], name='backoffice__major_i_beb8bd_idx'),
        ),
    ]