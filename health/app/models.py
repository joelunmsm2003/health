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


from django.db import models

@python_2_unicode_compatible
class Asistencia(models.Model):
    nombre = models.CharField(max_length=300,blank=True,null=True)
  
    def __str__(self):
        
        return self.nombre

@python_2_unicode_compatible
class Origen(models.Model):
    nombre = models.CharField(max_length=300,blank=True,null=True)
  
    def __str__(self):
        
        return self.nombre

@python_2_unicode_compatible

class Reporte(models.Model):
    Fecha_ini = models.DateTimeField(blank=True, null=True)
    tipos = models.CharField(max_length=300,blank=True,null=True)
  
    def __str__(self):
        
        return self.tipos



@python_2_unicode_compatible
class Tratamiento(models.Model):
    paciente = models.ForeignKey('Pacientes',max_length=300,blank=True, null=True)
    medico = models.ForeignKey('Medicos',max_length=300,blank=True, null=True)

    Diagnostico = models.CharField(max_length=300,blank=True,null=True)
    Fecha_ini = models.DateTimeField(blank=True, null=True)
    Frecuencia = models.CharField(max_length=300,blank=True,null=True)
    Apoyo = models.CharField(max_length=300,blank=True,null=True)
    Tipo = models.CharField(max_length=300,blank=True,null=True)
    Porcentaje = models.CharField(max_length=300,blank=True,null=True)
    Sesion = models.CharField(max_length=300,blank=True,null=True)
    Dolor_Fisico = models.CharField(max_length=300,blank=True,null=True)
    Malestar_Emocional = models.CharField(max_length=300,blank=True,null=True)
    Estudio_Medico = models.CharField(max_length=300,blank=True,null=True)
    Firma = models.CharField(max_length=300,blank=True,null=True)


    def __str__(self):
        
        return self.Tipo


@python_2_unicode_compatible
class Citas(models.Model):

    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey('Pacientes',max_length=300,blank=True, null=True)
    title = models.CharField('Titulo',max_length=300)
    descripcion = models.CharField('Descripcion',max_length=300)
    area = models.ForeignKey('Area',max_length=300,blank=True,null=True)
    start = models.DateTimeField('Fecha de Inicio',blank=True, null=True)

    end = models.DateTimeField('Fecha deFin',blank=True, null=True)

    medico = models.ForeignKey('Medicos',max_length=300,blank=True, null=True)


    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        
        return self.title



@python_2_unicode_compatible
class Ciudad(models.Model):

    nombre = models.CharField(max_length=300)
    def __str__(self):

        return self.nombre


@python_2_unicode_compatible
class Departamento(models.Model):

    nombre = models.CharField(max_length=300)
    def __str__(self):

        return self.nombre 


@python_2_unicode_compatible
class Pestados(models.Model):

    nombre = models.CharField(max_length=300)
    def __str__(self):

        return self.nombre       

@python_2_unicode_compatible
class Pacientes(models.Model):
    nombre =models.CharField(max_length=300,blank=True)
    apellido =models.CharField(max_length=300,blank=True)
    dni = models.CharField(max_length=300,blank=True)
    domicilio = models.CharField(max_length=300,blank=True,null=True)
    ciudad = models.ForeignKey('Ciudad',max_length=300,blank=True,null=True)
    telefono = models.CharField(max_length=300,blank=True)
    celular = models.CharField(max_length=300,blank=True)
    email = models.CharField(max_length=300,blank=True,null=True)
    referenciado = models.CharField(max_length=300,blank=True)
    foto = models.TextField(db_column='foto',blank=True,)
    user = models.ForeignKey(User, models.DO_NOTHING,blank=True,null=True)
    nacimiento= models.DateTimeField(blank=True, null=True)
    fecha_ini= models.DateTimeField('Fecha de Ingreso',blank=True, null=True)
    estados = models.ForeignKey('Pestados',max_length=300,blank=True,null=True)


    def __str__(self):

        return self.nombre

    def save(self, *args,**kwargs):

        print 'Estoy fregando....', self.user

        super(Pacientes, self) .save(*args, **kwargs)

