# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-10 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nittutorial', '0018_auto_20160410_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorials',
            name='conten',
        ),
        migrations.AddField(
            model_name='tutorials',
            name='content',
            field=models.TextField(default='write your content here'),
        ),
    ]
