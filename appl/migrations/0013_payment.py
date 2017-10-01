# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 14:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regis', '0002_applicant_passport_number'),
        ('appl', '0012_admission_fee_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('national_id', models.CharField(max_length=20)),
                ('verification_number', models.CharField(max_length=30)),
                ('source_type', models.IntegerField(default=0)),
                ('payment_name', models.CharField(blank=True, max_length=100)),
                ('amount', models.FloatField(default=0)),
                ('paid_at', models.DateTimeField()),
                ('has_payment_error', models.BooleanField(default=False)),
                ('admission_round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appl.AdmissionRound')),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='regis.Applicant')),
            ],
        ),
    ]
