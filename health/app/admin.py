from django.contrib import admin

# Register your models here.


#EJEMPLOSSSSSSSSSS......
 
from .models import *
from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

@admin.register(Citas)
class CitasAdmin(admin.ModelAdmin):
	list_display = ('id','title','descripcion','start','end')


@admin.register(Pacientes)
class PacientesAdmin(admin.ModelAdmin):
	list_display = ('DNI','Domicilio','Ciudad','Telefono','Celular','Email','Referenciado')


@admin.register(Habitos)
class HabitosAdmin(admin.ModelAdmin):
	list_display = ('nombre',)



@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Tratamiento)
class TratamientoAdmin(admin.ModelAdmin):
	list_display = ('Diagnostico','Fecha_ini','Frecuencia','Apoyo','Tipo','Porcentaje','Sesion','Dolor_Fisico','Malestar_Emocional','Estudio_Medico','Firma')

