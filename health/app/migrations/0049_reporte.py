# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-20 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_auto_20180119_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_ini', models.DateTimeField(blank=True, null=True)),
                ('tipos', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]