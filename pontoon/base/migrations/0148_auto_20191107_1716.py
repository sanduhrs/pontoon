# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-07 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0147_auto_20191016_2349"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="preferred_source_locale",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="custom_homepage",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
