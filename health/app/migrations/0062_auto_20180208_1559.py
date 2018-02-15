# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-08 20:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0061_auto_20180208_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log_pc',
            old_name='nombre',
            new_name='cambios',
        ),
        migrations.AlterField(
            model_name='pagos',
            name='productos',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Productos'),
        ),
    ]
