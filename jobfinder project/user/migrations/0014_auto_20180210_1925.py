# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-10 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]