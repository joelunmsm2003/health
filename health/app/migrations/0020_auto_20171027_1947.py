# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-27 19:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20171027_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagos',
            name='estado',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Estado'),
        ),
        migrations.AlterField(
            model_name='pagos',
            name='tipo',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Tipo'),
        ),
    ]
