Log_r(models.Models):
	action =models.CharField(max_length=300,blank=True)
	user = models.ForeignKey('User',max_length=300,blank=True, null=True)
	paciente = models.ForeignKey('Pacientes',max_length=300,blank=True, null=True)

    	departamento=  models.ForeignKey('Departamento',max_length=300,blank=True, null=True)
    	hora = models.TimeField(blank=True, null=True)

    	fecha_ini= models.DateTimeField(blank=True, null=True)
    
    	#medicos = models.ForeignKey('Medicos',max_length=300,blank=True, 	null=True)
    	#consulta = models.ForeignKey('Consulta',max_length=300,blank=True, 	null=True)
    	tipo = models.ForeignKey('Tipo',max_length=300,blank=True, null=True)
    	origen = models.ForeignKey('Origen',max_length=300,blank=True, 	null=True)
    	asistencia = models.ForeignKey('Asistencia',max_length=300,blank=True, 	null=True)

    	def __str__(self):

        		return self.nombre
        	class Meta:
        		managed =True
        		verbose_name ='log_nuevaconsulta'	


        		

        def save(self, *args,**kwargs):
        	Log_r(user=self.user, action='se creo una nueva consulta')
        	super(locales, self) .save(*args, **kwargs)
        	

    