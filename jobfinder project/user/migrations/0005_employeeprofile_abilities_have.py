# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-07 06:16
from __future__ import unicode_literals

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_employeeprofile_abilities_have'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeprofile',
            name='abilities_have',
            field=django_mysql.models.ListTextField(models.CharField(max_length=20), default='', size=6),
            preserve_default=False,
        ),
    ]
