# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-30 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20180129_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.DecimalField(decimal_places=2, max_digits=8)),
                ('people', models.IntegerField(help_text='Texto de ayuda')),
            ],
        ),
        migrations.AlterField(
            model_name='pagos',
            name='productos',
            field=models.ForeignKey(blank=True, max_length=300, on_delete=django.db.models.deletion.CASCADE, to='app.Productos'),
        ),
    ]
