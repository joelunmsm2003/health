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

from .forms import *

from app.serializer import CitasSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse

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




def calendar(request):


	
	return render(request, 'calendar_1.html',{})


def home(request):


	
	return render(request, 'index.html',{})

def login2(request):


	
	return render(request, 'login.html',{})

def citasjson(request):




    serializer = CitasSerializer(Citas.objects.all(), many=True)
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

		# Create and save the new author instance. There's no need to do anything else.


	# check whether it's valid:
		if form.is_valid():

			a = Citas()

			f = CitasForm(request.POST, instance=a).save()


			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return HttpResponseRedirect('/nuevopaciente/')

	    # if a GET (or any other method) we'll create a blank form
	else:

		form = CitasForm()

	return render(request, 'nuevacita.html',{'form': form})



def paciente(request):


	form = PacienteForm()


	return render(request, 'paciente.html',{'form': form})

def medico(request):


	form = MedicosForm()


	return render(request, 'medico.html',{'form': form})
 

def dashboard(request):

	
	
	return render(request, 'dashboard.html',{})



def nuevopaciente(request):

	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = PacientesForm(request.POST)

		# Create and save the new author instance. There's no need to do anything else.


	# check whether it's valid:
		if form.is_valid():

			a = Pacientes()

			f = PacientesForm(request.POST, instance=a).save()


			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return HttpResponseRedirect('/nuevopaciente/')

	    # if a GET (or any other method) we'll create a blank form
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

