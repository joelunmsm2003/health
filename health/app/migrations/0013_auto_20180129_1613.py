# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-29 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20180129_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagos',
            name='productos',
            field=models.ForeignKey(blank=True, max_length=300, on_delete=django.db.models.deletion.CASCADE, to='app.Productos'),
        ),
    ]
