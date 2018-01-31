# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-25 23:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180125_1821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cobro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='pagos',
            name='cita',
        ),
        migrations.AddField(
            model_name='pagos',
            name='cobro',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Cobro'),
        ),
    ]