@python_2_unicode_compatible
class Enfermeros(models.Model):
    nombre = models.CharField(max_length=300,blank=True)
    apellido = models.CharField(max_length=300,blank=True)
    dni = models.CharField(max_length=300,blank=True)
    domicilio = models.CharField(max_length=300)
    ciudad = models.ForeignKey('Ciudad',max_length=300,blank=True,null=True)
    telefono = models.CharField(max_length=300,blank=True)
    celular = models.CharField(max_length=300,blank=True)
    email = models.CharField(max_length=300)
    referenciado = models.CharField(max_length=300,blank=True)
    foto = models.FileField(upload_to='static')
    user = models.ForeignKey(User, models.DO_NOTHING,blank=True,null=True)

    def __str__(self):
        
        return self.nombre

@python_2_unicode_compatible
class Recepcion(models.Model):
    nombre = models.CharField(max_length=300,blank=True)
    apellido = models.CharField(max_length=300,blank=True)
    dni = models.CharField(max_length=300,blank=True)
    domicilio = models.CharField(max_length=300)
    ciudad = models.ForeignKey('Ciudad',max_length=300,blank=True,null=True)
    telefono = models.CharField(max_length=300,blank=True)
    celular = models.CharField(max_length=300,blank=True)
    email = models.CharField(max_length=300)
    referenciado = models.CharField(max_length=300,blank=True)
    foto = models.FileField(upload_to='static',blank=True,null=True)
    user = models.ForeignKey(User, models.DO_NOTHING,blank=True,null=True)

    def __str__(self):
        
        return self.nombre


@python_2_unicode_compatible
class Fotos(models.Model):
    nombre = models.CharField(max_length=300,blank=True)
    foto = models.FileField(upload_to='static')

    def __str__(self):
        
        return self.nombre



@python_2_unicode_compatible
class Medicos(models.Model):
    nombre = models.CharField(max_length=300,blank=True)
    apellido = models.CharField(max_length=300,blank=True)
    dni = models.CharField(max_length=300,blank=True)
    domicilio = models.CharField(max_length=300)
    ciudad = models.ForeignKey('Ciudad',max_length=300,blank=True,null=True)
    telefono = models.CharField(max_length=300,blank=True)
    celular = models.CharField('Celular',max_length=300,blank=True)
    email = models.CharField(max_length=300)
    referenciado = models.CharField(max_length=300,blank=True)
    foto = models.FileField(upload_to='static')
    user = models.ForeignKey(User, models.DO_NOTHING,blank=True,null=True)

    def __str__(self):
        
        return self.nombre


@python_2_unicode_compatible
class Habitos(models.Model):

    nombre = models.CharField(max_length=300)
        
    def __str__(self):

        return self.nombre







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

    paciente = models.ForeignKey('Pacientes',max_length=300,blank=True, null=True)
    medicos = models.ForeignKey('Medicos',max_length=300,blank=True, null=True)
    evaluacion = models.ForeignKey('Evaluacion',max_length=300,blank=True, null=True)
    control= models.ForeignKey('Control',max_length=300,blank=True, null=True)
    tratamiento= models.ForeignKey('Tratamiento',max_length=300,blank=True, null=True)
    descripcion = models.CharField(max_length=300,blank=True)
    fecha = models.DateTimeField('Fecha de Atencion',blank=True, null=True)
   
    def __str__(self):

        return self.medicos

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


class Log_usuario(models.Model):
        action =models.CharField(max_length=300,blank=True)
        user = models.ForeignKey(User,max_length=300,blank=True, null=True)
        fecha =models.CharField(max_length=300,blank=True)
        

        def __str__(self):

                return self.nombre
        class Meta:
                managed =True
                verbose_name ='log_usuarios' 



class Log_pc(models.Model):
        action =models.CharField(max_length=300,blank=True)
        user = models.ForeignKey(User,max_length=300,blank=True, null=True)
        cambios =models.CharField(max_length=300,blank=True)
        fecha =models.CharField(max_length=300,blank=True)
        

        def __str__(self):

                return self.nombre
        class Meta:
                managed =True
                verbose_name ='log_Pacientes' 




