from django import forms
from django.forms import ModelForm, TextInput,DateInput,Select
from app.models import *
from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.Form):

    subject = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Mensaje',widget=forms.TextInput(attrs={'class': 'form-control'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cc_myself = forms.BooleanField(required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))


class PacientesForm(ModelForm):
    class Meta:
        model = Pacientes
        fields = '__all__'
        widgets = {
            'DNI':TextInput(attrs={'class':'form-control'}),
			'Domicilio':TextInput(attrs={'class':'form-control'}),
			'Ciudad':TextInput(attrs={'class':'form-control'}),
			'Telefono':TextInput(attrs={'class':'form-control'}),
			'Celular':TextInput(attrs={'class':'form-control'}),
			'Email':TextInput(attrs={'class':'form-control'}),
			'Referenciado':TextInput(attrs={'class':'form-control'}),
            'nombre':TextInput(attrs={'class':'form-control'}),
            'apellido':TextInput(attrs={'class':'form-control'}),
            'user':Select(attrs={'class':'form-control'})
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
        widgets = {
            'id':TextInput(attrs={'class':'form-control'}),
            'paciente':Select(attrs={'class':'form-control'}),
            'title':TextInput(attrs={'class':'form-control'}),
            'descripcion':TextInput(attrs={'class':'form-control'}),
            'area':Select(attrs={'class':'form-control'}),
            'start':forms.widgets.DateTimeInput(format='%m/%d/%Y %H:%M'),
            'end':DateInput(),
            'medico':TextInput(attrs={'class':'form-control'})
            

        }

class MedicosForm(ModelForm):
    class Meta:
        model = Medicos
        fields = '__all__'
        widgets = {
            'DNI':TextInput(attrs={'class':'form-control'}),
            'Domicilio':TextInput(attrs={'class':'form-control'}),
            'Ciudad':TextInput(attrs={'class':'form-control'}),
            'Telefono':TextInput(attrs={'class':'form-control'}),
            'Celular':TextInput(attrs={'class':'form-control'}),
            'Email':TextInput(attrs={'class':'form-control'}),
            'Referenciado':TextInput(attrs={'class':'form-control'}),
            'nombre':TextInput(attrs={'class':'form-control'}),
            'apellido':TextInput(attrs={'class':'form-control'})
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
            'Cita':TextInput(attrs={'class':'form-control'}),
            'Consulta':TextInput(attrs={'class':'form-control'}),
            'Evaluacion':TextInput(attrs={'class':'form-control'}),
            'Control':TextInput(attrs={'class':'form-control'}),
            'Tratamiento':TextInput(attrs={'class':'form-control'}),
        }
        error_messages = {
            'Cita': {
                'max_length': _("This writer's name is too long."),
                'required': _("Este campo es obligatorio"),
            },
            'Consulta': {
                'max_length': _("This writer's name is too long."),
                'required': _("El domicilio es obligatorio"),
            },

        }
        help_texts = {
            'Cita': _('Correo valido.'),
            'Consulta':_('Ingrese su direccion de casa'),
        }


class PagosForm(ModelForm):
    class Meta:
        model = Pagos
        fields = '__all__'
        widgets = {
            'Pacientes':TextInput(attrs={'class':'form-control'}),
            'Fecha':TextInput(attrs={'class':'form-control'}),
            'Cita':TextInput(attrs={'class':'form-control'}),
            'Monto':TextInput(attrs={'class':'form-control'}),
            'Estado':TextInput(attrs={'class':'form-control'}),
            'Tipo':TextInput(attrs={'class':'form-control'}),
        }
        error_messages = {
            'Pacientes': {
                'max_length': _("This writer's name is too long."),
                'required': _("Este campo es obligatorio"),
            },
            'Fecha': {
                'max_length': _("This writer's name is too long."),
                'required': _("El domicilio es obligatorio"),
            },

        }
        help_texts = {
            'Pacientes': _('Correo valido.'),
            'Fecha':_('Ingrese su direccion de casa'),
        }



