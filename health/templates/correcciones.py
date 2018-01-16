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

	return render(request, 'nuevacita.html',{'form': form,'id_cita':id_cita})



......................................................................................
def editcita(request,id_paciente):

	if request.method == 'POST':

		a=Citas.objects.get(id=id_cita)

		form = CitasForm(request.POST, instance=a)


		if form.is_valid():

			print 'validoooooo'

			f = CitasForm(request.POST, instance=a).save()


			return HttpResponseRedirect('/cita')

	    # if a GET (or any other method) we'll create a blank form
	else:


		m=Pacientes.objects.get(id=id_paciente)
		
		form = CitasForm()

	return render(request, 'nuevacita.html',{'form': form,'paciente':m})
