# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-18 09:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hasher', '0003_auto_20170617_2252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='number_of_loads',
        ),
    ]
