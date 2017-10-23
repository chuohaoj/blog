# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-22 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20171020_0024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['modified_time', '-created_time']},
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
