# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-24 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0007_auto_20161024_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, help_text='Please enter age', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.IntegerField(blank=True, help_text='Please enter height in cm.', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.IntegerField(blank=True, help_text='Please enter weight in kg', null=True),
        ),
    ]