from django import forms
from django.forms import ModelForm, TextInput
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
			'Referenciado':TextInput(attrs={'class':'form-control'})
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
            'title':TextInput(attrs={'class':'form-control'}),
            'descripcion':TextInput(attrs={'class':'form-control'}),
            'start':TextInput(attrs={'class':'form-control'}),
            'end':TextInput(attrs={'class':'form-control'})
            
        }



