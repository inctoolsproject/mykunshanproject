# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 00:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reportdate', models.DateField(verbose_name='回報日期')),
                ('reportnum', models.IntegerField(default=0, verbose_name='項次')),
                ('description', models.CharField(max_length=200, verbose_name='說明')),
            ],
            options={
                'verbose_name_plural': '回報',
                'verbose_name': '回報',
            },
        ),
    ]
