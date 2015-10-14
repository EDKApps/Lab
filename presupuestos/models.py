 # -- coding: utf-8 --
	
# $ python manage.py makemigrations
# $ python manage.py migrate
# $ python manage.py createsuperuser
# $ python manage.py sqlmigrate rango 0001
# $ python manage.py runserver

from django.db import models

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
	referencia = models.CharField(max_length=100, blank='true')
	fecha_de_solicitud = models.DateField('fecha de solicitud')
	fecha_de_aprobacion = models.DateField('fecha de aprobacion')
	#fecha_de_solicitud = models.DateTimeField('')
	#fecha_de_aprobacion = models.DateTimeField('')
	descripcion = models.CharField(max_length=100)
	tipo = models.ForeignKey(Tipo)
	estado = models.ForeignKey(Estado)
	observacion = models.CharField(max_length=100, blank='true')
	"""def __str__(self):
		return self.fecha_de_solicitud"""
	def __str__(self):
		return self.referencia

