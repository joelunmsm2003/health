# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-06 22:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_auto_20171206_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='tipo',
            field=models.ForeignKey(blank=True, max_length=300, on_delete=django.db.models.deletion.CASCADE, to='app.Tipo'),
        ),
    ]