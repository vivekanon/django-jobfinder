# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-10 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20180210_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
