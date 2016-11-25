# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weeklyreport', '0005_auto_20161028_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacation',
            name='vacationstatus',
            field=models.CharField(choices=[('已休假', '已休假'), ('申請休假', '申請休假')], default='申請休假', max_length=50, verbose_name='狀態'),
        ),
    ]