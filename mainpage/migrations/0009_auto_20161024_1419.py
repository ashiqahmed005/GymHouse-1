# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-24 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0008_auto_20161024_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.CharField(choices=[('1', 'Beginner'), ('2', 'Intermediate'), ('3', 'Advanced'), ('4', 'Expert')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('REG', 'Regular'), ('TRN', 'Trainer'), ('ADM', 'Admin')], default='REG', max_length=3),
        ),
    ]
