# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-10 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nittutorial', '0005_auto_20160229_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorials',
            name='complexity',
            field=models.CharField(max_length=50),
        ),
    ]
