# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-22 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0053_auto_20180122_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='origen',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Origen'),
        ),
    ]
