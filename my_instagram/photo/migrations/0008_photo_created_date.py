# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 08:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0007_auto_20161111_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
