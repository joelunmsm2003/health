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

	_consulta = Consulta.objects.all()
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


def busqueda(request):

	nombre = request.GET['dato']

	#p=Pacientes.objects.filter(dni__search=nombre)

	p=Pacientes.objects.filter(nombre__contains=nombre)

	
	return render(request, 'paciente.html',{'pacientes':p})


def busquedacita(request):

	paciente = request.GET['dato']

	#p=Pacientes.objects.filter(dni__search=nombre)

	c=Citas.objects.filter(paciente__nombre__contains=paciente)

	
	return render(request, 'index.html',{'citas':c})


def busquedamedico(request):

	nombre= request.GET['dato']

	#p=Pacientes.objects.filter(dni__search=nombre)

	m=Medicos.objects.filter(nombre__contains=nombre)

	
	return render(request, 'medico.html',{'medicos':m})


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


		fecha = str(request.POST['start'])+' '+str(request.POST['starthora'])



		fecha = datetime.strptime(fecha, '%Y-%m-%d %H:%M')

								

		# Create and save the new author instance. There's no need to do anything else.


	# check whether it's valid:
		if form.is_valid():

			a = Citas()

			f = CitasForm(request.POST, instance=a).save()

			id_c = Citas.objects.all().values('id').order_by('-id')[0]['id']

			c = Citas.objects.get(id=id_c)

			c.start = fecha
	
			c.save()



			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return HttpResponseRedirect('/dashboard')

	    # if a GET (or any other method) we'll create a blank form
	else:

		form = CitasForm()

		u = User.objects.get(id=request.user.id)

		grupo =u.groups.get()



	return render(request, 'nuevacita.html',{'form': form,'grupo':grupo})


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


		p=Pacientes.objects.get(id=id_paciente)
		
		form = PacientesForm(instance=p)

	return render(request, 'editpaciente.html',{'form': form,'id_paciente':id_paciente})


def paciente(request):


	form = PacientesForm()

	_pacientes = Pacientes.objects.all()

	u = User.objects.get(id=request.user.id)

	grupo =u.groups.get()

	npacientes = Pacientes.objects.all().count()

	ncitas = Citas.objects.all().count()

	natenciones= Atencion.objects.all().count()

	ncitashoy = Citas.objects.filter(start__gte=datetime.today()).count()


	return render(request, 'paciente.html',{'form': form,'pacientes':_pacientes,'user':u,'grupo':grupo,'natenciones':natenciones,'npacientes':npacientes,'ncitashoy':ncitashoy,'ncitas':ncitas})


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



	return render(request, 'index.html',{'form': form,'citas':_citas,'user':u,'grupo':grupo,'natenciones':natenciones,'npacientes':npacientes,'ncitashoy':ncitashoy,'ncitas':ncitas})

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

	return render(request, 'editmedico.html',{'form': form,'id_medico':id_medico})






def medico(request):


	form = MedicosForm()
	_medicos = Medicos.objects.all()

	npacientes = Pacientes.objects.all().count()

	ncitas = Citas.objects.all().count()

	natenciones= Atencion.objects.all().count()



	ncitashoy = Citas.objects.filter(start__gte=datetime.today()).count()


	return render(request, 'medico.html',{'form':  form,'medicos':_medicos})
 

def dashboard(request):

	u = User.objects.get(id=request.user.id)

	grupo =u.groups.get()
	print "nnnnnn",datetime

	npacientes = Pacientes.objects.filter(fecha_ini=date.today()).count()

	ncitas = Citas.objects.all().count()

	natenciones= Atencion.objects.all().count()


	print "TIGREZHITO",date.today()
	#ncitashoy = Citas.objects.annotate(Count('start')).count()
	ncitashoy = Citas.objects.filter(start__gte=date.today()).count()

	print "ttttttttttttttttttt",ncitashoy

	
	
	return render(request,'dashboard.html',{'user':u,'grupo':grupo,'natenciones':natenciones,'npacientes':npacientes,'ncitashoy':ncitashoy,'ncitas':ncitas})




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

	return render(request, 'nuevacita.html',{'form': form,'cita':m,'id_cita':id_cita})


def nuevopaciente(request):

	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = PacientesForm(request.POST)

		# Create and save the new author instance. There's no need to do anything else.


	# check whether it's valid:
		if form.is_valid():

			a = Pacientes()


			p = PacientesForm(request.POST, instance=a).save()

			Atencion(paciente_id=p.id).save()

			id_a = Atencion.objects.all().values('id').order_by('-id')[0]['id']

			a = Atencion.objects.get(id=id_a)

			form = AtencionForm(instance=a)





			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return render(request, 'atencion.html',{'msj': 'Paciente se guardaron con exito  ;)  ','form':form})



	else:
		form = PacientesForm()

	return render(request, 'nuevopaciente.html',{'form': form})





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

	return render(request, 'atencion.html',{'form': form})



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

	return render(request, 'pagos.html',{'form': form})


def nuevaconsulta(request):

	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = ConsultaForm(request.POST)

		# Create and save the new author instance. There's no need to do anything else.


	# check whether it's valid:
		if form.is_valid():

			a = Consulta()

			f = ConsultaForm(request.POST, instance=a).save()


			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return HttpResponseRedirect('/nuevaconsulta/')

	    # if a GET (or any other method) we'll create a blank form
	else:
		form = ConsultaForm()

	return render(request, 'nuevaconsulta.html',{'form': form})

