# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-25 23:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_clasificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagos',
            name='Clasificacion',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Clasificacion'),
        ),
        migrations.AddField(
            model_name='pagos',
            name='medico',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Medicos'),
        ),
    ]
