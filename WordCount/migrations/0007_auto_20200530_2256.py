# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-05-30 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WordCount', '0006_auto_20200530_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordcount',
            name='file',
            field=models.FileField(upload_to='WordCount'),
        ),
    ]