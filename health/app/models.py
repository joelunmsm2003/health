from __future__ import unicode_literals
from django.forms import ModelForm
from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.

from django.utils.encoding import python_2_unicode_compatible

import datetime

from django.utils import timezone

@python_2_unicode_compatible
class Citas(models.Model):

    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey('Pacientes',max_length=300,blank=True, null=True)
    title = models.CharField('Titulo',max_length=300)
    descripcion = models.CharField('Descripcion',max_length=300)
    area = models.ForeignKey('Area',max_length=300,blank=True)
    start = models.DateTimeField('Inicio',blank=True, null=True)
    end = models.DateTimeField('Fin',blank=True, null=True)
    medico = models.ForeignKey('Medicos',max_length=300,blank=True, null=True)
   

    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        
        return self.title


@python_2_unicode_compatible
class Consulta(models.Model):

    nombre = models.CharField(max_length=300)
    def __str__(self):

        return self.nombre


@python_2_unicode_compatible
class Pacientes(models.Model):
    nombre =models.CharField(max_length=300,blank=True)
    apellido =models.CharField(max_length=300,blank=True)
    DNI = models.CharField(max_length=300,blank=True)
    Domicilio = models.CharField(max_length=300)
    Ciudad = models.CharField(max_length=300,blank=True)
    Telefono = models.CharField(max_length=300,blank=True)
    Celular = models.CharField(max_length=300,blank=True)
    Email = models.CharField(max_length=300)
    Referenciado = models.CharField(max_length=300,blank=True)
    foto = models.FileField(upload_to='static')
    user = models.ForeignKey(User, models.DO_NOTHING,blank=True,null=True)

    def __str__(self):
        
        if self.user:
            return self.nombre
        else:
            return 'No hay user'





@python_2_unicode_compatible
class Medicos(models.Model):
    nombre = models.CharField(max_length=300,blank=True)
    apellido = models.CharField(max_length=300,blank=True)
    DNI = models.CharField(max_length=300,blank=True)
    Domicilio = models.CharField(max_length=300)
    Ciudad = models.CharField(max_length=300,blank=True)
    Telefono = models.CharField(max_length=300,blank=True)
    Celular = models.CharField(max_length=300,blank=True)
    Email = models.CharField(max_length=300)
    Referenciado = models.CharField(max_length=300,blank=True)
    foto = models.FileField(upload_to='static')
    user = models.ForeignKey(User, models.DO_NOTHING,blank=True,null=True)

    def __str__(self):
        
        if self.user:
            return self.user.username
        else:
            return 'No hay user' 

@python_2_unicode_compatible
class Habitos(models.Model):

    nombre = models.CharField(max_length=300)
        
    def __str__(self):

        return self.nombre





@python_2_unicode_compatible
class Tratamiento(models.Model):

    Diagnostico = models.CharField(max_length=300)
    Fecha_ini = models.DateTimeField(blank=True, null=True)
    Frecuencia = models.CharField(max_length=300)
    Apoyo = models.CharField(max_length=300)
    Tipo = models.CharField(max_length=300)
    Porcentaje = models.CharField(max_length=300)
    Sesion = models.CharField(max_length=300)
    Dolor_Fisico = models.CharField(max_length=300)
    Malestar_Emocional = models.CharField(max_length=300)
    Estudio_Medico = models.CharField(max_length=300)
    Firma = models.CharField(max_length=300)

    def __str__(self):
        
        return self.Diagnostico


@python_2_unicode_compatible
class Area(models.Model):
  
    nombre = models.CharField(max_length=300,blank=True)

    def __str__(self):

        return self.nombre

@python_2_unicode_compatible
class Control(models.Model):
  
    nombre = models.CharField(max_length=300,blank=True)

    def __str__(self):

        return self.nombre

@python_2_unicode_compatible
class Evaluacion(models.Model):
  
    nombre = models.CharField(max_length=300,blank=True)

    def __str__(self):

        return self.nombre

@python_2_unicode_compatible
class Atencion(models.Model):

    citas = models.ForeignKey('Citas',max_length=300,blank=True, null=True)
    consulta = models.ForeignKey('Consulta',max_length=300,blank=True, null=True)
    evaluacion = models.ForeignKey('Evaluacion',max_length=300,blank=True, null=True)
    control= models.ForeignKey('Control',max_length=300,blank=True, null=True)
    tratamiento= models.ForeignKey('Tratamiento',max_length=300,blank=True, null=True)
   
    def __str__(self):

        return self.citas

@python_2_unicode_compatible
class Estado(models.Model):
  
    nombre = models.CharField(max_length=300,blank=True)

    def __str__(self):

        return self.nombre




@python_2_unicode_compatible
class Tipo(models.Model):
  
    nombre = models.CharField(max_length=300,blank=True)

    def __str__(self):

        return self.nombre



@python_2_unicode_compatible
class Pagos(models.Model):

    titulo = models.CharField(max_length=300,blank=True)
    pacientes = models.ForeignKey('Pacientes',max_length=300,blank=True, null=True)
    fecha= models.DateTimeField(blank=True, null=True)
    cita = models.ForeignKey('Citas',max_length=300,blank=True, null=True)
    monto = models.CharField(max_length=300,blank=True)
    estado = models.ForeignKey('Estado',max_length=300,blank=True, null=True)
    tipo = models.ForeignKey('Tipo',max_length=300,blank=True, null=True)
    
    def __str__(self):

        return self.titulo



@python_2_unicode_compatible
class Prospecto(models.Model):
  
    nombre = models.CharField(max_length=300,blank=True)

    def __str__(self):

        return self.nombre



