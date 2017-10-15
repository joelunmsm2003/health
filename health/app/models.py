from __future__ import unicode_literals
from django.forms import ModelForm
from django.db import models
from django import forms

# Create your models here.
# Create your models here.

from django.utils.encoding import python_2_unicode_compatible

import datetime

from django.utils import timezone

@python_2_unicode_compatible
class Citas(models.Model):
    title = models.CharField(max_length=300)
    direccion = models.CharField(max_length=300)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        
        return self.title


@python_2_unicode_compatible
class Consulta(models.Model):

    nombre = models.CharField(max_length=300)
    def __str__(self):

        return self.nombre


@python_2_unicode_compatible
class Pacientes(models.Model):

    DNI = models.CharField(max_length=300,blank=True)
    Domicilio = models.CharField(max_length=300)
    Ciudad = models.CharField(max_length=300,blank=True)
    Telefono = models.CharField(max_length=300,blank=True)
    Celular = models.CharField(max_length=300,blank=True)
    Email = models.CharField(max_length=300)
    Referenciado = models.CharField(max_length=300,blank=True)

    def __str__(self):
        
        return self.DNI


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

