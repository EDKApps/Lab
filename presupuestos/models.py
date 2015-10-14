 # -- coding: utf-8 --
	
# $ python manage.py makemigrations
# $ python manage.py migrate
# $ python manage.py createsuperuser
# $ python manage.py sqlmigrate rango 0001
# $ python manage.py runserver

from django.db import models
from datetime import date
#from .APINumerador import sigNumero

class Cliente (models.Model):
	empresa = models.CharField(max_length=100)
	contacto_nombre = models.CharField(max_length=100)
	contacto_apellido = models.CharField(max_length=100)
	domicilio = models.CharField(max_length=100, blank='true')
	telefono_fijo = models.CharField(max_length=100, blank='true')
	telefono_movil = models.CharField(max_length=100, blank='true')
	email = models.CharField(max_length=100, blank='true')
	cuit = models.CharField(max_length=13, blank='true')
	nota = models.CharField(max_length=200, blank='true')
	def __str__(self):
		return self.contacto_apellido+', '+self.contacto_nombre
	
class Tipo (models.Model):
	nombre_tipo = models.CharField(max_length=100)
	def __str__(self):
		return self.nombre_tipo
	
class Estado (models.Model):
	estado_actual = models.CharField(max_length=100)
	def __str__(self):
		return self.estado_actual
	

class Presupuesto (models.Model):
	cliente = models.ForeignKey(Cliente)
	referencia_clave = models.CharField(max_length=100, blank='true')#texto, por ejemplo 'S-P'
	referencia = models.CharField(max_length=20,blank='true') #autoincremental
	fecha_de_solicitud = models.DateField('fecha de solicitud')
	fecha_de_aprobacion = models.DateField('fecha de aprobacion')
	fecha_de_vencimiento = models.DateField('fecha de vencimiento',default=date.today)
	descripcion = models.CharField(max_length=100)
	tipo = models.ForeignKey(Tipo)
	estado = models.ForeignKey(Estado)
	observacion = models.CharField(max_length=100, blank='true')
	"""def __str__(self):
		return self.fecha_de_solicitud"""
	def __str__(self):
		return self.referencia
	
	def save(self, *args, **kwargs):
		#si es insert (id= 0), asignar referencia autoincremental	
		if self.id is None:
			#print ('>>>' + str(self.id))
			self.referencia = "SSPP " + str(sigNumero('presupuesto_referencia'))
			
		super(Presupuesto, self).save(*args, **kwargs) # Call the "real" save() method.

class Numerador (models.Model):
	nombre = models.CharField(max_length=30, blank='true',unique=True)
	ultimo_valor = models.IntegerField(default=0)
	def __str__(self):
		return self.nombre

def sigNumero(nombreNumerador):
	try:
		n = Numerador.objects.get(nombre=nombreNumerador)
	except Numerador.DoesNotExist:
		#Si no existe en la BD, lo creo
		n = Numerador(nombre=nombreNumerador, ultimo_valor = 1)
		n.save()
		return n.ultimo_valor
	else:
		#si existe, incremento el valor, lo guardo y lo retorno
		n.ultimo_valor += 1
		n.save()
		return n.ultimo_valor

#numerador, created = Numerador.objects.update_or_create(
#        identifier=identifier, defaults={"name": name}
#)
