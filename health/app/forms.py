from django import forms
from django.forms import *
from app.models import *
from django.utils.translation import ugettext_lazy as  _

class PacientesForm(ModelForm):
    class Meta:
        model = Pacientes
        fields = '__all__'
        exclude = ('user','foto','apellido','telefono','referenciado','ciudad') 
        widgets = {
            'dni':TextInput(attrs={'class':'form-control','type':'number'}),
			'domicilio':TextInput(attrs={'class':'form-control'}),
			'ciudad':Select(attrs={'class':'form-control'}),
			'telefono':TextInput(attrs={'class':'form-control','type':'number'}),
			'celular':TextInput(attrs={'class':'form-control','type':'number'}),
			'email':TextInput(attrs={'class':'form-control'}),
			'referenciado':TextInput(attrs={'class':'form-control'}),
            'nombre':TextInput(attrs={'class':'form-control'}),
            'apellido':TextInput(attrs={'class':'form-control'}),
            'user':Select(attrs={'class':'form-control'}),
            'nacimiento':TextInput(attrs={'type':'date','class':'form-control'}),
            'fecha_ini':TextInput(attrs={'type':'date','class':'form-control'})
        }
        error_messages = {
            'Email': {
                'max_length': _("This writer's name is too long."),
                'required': _("Este campo es obligatorio"),
            },
            'Domicilio': {
                'max_length': _("This writer's name is too long."),
                'required': _("El domicilio es obligatorio"),
            },

        }
        help_texts = {
            'Email': _('Correo valido.'),
            'Domicilio':_('Ingrese su direccion de casa'),
        }

class CitasForm(ModelForm):
    class Meta:
        model = Citas
        fields = '__all__'
        exclude = ('title','area','end','endhora') 
        widgets = {
            'id':TextInput(attrs={'class':'form-control'}),
            'paciente':Select(attrs={'class':'form-control'}),
            'title':TextInput(attrs={'class':'form-control'}),
            'descripcion':TextInput(attrs={'class':'form-control'}),
            'area':Select(attrs={'class':'form-control'}),
            'start':TextInput(attrs={'type':'date','class':"form-control"}),
            'starthora':TextInput(attrs={'type':'time','class':"form-control"}),
            'end':TextInput(attrs={'type':'date','class':"form-control"}),
            'endhora':TextInput(attrs={'type':'time','class':"form-control"}),
            'medico':Select(attrs={'class':'form-control'})
            

        }


class TratamientoForm(ModelForm):
    class Meta:
        model = Tratamiento
        fields = '__all__'
        widgets = {
            'Diagnostico':TextInput(attrs={'class':'form-control'}),
            'paciente':Select(attrs={'class':'form-control'}),
            'medico':Select(attrs={'class':'form-control'}),
            'Fecha_ini':TextInput(attrs={'type':'date','class':'form-control'}),
            'Frecuencia':TextInput(attrs={'class':'form-control'}),
            'Apoyo':TextInput(attrs={'class':'form-control'}),
            'Tipo':TextInput(attrs={'class':'form-control'}),
            'Porcentaje':TextInput(attrs={'class':'form-control'}),
            'Sesion':TextInput(attrs={'class':"form-control"}),
            'Dolor_Fisico':TextInput(attrs={'class':"form-control"}),
            'Malestar_Emocional':TextInput(attrs={'class':"form-control"}),
            'Estudio_Medico':TextInput(attrs={'class':"form-control"}),
            'Firma':TextInput(attrs={'class':'form-control'})
        }



class MedicosForm(ModelForm):
    class Meta:
        model = Medicos
        fields = '__all__'
        exclude = ('user','foto') 
        widgets = {
        'nombre':TextInput(attrs={'class':'form-control'}),
            'apellido':TextInput(attrs={'class':'form-control'}),
            'dni':TextInput(attrs={'class':'form-control','type':'number'}),
            'domicilio':TextInput(attrs={'class':'form-control'}),
            'ciudad':Select(attrs={'class':'form-control'}),
            'telefono':TextInput(attrs={'class':'form-control','type':'number'}),
            'Celular':TextInput(attrs={'class':'form-control','type':'number'}),
            'email':TextInput(attrs={'class':'form-control'}),
            'referenciado':TextInput(attrs={'class':'form-control'})
            
        }
        error_messages = {
            'Email': {
                'max_length': _("This writer's name is too long."),
                'required': _("Este campo es obligatorio"),
            },
            'Domicilio': {
                'max_length': _("This writer's name is too long."),
                'required': _("El domicilio es obligatorio"),
            },

        }
        help_texts = {
            'Email': _('Correo valido.'),
            'Domicilio':_('Ingrese su direccion de casa'),
        }


class AtencionForm(ModelForm):
    class Meta:

        model = Atencion
        fields = '__all__'
        widgets = {
            'paciente':Select(attrs={'class':'form-control'}),
            'medicos':Select(attrs={'class':'form-control'}),
            'evaluacion':Select(attrs={'class':'form-control'}),
            'control':Select(attrs={'class':'form-control'}),
            'tratamiento':Select(attrs={'class':'form-control'}),
            'descripcion':TextInput(attrs={'class':'form-control'})
        }
   

class PagosForm(ModelForm):
    class Meta:
        model = Pagos
        fields = '__all__'
        widgets = {
            'Pacientes':TextInput(attrs={'class':'form-control'}),
            'Fecha':TextInput(attrs={'class':'form-control'}),
            'Cita':TextInput(attrs={'class':'form-control'}),
            'Monto':TextInput(attrs={'class':'form-control','type':'number'}),
            'Estado':TextInput(attrs={'class':'form-control'}),
            'Tipo':TextInput(attrs={'class':'form-control'}),
        }

class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'
        widgets = {
            'Departamento':TextInput(attrs={'class':'form-control'}),
            'hora':TextInput(attrs={'type':'time','class':'form-control'}),

            'paciente':Select(attrs={'class':'form-control','disabled':True}),
            
            'medico':TextInput(attrs={'class':'form-control'}),
            'Tipo ':TextInput(attrs={'class':'form-control'}),
           
            'fecha_ini':TextInput(attrs={'type':'date','class':'form-control'})
        }
     
 

class ReporteForm(ModelForm):
    class Meta:
        model = Reporte
        fields = '__all__'
        widgets = {
           
            'fecha_ini':TextInput(attrs={'type':'date','class':'form-control'}),
               'Tipo':TextInput(attrs={'class':'form-control'}),
        }
     