# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-27 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20171027_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atencion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citas', models.CharField(max_length=300)),
                ('consulta', models.CharField(max_length=300)),
                ('evaluacion', models.CharField(max_length=300)),
                ('control', models.DateTimeField(blank=True, null=True)),
                ('tratamiento', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
