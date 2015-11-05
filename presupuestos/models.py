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
	referencia_clave = models.CharField(max_length=100, blank='true',default='S-P')
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
	
class Familia (models.Model):
	nombre_familia= models.CharField(max_length=100)
	def __str__(self):
		return self.nombre_familia
	
class Parametro (models.Model):
	nombre_par = models.CharField('Parametro', max_length=100)
	familia = models.ForeignKey(Familia)
	def __str__(self):
		return self.nombre_par
	
class Tecnica (models.Model):
	nombre_tec = models.CharField('Tecnica', max_length=100)
	derivacion= models.CharField(max_length=100, blank='true')
	link = models.CharField(max_length=100, blank='true')
	observacion = models.CharField(max_length=100, blank='true')
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
	fecha_de_precio = models.DateField('Fecha del precio')
	
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

class Grupo_Parametro (models.Model):
	nombre_gparametro = models.CharField(max_length=100)
	def __str__(self):
		return self.nombre_gparametro
	
class GrupoParametroPrecio (models.Model):
	
	matriz = models.ForeignKey(Matriz)
	grupo_parametro  = models.ForeignKey(Grupo_Parametro)
	tecnica = models.ForeignKey(Tecnica)
	precio_del_grupo = models.DecimalField(max_digits=8, decimal_places=2)
	fecha_de_precio = models.DateField('Fecha del precio')
	
class GrupoParametroPrecio_Parametro (models.Model):
	grupoparametroprecio = models.ForeignKey(GrupoParametroPrecio)
	parametro = models.ForeignKey(Parametro)
	#todo:agregar inferida de unidades y lct, que vienen de matriztecnicalct
	
