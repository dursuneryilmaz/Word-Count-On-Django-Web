# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-05-30 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WordCount', '0005_auto_20200530_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wordcount',
            name='file_path',
        ),
        migrations.AddField(
            model_name='wordcount',
            name='file',
            field=models.FileField(default='', upload_to=b''),
            preserve_default=False,
        ),
    ]