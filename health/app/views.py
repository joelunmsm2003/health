 #      ___           ___          _____                             ___          ___     
 #     /  /\         /__/\        /  /::\         ___               /  /\        /  /\    
 #    /  /::\        \  \:\      /  /:/\:\       /__/|             /  /:/       /  /::\   
 #   /  /:/\:\        \  \:\    /  /:/  \:\     |  |:|            /__/::\      /  /:/\:\  
 #  /  /:/~/::\   _____\__\:\  /__/:/ \__\:|    |  |:|            \__\/\:\    /  /:/  \:\ 
 # /__/:/ /:/\:\ /__/::::::::\ \  \:\ /  /:/  __|__|:|               \  \:\  /__/:/ \__\:\
 # \  \:\/:/__\/ \  \:\~~\~~\/  \  \:\  /:/  /__/::::\                \__\:\ \  \:\ /  /:/
 #  \  \::/       \  \:\  ~~~    \  \:\/:/      ~\~~\:\               /  /:/  \  \:\  /:/ 
 #   \  \:\        \  \:\         \  \::/         \  \:\             /__/:/    \  \:\/:/  
 #    \  \:\        \  \:\         \__\/           \__\/             \__\/      \  \::/   
 #     \__\/         \__\/                                                       \__\/    
                                                                                                                                                                     
                                               
# Empresa Xiencias
# Developers:
# email : joelunmsm@gmail.com
# email :
# Web   : xiencias.com
# Fecha : 2 de Nov 2017
                                                                                    
                                                                                                 
                                                                                                 


from django.shortcuts import *
from django.template import RequestContext
from django.contrib.auth import *
from django.contrib.auth.models import Group, User

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Max,Count
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app.models import *

from django.db import transaction
from django.contrib.auth.hashers import *
from django.core.mail import send_mail

from django.utils.six.moves import range
from django.http import StreamingHttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt
import time
import collections
import xlrd
import json 
import csv
import simplejson
import xlwt
import requests
import os
from django.contrib.auth import authenticate, login


from datetime import datetime,timedelta
from django.contrib.auth import authenticate

from django.contrib.sites.shortcuts import get_current_site
from django.core import serializers

from forms import *

from app.serializer import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from datetime import *


def traeconsulta(request):


	form = ConsultaForm()

	_consulta = Consulta.objects.all().order_by('-id')
	#para q apraseca los conteos  de los indicadore en consulta

	u = User.objects.get(id=request.user.id)

	grupo =u.groups.get()

	npacientes = Pacientes.objects.all().count()

	ncitas = Citas.objects.all().count()

	natenciones= Atencion.objects.all().count()

	ncitashoy = Citas.objects.filter(start__gte=datetime.today()).count()




	return render(request, 'consulta.html',{'form': form,'consulta':_consulta,'user':u,'grupo':grupo,'natenciones':natenciones,'npacientes':npacientes,'ncitashoy':ncitashoy,'ncitas':ncitas})


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'dashboard.html', {'form': form})



def reportes(request):


	c = Consulta.objects.all()

	#nombre = request.GET['dato']

	#p=Pacientes.objects.filter(dni__search=nombre)

	#p=Pacientes.objects.filter(nombre__contains=nombre)

	
	return render(request, 'reportes.html',{'c':c})

def busqueda(request):

	nombre = request.GET['dato']

	#p=Pacientes.objects.filter(dni__search=nombre)

	p=Pacientes.objects.filter(nombre__contains=nombre)

	
	return render(request, 'paciente.html',{'pacientes':p})

def tomafoto(request):


	
	return render(request, 'subefoto.html',{})

import base64
@csrf_exempt
def uploadfoto(request,paciente):

	
	if request.method == 'POST':



		data =request.POST['file']

		print 'ingrese....'

		p =Pacientes.objects.get(id=paciente)
		p.foto = str(data)
		p.save()



		f = open('/var/www/recibidos.txt', 'a')
		f.write(str((data)))
		f.close()


	
	return render(request, 'subefoto.html',{})


def decode_base64(data):

    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding)
    return base64.decodestring(data)

def busquedacita(request):

	paciente = request.GET['dato']

	#p=Pacientes.objects.filter(dni__search=nombre)

	c=Citas.objects.filter(paciente__nombre__contains=paciente)

	
	return render(request, 'citas.html',{'citas':c})


