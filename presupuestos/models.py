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
	contacto = models.CharField('Contacto (apellido, nombre)', max_length=200)
	funcion = models.CharField(max_length=100, blank='true')
	domicilio = models.CharField(max_length=100, blank='true')
	localidad = models.CharField(max_length=200, blank='true')
	telefono_fijo = models.CharField(max_length=100, blank='true')
	telefono_movil = models.CharField(max_length=100, blank='true')
	email = models.CharField(max_length=100, blank='true')
	cuit = models.CharField(max_length=13, blank='true')
	nota = models.CharField(max_length=200, blank='true')
	def __str__(self):
		return self.contacto+', '+self.empresa
	
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
	referencia_clave = models.CharField(max_length=100, blank='true',default='S-P')
	referencia = models.CharField(max_length=20,blank='true') #autoincremental
	fecha_solicitud = models.DateField('fecha de solicitud', default=date.today)
	fecha_vencimiento = models.DateField('fecha de vencimiento', blank='true', null='true')
	fecha_envio = models.DateField('fecha de envio', blank='true', null='true')
	fecha_aprobacion = models.DateField('fecha de aprobacion', blank='true', null='true')
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
			self.referencia = str(sigNumero('presupuesto_referencia'))
			
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


class Matriz (models.Model):
	nombre_matriz = models.CharField(max_length=100)
	def __str__(self):
		return self.nombre_matriz
	
class Familia (models.Model): # también llamada Grupo
	nombre= models.CharField(max_length=100)
	def __str__(self):
		return self.nombre
	
class Parametro (models.Model):
	nombre_par = models.CharField('Parametro', max_length=100)
	familia = models.ForeignKey(Familia, blank='true', null='true')
	def __str__(self):
		return self.nombre_par
	
class Tecnica (models.Model):
	nombre_tec = models.CharField('Tecnica', max_length=100)
	derivacion= models.CharField(max_length=100, blank='true')
	link = models.CharField(max_length=100, blank='true')
	observacion = models.TextField(blank='true')
	def __str__(self):
		return self.nombre_tec
	
class Unidades (models.Model):
	nombre_unidad = models.CharField('Unidades', max_length=100)
	def __str__(self):
		return self.nombre_unidad

class MatrizTecnicaLct (models.Model):
	matriz = models.ForeignKey(Matriz)
	parametro = models.ForeignKey(Parametro)
	tecnica = models.ForeignKey(Tecnica)
	lct = models.DecimalField(max_digits=10, decimal_places=6)
	unidad = models.ForeignKey(Unidades)
	
	def __str__(self):
		return self.matriz.nombre_matriz+', '+self.parametro.nombre_par+', '+self.tecnica.nombre_tec
	
class ParametroPrecio  (models.Model):
	matriz = models.ForeignKey(Matriz)
	parametro = models.ForeignKey(Parametro)
	tecnica = models.ForeignKey(Tecnica)
	precio_del_parametro = models.DecimalField(max_digits=8, decimal_places=2)
	fecha_de_precio = models.DateField('Fecha del precio', default=date.today)
	
	#def familia(self): todo: (Inferido) a partir del parametro retornar su familia
		
	def lcm(self):
		try:
			mt = MatrizTecnicaLct.objects.get(matriz=self.matriz, parametro=self.parametro, tecnica=self.tecnica)
		except MatrizTecnicaLct.DoesNotExist:
			return 0
		else:
			return mt.lct
	def uni(self):
		try:
			mt = MatrizTecnicaLct.objects.get(matriz=self.matriz, parametro=self.parametro, tecnica=self.tecnica)
		except MatrizTecnicaLct.DoesNotExist:
			return ''
		else:
			return mt.unidad
	
class PerfilPrecio (models.Model): # ex GrupoParametroPrecio
	nombre = models.CharField( max_length=100)
	matriz = models.ForeignKey(Matriz)
	precio = models.DecimalField(max_digits=8, decimal_places=2)
	fecha_precio = models.DateField('Fecha del precio')
	def __str__(self):
		return self.nombre

class PerfilPrecio_Parametro (models.Model): # ex GrupoParametroPrecio_Parametro
	perfilPrecio = models.ForeignKey(PerfilPrecio)
	parametro = models.ForeignKey(Parametro)
	tecnica = models.ForeignKey(Tecnica)	
	
	#todo:agregar inferida de unidades y lct, que vienen de matriztecnicalct
	
class Item (models.Model):
	numero = models.IntegerField(default= 0)
	descripcion = models.CharField(max_length= 100, blank='true')
	matriz = models.ForeignKey(Matriz)
	cantidadMuestra = models.IntegerField(default= 0)
	def __str__(self):
		return self.descripcion

class Campania (models.Model):
	descripcion = models.CharField(max_length= 100)
	cantidad = models.IntegerField(default='0')
	unidad_medida = models.CharField(max_length= 100, blank='true')
	valor_unitario = models.DecimalField(max_digits=8, decimal_places=2)
	valor_total = models.DecimalField(max_digits=8, decimal_places=2)
