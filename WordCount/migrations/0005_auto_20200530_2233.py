# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-05-30 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WordCount', '0004_wordcount_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordcount',
            name='comments',
            field=models.TextField(default=''),
        ),
    ]
