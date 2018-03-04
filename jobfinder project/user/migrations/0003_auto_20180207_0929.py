# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-07 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180207_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='job_recommended',
            field=models.ManyToManyField(blank=True, to='job.Job'),
        ),
        migrations.AlterField(
            model_name='employerprofile',
            name='job_offer',
            field=models.ManyToManyField(blank=True, to='job.Job'),
        ),
    ]