# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 06:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='provider',
            old_name='languages',
            new_name='language',
        ),
    ]
