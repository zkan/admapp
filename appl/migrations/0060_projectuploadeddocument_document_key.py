# Generated by Django 2.1.3 on 2018-11-30 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appl', '0059_auto_20181119_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectuploadeddocument',
            name='document_key',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]