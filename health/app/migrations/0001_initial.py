# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-25 20:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Atencion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=300)),
                ('fecha', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Atencion')),
            ],
        ),
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300, verbose_name='Titulo')),
                ('descripcion', models.CharField(max_length=300, verbose_name='Descripcion')),
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Inicio')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='Fecha deFin')),
                ('area', models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Area')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.TimeField(blank=True, null=True)),
                ('fecha_ini', models.DateTimeField(blank=True, null=True)),
                ('asistencia', models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Asistencia')),
            ],
        ),
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Enfermeros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300)),
                ('apellido', models.CharField(blank=True, max_length=300)),
                ('dni', models.CharField(blank=True, max_length=300)),
                ('domicilio', models.CharField(max_length=300)),
                ('telefono', models.CharField(blank=True, max_length=300)),
                ('celular', models.CharField(blank=True, max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('referenciado', models.CharField(blank=True, max_length=300)),
                ('foto', models.FileField(upload_to='static')),
                ('ciudad', models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Ciudad')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300)),
                ('foto', models.FileField(upload_to='static')),
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
            name='Medicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300)),
                ('apellido', models.CharField(blank=True, max_length=300)),
                ('dni', models.CharField(blank=True, max_length=300)),
                ('domicilio', models.CharField(max_length=300)),
                ('telefono', models.CharField(blank=True, max_length=300)),
                ('celular', models.CharField(blank=True, max_length=300, verbose_name='Celular')),
                ('email', models.CharField(max_length=300)),
                ('referenciado', models.CharField(blank=True, max_length=300)),
                ('foto', models.FileField(upload_to='static')),
                ('ciudad', models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Ciudad')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Origen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300)),
                ('apellido', models.CharField(blank=True, max_length=300)),
                ('dni', models.CharField(blank=True, max_length=300)),
                ('domicilio', models.CharField(blank=True, max_length=300, null=True)),
                ('telefono', models.CharField(blank=True, max_length=300)),
                ('celular', models.CharField(blank=True, max_length=300)),
                ('email', models.CharField(blank=True, max_length=300, null=True)),
                ('referenciado', models.CharField(blank=True, max_length=300)),
                ('foto', models.TextField(blank=True, db_column='foto')),
                ('nacimiento', models.DateTimeField(blank=True, null=True)),
                ('fecha_ini', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Ingreso')),
                ('ciudad', models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Ciudad')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('monto', models.CharField(blank=True, max_length=300)),
                ('cita', models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Citas')),
                ('estado', models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Estado')),
                ('pacientes', models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Pacientes')),
            ],
        ),
        migrations.CreateModel(
            name='Prospecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Recepcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300)),
                ('apellido', models.CharField(blank=True, max_length=300)),
                ('dni', models.CharField(blank=True, max_length=300)),
                ('domicilio', models.CharField(max_length=300)),
                ('telefono', models.CharField(blank=True, max_length=300)),
                ('celular', models.CharField(blank=True, max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('referenciado', models.CharField(blank=True, max_length=300)),
                ('foto', models.FileField(upload_to='static')),
                ('ciudad', models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Ciudad')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_ini', models.DateTimeField(blank=True, null=True)),
                ('tipos', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='tiposventa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Diagnostico', models.CharField(blank=True, max_length=300, null=True)),
                ('Fecha_ini', models.DateTimeField(blank=True, null=True)),
                ('Frecuencia', models.CharField(blank=True, max_length=300, null=True)),
                ('Apoyo', models.CharField(blank=True, max_length=300, null=True)),
                ('Tipo', models.CharField(blank=True, max_length=300, null=True)),
                ('Porcentaje', models.CharField(blank=True, max_length=300, null=True)),
                ('Sesion', models.CharField(blank=True, max_length=300, null=True)),
                ('Dolor_Fisico', models.CharField(blank=True, max_length=300, null=True)),
                ('Malestar_Emocional', models.CharField(blank=True, max_length=300, null=True)),
                ('Estudio_Medico', models.CharField(blank=True, max_length=300, null=True)),
                ('Firma', models.CharField(blank=True, max_length=300, null=True)),
                ('medico', models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Medicos')),
                ('paciente', models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Pacientes')),
            ],
        ),
        migrations.AddField(
            model_name='pagos',
            name='tipo',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Tipo'),
        ),
        migrations.AddField(
            model_name='pagos',
            name='venta',
            field=models.ForeignKey(blank=True, max_length=300, on_delete=django.db.models.deletion.CASCADE, to='app.tiposventa'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='departamento',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Departamento'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='origen',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Origen'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Pacientes'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='tipo',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Tipo'),
        ),
        migrations.AddField(
            model_name='citas',
            name='medico',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Medicos'),
        ),
        migrations.AddField(
            model_name='citas',
            name='paciente',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Pacientes'),
        ),
        migrations.AddField(
            model_name='atencion',
            name='control',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Control'),
        ),
        migrations.AddField(
            model_name='atencion',
            name='evaluacion',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Evaluacion'),
        ),
        migrations.AddField(
            model_name='atencion',
            name='medicos',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Medicos'),
        ),
        migrations.AddField(
            model_name='atencion',
            name='paciente',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Pacientes'),
        ),
        migrations.AddField(
            model_name='atencion',
            name='tratamiento',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Tratamiento'),
        ),
    ]
