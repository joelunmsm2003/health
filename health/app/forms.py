from django import forms
from django.forms import ModelForm, TextInput
from app.models import *


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



