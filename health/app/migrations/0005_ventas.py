# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-26 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180125_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='ventas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]