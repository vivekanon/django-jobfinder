# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-12 07:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20180210_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workschedule',
            name='user',
        ),
        migrations.AddField(
            model_name='workschedule',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.EmployerProfile'),
        ),
    ]
