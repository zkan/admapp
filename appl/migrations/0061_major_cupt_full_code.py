# Generated by Django 2.1.3 on 2018-12-19 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appl', '0060_projectuploadeddocument_document_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='major',
            name='cupt_full_code',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
