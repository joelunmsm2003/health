# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-07 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20171102_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citas',
            name='end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha deFin'),
        ),
        migrations.AlterField(
            model_name='citas',
            name='endhora',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora final'),
        ),
        migrations.AlterField(
            model_name='citas',
            name='start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Inicio'),
        ),
        migrations.AlterField(
            model_name='citas',
            name='starthora',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora de Inicio'),
        ),
    ]