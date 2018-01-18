# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-17 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_auto_20171213_1715'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tratamiento',
            old_name='Fecha_ini',
            new_name='fecha_ini',
        ),
        migrations.RemoveField(
            model_name='tratamiento',
            name='Apoyo',
        ),
        migrations.RemoveField(
            model_name='tratamiento',
            name='Diagnostico',
        ),
        migrations.RemoveField(
            model_name='tratamiento',
            name='Dolor_Fisico',
        ),
        migrations.RemoveField(
            model_name='tratamiento',
            name='Estudio_Medico',
        ),
        migrations.RemoveField(
            model_name='tratamiento',
            name='Firma',
        ),
        migrations.RemoveField(
            model_name='tratamiento',
            name='Frecuencia',
        ),
        migrations.RemoveField(
            model_name='tratamiento',
            name='Malestar_Emocional',
        ),
        migrations.RemoveField(
            model_name='tratamiento',
            name='Porcentaje',
        ),
        migrations.RemoveField(
            model_name='tratamiento',
            name='Sesion',
        ),
        migrations.RemoveField(
            model_name='tratamiento',
            name='Tipo',
        ),
        migrations.AddField(
            model_name='tratamiento',
            name='apoyo',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='tratamiento',
            name='diagnostico',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='tratamiento',
            name='dolor_fisico',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='tratamiento',
            name='estudio_medico',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='tratamiento',
            name='firma',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='tratamiento',
            name='frecuencia',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='tratamiento',
            name='malestar_emocional',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='tratamiento',
            name='porcentaje',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='tratamiento',
            name='sesion',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='tratamiento',
            name='tipo',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='atencion',
            name='descripcion',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='domicilio',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='email',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