def busquedamedico(request):

	nombre= request.GET['dato']

	#p=Pacientes.objects.filter(dni__search=nombre)

	m=Medicos.objects.filter(nombre__contains=nombre)

	
	return render(request, 'medico.html',{'medicos':m})



def busquedaconsulta(request):

	tipo= request.POST['tipo']

	print 'traendo los tipossss',tipo

	fecha= request.POST['fecha']

	print 'fechasss',fecha

	c = Consulta.objects.filter(fecha_ini=fecha)

	print 'cccccc',c

	#p=Pacientes.objects.filter(dni__search=nombre)

	
	
	return render(request, 'reportes.html',{'c':c})





def home(request):


	
	return render(request, 'index.html',{})

def login2(request):


	
	return render(request, 'login.html',{})

def citasjson(request):




    serializer = CitasSerializer(Citas.objects.all(), many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def fotos(request):

    serializer = FotosSerializer(Fotos.objects.all().order_by('id'), many=True)
    return JsonResponse(serializer.data, safe=False)


def citaspk(request,pk):

	try:
		c = Citas.objects.get(pk=pk)
	except Citas.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = CitasSerializer(c)
		return JsonResponse(serializer.data)
	

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = CitasSerializer(c, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)


	serializer = CitasSerializer(Citas.objects.all(), many=True)
	return JsonResponse(serializer.data, safe=False)


def nuevacita(request):

	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = CitasForm(request.POST)


		fecha = str(request.POST['start'])

		#+' '+str(request.POST['starthora'])



		fecha = datetime.strptime(fecha, '%Y-%m-%d')

								

		# Create and save the new author instance. There's no need to do anything else.


	# check whether it's valid:
		if form.is_valid():

			print 'Entre a guardar'

			a = Citas()

			f = CitasForm(request.POST, instance=a).save()

			id_c = Citas.objects.all().values('id').order_by('-id')[0]['id']

			c = Citas.objects.get(id=id_c)

			c.start = fecha
	
			c.save()



			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return HttpResponseRedirect('/citas')

	    # if a GET (or any other method) we'll create a blank form
	else:

		form = CitasForm()

		u = User.objects.get(id=request.user.id)

		grupo =u.groups.get()



	return render(request, 'nuevacita.html',{'user':traeeluser(request),'grupo':traeelgrupo(request),'form': form})


def editpaciente(request,id_paciente):

	if request.method == 'POST':

		a=Pacientes.objects.get(id=id_paciente)

		form = PacientesForm(request.POST, instance=a)


		if form.is_valid():

			print 'validoooooo'

			f = PacientesForm(request.POST, instance=a).save()


			return HttpResponseRedirect('/paciente/')

	    # if a GET (or any other method) we'll create a blank form
	else:


		p = Pacientes.objects.get(id=id_paciente)

		c = Citas.objects.filter(paciente_id=id_paciente)

		t = Tratamiento.objects.filter(paciente_id=id_paciente)
		
		form = PacientesForm(instance=p)

	return render(request, 'editpaciente.html',{'t':t,'user':traeeluser(request),'grupo':traeelgrupo(request),'form': form,'id_paciente':id_paciente,'paciente':p,'citas':c})


def traeeluser(request):

	u = User.objects.get(id=request.user.id)

	grupo =u.groups.get()

	if str(grupo) =='Recepcion':

		u = Recepcion.objects.get(user_id=request.user.id)

	if str(grupo) =='Enfermeros':

		u = Enfermeros.objects.get(user_id=request.user.id)

	if str(grupo) =='Medicos':

		u = Medicos.objects.get(user_id=request.user.id)

	return u

def traeelgrupo(request):

	u = User.objects.get(id=request.user.id)

	grupo =u.groups.get()

	return grupo


@login_required(login_url="/login")
def paciente(request):


	form = PacientesForm()

	_pacientes = Pacientes.objects.all().order_by('-id')

	npacientes = Pacientes.objects.all().count()

	ncitas = Citas.objects.all().count()

	natenciones= Atencion.objects.all().count()

	ncitashoy = Citas.objects.filter(start__gte=datetime.today()).count()


	return render(request, 'paciente.html',{'user':traeeluser(request),'form': form,'pacientes':_pacientes,'grupo':traeelgrupo(request),'natenciones':natenciones,'npacientes':npacientes,'ncitashoy':ncitashoy,'ncitas':ncitas})

@login_required(login_url="/login")
def citas(request):


	form = CitasForm()

	_citas = Citas.objects.all()
	#para q apraseca los conteos  de los indicadore en citas

	u = User.objects.get(id=request.user.id)

	grupo =u.groups.get()

	npacientes = Pacientes.objects.all().count()

	ncitas = Citas.objects.all().count()

	natenciones= Atencion.objects.all().count()

	ncitashoy = Citas.objects.filter(start__gte=datetime.today()).count()



	return render(request, 'citas.html',{'user':traeeluser(request),'grupo':traeelgrupo(request),'form': form,'citas':_citas,'natenciones':natenciones,'npacientes':npacientes,'ncitashoy':ncitashoy,'ncitas':ncitas})

@login_required(login_url="/login")
def editmedico(request,id_medico):

	if request.method == 'POST':

		a=Medicos.objects.get(id=id_medico)

		form = MedicosForm(request.POST, instance=a)


		if form.is_valid():

			print 'validoooooo'

			f = MedicosForm(request.POST, instance=a).save()


			return HttpResponseRedirect('/medico/')

	    # if a GET (or any other method) we'll create a blank form
	else:


		m=Medicos.objects.get(id=id_medico)
		
		form = MedicosForm(instance=m)

	return render(request, 'editmedico.html',{'user':traeeluser(request),'grupo':traeelgrupo(request),'form': form,'id_medico':id_medico})

@login_required(login_url="/login")
def createncion(request,paciente):


	if request.method == 'GET':
		
		paciente = Pacientes.objects.get(id=paciente)


		medicos = Medicos.objects.all()

		c = Citas.objects.filter(paciente_id=paciente)

		a = Atencion.objects.filter(paciente_id=paciente)

		t = Tratamiento.objects.filter(paciente_id=paciente)


		# form = MedicosForm()
		# _medicos = Medicos.objects.all()

		# npacientes = Pacientes.objects.all().count()

		# ncitas = Citas.objects.all().count()

		# natenciones= Atencion.objects.all().count()



		# ncitashoy = Citas.objects.filter(start__gte=datetime.today()).count()


		return render(request, 'atencion.html',{'t':t,'user':traeeluser(request),'grupo':traeelgrupo(request),'paciente':paciente,'medicos':medicos,'citas':c,'atencion':a})

	if request.method == 'POST':

		p = Pacientes.objects.get(id=paciente)


		data = request.POST

		descripcion = data['descripcion']
		start = data['start']
		medico = data['medico']

		Atencion(paciente_id=paciente,descripcion=descripcion,fecha=start,medicos_id=medico).save()

		return HttpResponseRedirect('/createncion/'+paciente)
		#return render(request, 'creacita.html',{'paciente':p})


@login_required(login_url="/login")
def creacita(request,paciente):


	if request.method == 'GET':
		
		paciente = Pacientes.objects.get(id=paciente)


		medicos = Medicos.objects.all()

		c = Citas.objects.filter(paciente_id=paciente)

		a = Atencion.objects.filter(paciente_id=paciente)

		t = Tratamiento.objects.filter(paciente_id=paciente)


		# form = MedicosForm()
		# _medicos = Medicos.objects.all()

		# npacientes = Pacientes.objects.all().count()

		# ncitas = Citas.objects.all().count()

		# natenciones= Atencion.objects.all().count()



		# ncitashoy = Citas.objects.filter(start__gte=datetime.today()).count()


		return render(request, 'creacita.html',{'t':t,'user':traeeluser(request),'grupo':traeelgrupo(request),'paciente':paciente,'medicos':medicos,'citas':c,'atencion':a})

	if request.method == 'POST':

		p = Pacientes.objects.get(id=paciente)


		data = request.POST

		descripcion = data['descripcion']
		start = data['start']
		medico = data['medico']

		Citas(paciente_id=paciente,descripcion=descripcion,start=start,medico_id=medico).save()

		return HttpResponseRedirect('/creacita/'+paciente)
		#return render(request, 'creacita.html',{'paciente':p})






@login_required(login_url="/login")
def medico(request):


	form = MedicosForm()
	_medicos = Medicos.objects.all()

	npacientes = Pacientes.objects.all().count()

	ncitas = Citas.objects.all().count()

	natenciones= Atencion.objects.all().count()



	ncitashoy = Citas.objects.filter(start__gte=datetime.today()).count()


	return render(request, 'medico.html',{'user':traeeluser(request),'grupo':traeelgrupo(request),'form':  form,'medicos':_medicos})
 
@login_required(login_url="/login")

def dashboard(request):

	u = User.objects.get(id=request.user.id)

	grupo =u.groups.get()

	npacientes = Pacientes.objects.filter(fecha_ini=date.today()).count()

	ncitas = Citas.objects.all().count()

	natenciones= Atencion.objects.all().count()

	#ncitashoy = Citas.objects.annotate(Count('start')).count()
	ncitashoy = Citas.objects.filter(start__gte=date.today()).count()

	return render(request,'dashboard.html',{'user':traeeluser(request),'grupo':traeelgrupo(request),'natenciones':natenciones,'npacientes':npacientes,'ncitashoy':ncitashoy,'ncitas':ncitas})


@login_required(login_url="/login")

def dashboard(request):

	u = User.objects.get(id=request.user.id)

	grupo =u.groups.get()

	npacientes = Pacientes.objects.filter(fecha_ini=date.today()).count()

	ncitas = Citas.objects.all().count()

	natenciones= Atencion.objects.all().count()

	#ncitashoy = Citas.objects.annotate(Count('start')).count()

	ncitashoy = Citas.objects.filter(start__gte=date.today()).count()

	return render(request,'dashboard.html',{'user':traeeluser(request),'grupo':traeelgrupo(request),'natenciones':natenciones,'npacientes':npacientes,'ncitashoy':ncitashoy,'ncitas':ncitas})


def editcita(request,id_cita):

	if request.method == 'POST':

		a=Citas.objects.get(id=id_cita)

		form = CitasForm(request.POST, instance=a)


		if form.is_valid():

			print 'validoooooo'

			f = CitasForm(request.POST, instance=a).save()


			return HttpResponseRedirect('/cita')

	    # if a GET (or any other method) we'll create a blank form
	else:


		m=Citas.objects.get(id=id_cita)
		
		form = CitasForm(instance=m)

	return render(request, 'nuevacita.html',{'user':traeeluser(request),'grupo':traeelgrupo(request),'form': form,'cita':m,'id_cita':id_cita})



def editconsulta(request,id_consulta):

	if request.method == 'POST':

		a=Consulta.objects.get(id=id_cita)

		form = ConsultaForm(request.POST, instance=a)


		if form.is_valid():

			print 'validoooooo'

			f = ConsultaForm(request.POST, instance=a).save()


			return HttpResponseRedirect('/consulta')

	    # if a GET (or any other method) we'll create a blank form
	else:


		m=Consulta.objects.get(id=id_consulta)
		
		form = ConsultaForm(instance=m)

	return render(request, 'nuevaconsulta.html',{'user':traeeluser(request),'grupo':traeelgrupo(request),'form': form,'consulta':m,'id_consulta':id_consulta})





def nuevopaciente(request):

	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = PacientesForm(request.POST)

		# Create and save the new author instance. There's no need to do anything else.


	# check whether it's valid:
		if form.is_valid():

			a = Pacientes()


			p = PacientesForm(request.POST, instance=a).save()

			# Atencion(paciente_id=p.id).save()

			# id_a = Atencion.objects.all().values('id').order_by('-id')[0]['id']

			# a = Atencion.objects.get(id=id_a)

			# form = AtencionForm(instance=a)


			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:

			return HttpResponseRedirect('/paciente/')

			#return render(request, 'atencion.html',{'msj': 'El paciente se guardo con exito ','form':form})

	else:
		form = PacientesForm()

	return render(request, 'nuevopaciente.html',{'user':traeeluser(request),'grupo':traeelgrupo(request),'form': form})





def ingresar(request):

    username = request.POST['username']
    password = request.POST['password']

    print username,password
    user = authenticate(username=username, password=password)
    if user is not None:

        login(request, user)


        return HttpResponseRedirect('/dashboard/')

    else:


    	return render(request, 'login.html',{'error': 'No existe este usuario'})



def nuevomedico(request):

	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = MedicosForm(request.POST)

		# Create and save the new author instance. There's no need to do anything else.


	# check whether it's valid:
		if form.is_valid():

			a = Medicos()

			f = MedicosForm(request.POST, instance=a).save()


			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return HttpResponseRedirect('/nuevomedico/')

	    # if a GET (or any other method) we'll create a blank form
	else:
		form = MedicosForm()

	return render(request, 'nuevomedico.html',{'form': form})


def atencion(request):

	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = AtencionForm(request.POST)

		# Create and save the new author instance. There's no need to do anything else.


	# check whether it's valid:
		if form.is_valid():

			a = Atencion()

			f = AtencionForm(request.POST, instance=a).save()
			
			npacientes = Pacientes.objects.all().count()

			ncitas = Citas.objects.all().count()

			natenciones= Atencion.objects.all().count()



			ncitashoy = Citas.objects.filter(start__gte=datetime.datetime.today()).count()

			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return HttpResponseRedirect('/atencion/')

	    # if a GET (or any other method) we'll create a blank form
	else:
		form = AtencionForm()

	return render(request, 'atencion.html',{'user':traeeluser(request),'grupo':traeelgrupo(request),'form': form})



def pagos(request):

	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = AtencionForm(request.POST)

		# Create and save the new author instance. There's no need to do anything else.


	# check whether it's valid:
		if form.is_valid():

			a = Pagos()

			f = PagosForm(request.POST, instance=a).save()


			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return HttpResponseRedirect('/pagos/')

	    # if a GET (or any other method) we'll create a blank form
	else:
		form = PagosForm()

	return render(request, 'pagos.html',{'user':traeeluser(request),'grupo':traeelgrupo(request),'form': form})


def nuevaconsulta(request,id_paciente):

	if request.method == 'POST':
	# create a form instance and populate it with data from the request:

		paciente = Pacientes.objects.get(id=id_paciente)
		departamento =request.POST['departamento']

		print 'departamente',departamento
		tipo=request.POST['tipo']
		hora=request.POST['hora']
		origen=request.POST['origen']
		asistencia=request.POST['asistencia']
		fecha = request.POST['fecha']

		p =Pacientes.objects.get(id=id_paciente)


		Consulta(paciente_id=paciente.id,departamento_id=departamento,tipo_id=tipo,fecha_ini=fecha,origen_id=origen,asistencia_id=asistencia,).save()

		return HttpResponseRedirect('/consulta/')

	# 	form = ConsultaForm(request.POST)

	# 	# Create and save the new author instance. There's no need to do anything else.


	# # check whether it's valid:
	# 	if form.is_valid():

	# 		a = Consulta()

	# 		f = ConsultaForm(request.POST, instance=a).save()


	# 		# process the data in form.cleaned_data as required
	# 		# ...
	# 		# redirect to a new URL:
	# 		return HttpResponseRedirect('/consulta/')

	#     # if a GET (or any other method) we'll create a blank form
	else:
		form = ConsultaForm()

		p =Pacientes.objects.get(id=id_paciente)

		return render(request, 'nuevaconsulta.html',{'paciente':p,'user':traeeluser(request),'grupo':traeelgrupo(request),'form': form})


@login_required(login_url="/login")
def creatratamiento(request,paciente):


	if request.method == 'GET':
		
		paciente = Pacientes.objects.get(id=paciente)


		medicos = Medicos.objects.all()

		c = Citas.objects.filter(paciente_id=paciente)

		a = Atencion.objects.filter(paciente_id=paciente)

		t = Tratamiento.objects.filter(paciente_id=paciente)


		form = TratamientoForm()
		# _medicos = Medicos.objects.all()

		# npacientes = Pacientes.objects.all().count()

		# ncitas = Citas.objects.all().count()

		# natenciones= Atencion.objects.all().count()



		# ncitashoy = Citas.objects.filter(start__gte=datetime.today()).count()


		return render(request, 'creatratamiento.html',{'t':t,'form':form,'user':traeeluser(request),'grupo':traeelgrupo(request),'paciente':paciente,'medicos':medicos,'citas':c,'atencion':a})

	if request.method == 'POST':

		form = ConsultaForm(request.POST)

		# Create and save the new author instance. There's no need to do anything else.


	# check whether it's valid:
		if form.is_valid():

			a = Tratamiento()

			f = TratamientoForm(request.POST, instance=a).save()


			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return HttpResponseRedirect('/creatratamiento/'+paciente)
		
		#return render(request, 'creacita.html',{'paciente':p})
