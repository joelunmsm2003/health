# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-04 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_auto_20171127_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacientes',
            name='fecha_ini',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
