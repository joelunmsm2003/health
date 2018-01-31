# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-30 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20180130_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagos',
            name='resultado',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='pagos',
            name='productos',
            field=models.ForeignKey(blank=True, max_length=300, on_delete=django.db.models.deletion.CASCADE, to='app.Productos'),
        ),
    ]
