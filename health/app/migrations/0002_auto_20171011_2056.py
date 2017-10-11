# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-11 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Habitos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Diagnostico', models.CharField(max_length=300)),
                ('Fecha_ini', models.DateTimeField(blank=True, null=True)),
                ('Frecuencia', models.CharField(max_length=300)),
                ('Apoyo', models.CharField(max_length=300)),
                ('Tipo', models.CharField(max_length=300)),
                ('Porcentaje', models.CharField(max_length=300)),
                ('Sesion', models.CharField(max_length=300)),
                ('Dolor_Fisico', models.CharField(max_length=300)),
                ('Malestar_Emocional', models.CharField(max_length=300)),
                ('Estudio_Medico', models.CharField(max_length=300)),
                ('Firma', models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='pacientes',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='pacientes',
            name='nombre',
        ),
        migrations.AddField(
            model_name='pacientes',
            name='Celular',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='pacientes',
            name='Ciudad',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='pacientes',
            name='DNI',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='pacientes',
            name='Domicilio',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='pacientes',
            name='Email',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='pacientes',
            name='Referenciado',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='pacientes',
            name='Telefono',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