@python_2_unicode_compatible
class Log_r(models.Model):
        action =models.CharField(max_length=300,blank=True)
        user = models.ForeignKey(User,max_length=300,blank=True, null=True)
        paciente = models.ForeignKey('Pacientes',max_length=300,blank=True, null=True)

        departamento=  models.ForeignKey('Departamento',max_length=300,blank=True, null=True)
        hora = models.TimeField(blank=True, null=True)

        fecha_ini= models.DateTimeField(blank=True, null=True)
    
        #medicos = models.ForeignKey('Medicos',max_length=300,blank=True,   null=True)
        #consulta = models.ForeignKey('Consulta',max_length=300,blank=True,     null=True)
        tipo = models.ForeignKey('Tipo',max_length=300,blank=True, null=True)
        origen = models.ForeignKey('Origen',max_length=300,blank=True,  null=True)
        asistencia = models.ForeignKey('Asistencia',max_length=300,blank=True,  null=True)
        fecha =models.CharField(max_length=300,blank=True)

        def __str__(self):

                return self.nombre  
        class Meta:
                managed =True
                verbose_name ='log_nuevaconsulta'   



@python_2_unicode_compatible
class Consulta(models.Model):
    paciente = models.ForeignKey('Pacientes',max_length=300,blank=True, null=True)
    departamento=  models.ForeignKey('Departamento',max_length=300,blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)

    fecha_ini= models.DateTimeField(blank=True, null=True)
    
    #medicos = models.ForeignKey('Medicos',max_length=300,blank=True, null=True)
    #consulta = models.ForeignKey('Consulta',max_length=300,blank=True, null=True)
    tipo = models.ForeignKey('Tipo',max_length=300,blank=True, null=True)
    origen = models.ForeignKey('Origen',max_length=300,blank=True, null=True)
    asistencia = models.ForeignKey('Asistencia',max_length=300,blank=True, null=True)
    
    def __str__(self):

        return 'self.medicos.nombre'

@python_2_unicode_compatible
class Clasificacion(models.Model):
  
    nombre = models.CharField(max_length=300,blank=True)

    def __str__(self):

        return self.nombre




@python_2_unicode_compatible
class Cobro(models.Model):
  
    nombre = models.CharField(max_length=300,blank=True)

    def __str__(self):

        return self.nombre

@python_2_unicode_compatible
class ventas(models.Model):
  
    nombre = models.CharField(max_length=300,blank=True)

    def __str__(self):

        return self.nombre



@python_2_unicode_compatible
class Productos(models.Model):
  
    nombre = models.CharField(max_length=300,blank=True)

    def __str__(self):

        return self.nombre



@python_2_unicode_compatible
class Tiposventa(models.Model):
  
    nombre = models.CharField(max_length=300,blank=True)

    def __str__(self):

        return self.nombre
        
@python_2_unicode_compatible
class Pagos(models.Model):

    pacientes = models.ForeignKey('Pacientes',max_length=300,blank=True, null=True)
    venta = models.ForeignKey('ventas',max_length=300,blank=True,null=True)
    clasificacion=models.ForeignKey('Clasificacion',max_length=300,blank=True, null=True)
    estado = models.ForeignKey('Estado',max_length=300,blank=True, null=True)
    medico=models.ForeignKey('Medicos',max_length=300,blank=True, null=True)
    cobro= models.ForeignKey('Cobro',max_length=300,blank=True, null=True)  
    productos= models.ForeignKey('Productos',max_length=300,blank=True,null=True)
    cantidad = models.FloatField(max_length=300,blank=True,null=True)
    precio = models.FloatField(max_length=300,blank=True,null=True)
    descuento = models.FloatField(max_length=300,blank=True,null=True)
    
    pago = models.FloatField(max_length=300,blank=True,null=True)
    total = models.FloatField(max_length=300,blank=True,null=True)
    saldo = models.FloatField(max_length=300,blank=True,null=True)
    
    def __str__(self):

        return self.venta.nombre



@python_2_unicode_compatible
class Prospecto(models.Model):
  
    nombre = models.CharField(max_length=300,blank=True)

    def __str__(self):

        return self.nombre

@python_2_unicode_compatible
class Notificacion(models.Model):
  
    titulo = models.CharField(max_length=300,blank=True)

    def __str__(self):

        return self.nombre

