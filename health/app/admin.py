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
	list_display = ('id','paciente','title','descripcion','area','start','end','medico')


@admin.register(Pacientes)
class PacientesAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellido','DNI','Domicilio','Ciudad','Telefono','Celular','Email','Referenciado','foto','user')



@admin.register(Medicos)
class MedicosAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellido','DNI','Domicilio','Ciudad','Telefono','Celular','Email','Referenciado','foto','user')

@admin.register(Habitos)
class HabitosAdmin(admin.ModelAdmin):
	list_display = ('nombre',)



@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Tratamiento)
class TratamientoAdmin(admin.ModelAdmin):
	list_display = ('Diagnostico','Fecha_ini','Frecuencia','Apoyo','Tipo','Porcentaje','Sesion','Dolor_Fisico','Malestar_Emocional','Estudio_Medico','Firma')

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Control)
class ControlAdmin(admin.ModelAdmin):
	list_display = ('nombre',)

@admin.register(Evaluacion)
class EvaluacionAdmin(admin.ModelAdmin):
	list_display = ('nombre',)

@admin.register(Atencion)
class AtencionAdmin(admin.ModelAdmin):
	list_display = ('medicos','consulta','evaluacion','control','tratamiento')




@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Pagos)
class PagosAdmin(admin.ModelAdmin):
	list_display = ('pacientes','fecha','cita','monto','estado','tipo')


@admin.register(Prospecto)
class ProspectoAdmin(admin.ModelAdmin):
	list_display = ('nombre',)

	
