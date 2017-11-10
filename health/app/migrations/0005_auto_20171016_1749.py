# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-10-16 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20171016_0309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterModelOptions(
            name='citas',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterField(
            model_name='citas',
            name='descripcion',
            field=models.CharField(max_length=300, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='citas',
            name='end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fin'),
        ),
        migrations.AlterField(
            model_name='citas',
            name='start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Inicio'),
        ),
        migrations.AlterField(
            model_name='citas',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Titulo'),
        ),
    ]
