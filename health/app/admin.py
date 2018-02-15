from django.contrib import admin

# Register your models here.


#EJEMPLOSSSSSSSSSS......
 
from .models import *
from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


@admin.register(Log_pc)
class Log_pcAdmin(admin.ModelAdmin):
	list_display = ('action','user','cambios',)

@admin.register(Log_r)
class Log_rAdmin(admin.ModelAdmin):
	list_display = ('action','user','paciente','departamento','hora','fecha_ini','tipo','origen','asistencia')


@admin.register(Pestados)
class PestadosAdmin(admin.ModelAdmin):

	list_display = ('nombre',)
@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):

	list_display = ('nombre',)


@admin.register(Origen)
class OrigenAdmin(admin.ModelAdmin):

	list_display = ('nombre',)


@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):

	list_display = ('Fecha_ini','tipos')


@admin.register(Citas)
class CitasAdmin(admin.ModelAdmin):

	list_display = ('id','paciente','descripcion','start')

	def paciente(self, obj):
		return obj.paciente.nombre

@admin.register(Pacientes)
class PacientesAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','apellido','dni','domicilio','ciudad','telefono','celular','email','referenciado','foto','user','estados')


@admin.register(Enfermeros)
class EnfermerosAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellido','dni','domicilio','ciudad','telefono','celular','email','referenciado','foto','user')

@admin.register(Recepcion)
class RecepcionAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellido','dni','domicilio','ciudad','telefono','celular','email','referenciado','foto','user')



@admin.register(Medicos)
class MedicosAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellido','dni','domicilio','ciudad','telefono','celular','email','referenciado','foto','user')

@admin.register(Habitos)
class HabitosAdmin(admin.ModelAdmin):
	list_display = ('nombre',)

@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
	list_display = ('nombre',)

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Fotos)
class FotosAdmin(admin.ModelAdmin):
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
	list_display = ('paciente','medicos','evaluacion','control','tratamiento','descripcion')




@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Pagos)
class PagosAdmin(admin.ModelAdmin):
	list_display = ('id','venta','clasificacion','estado','medico','cobro','pacientes','total','saldo')
	list_filter=('pacientes__nombre',)


@admin.register(Prospecto)
class ProspectoAdmin(admin.ModelAdmin):
	list_display = ('nombre',)

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
	list_display = ('hora','fecha_ini','tipo','origen','asistencia')


@admin.register(Cobro)
class CobroAdmin(admin.ModelAdmin):
	list_display = ('nombre',)




@admin.register(ventas)
class VentasAdmin(admin.ModelAdmin):
	list_display = ('nombre',)


@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
	list_display = ('nombre',)

@admin.register(Clasificacion)
class ClasificacionAdmin(admin.ModelAdmin):
	list_display = ('nombre',)

