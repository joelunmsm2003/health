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


from datetime import datetime,timedelta
from django.contrib.auth import authenticate

from django.contrib.sites.shortcuts import get_current_site

from .forms import *

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


	
	return render(request, 'calendar.html',{})


def home(request):


	
	return render(request, 'index.html',{})

def login(request):


	
	return render(request, 'login.html',{})



def nuevacita(request):

	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = ContactForm(request.POST)
	# check whether it's valid:
		if form.is_valid():
			print form

			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return HttpResponseRedirect('/thanks/')

	    # if a GET (or any other method) we'll create a blank form
	else:
		form = ConsultaForm()
	
	return render(request, 'nuevacita.html',{'form': form})



def paciente(request):


	form = PacienteForm()


	return render(request, 'paciente.html',{'form': form})


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