# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-06 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_auto_20180206_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagos',
            name='productos',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Productos'),
        ),
    ]
