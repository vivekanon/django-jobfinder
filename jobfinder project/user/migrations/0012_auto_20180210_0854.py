# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-10 05:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20180210_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workschedule',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
