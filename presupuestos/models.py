 # -- coding: utf-8 --
# $ python manage.py makemigrations
# $ python manage.py migrate
# $ python manage.py createsuperuser
# $ python manage.py sqlmigrate rango 0001
# $ python manage.py runserver

from django.db import models
from datetime import date
from django.utils.encoding import python_2_unicode_compatible

#from .APINumerador import sigNumero

@python_2_unicode_compatible
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

@python_2_unicode_compatible
class Tipo (models.Model):
	nombre_tipo = models.CharField(max_length=100)
	def __str__(self):
		return self.nombre_tipo

@python_2_unicode_compatible
class Estado (models.Model):
	estado_actual = models.CharField(max_length=100)
	def __str__(self):
		return self.estado_actual
	
@python_2_unicode_compatible
class Presupuesto (models.Model):
	cliente = models.ForeignKey(Cliente, on_delete= models.PROTECT)
	referencia_clave = models.CharField(max_length=100, blank='true',default='S-P')
	referencia = models.CharField(max_length=20,blank='true') #autoincremental
	fecha_solicitud = models.DateField('fecha de solicitud', default=date.today)
	fecha_vencimiento = models.DateField('fecha de vencimiento', blank='true', null='true')
	fecha_envio = models.DateField('fecha de envio', blank='true', null='true')
	fecha_aprobacion = models.DateField('fecha de aprobacion', blank='true', null='true')
	descripcion = models.CharField(max_length=100)
	tipo = models.ForeignKey(Tipo,on_delete= models.PROTECT)
	estado = models.ForeignKey(Estado,on_delete= models.PROTECT)
	observacion = models.CharField(max_length=100, blank='true')
	descuento = models.DecimalField('descuento global (%)', max_digits=5, decimal_places=2, null='true', blank='true', default=0)

	def __str__(self):
		return self.referencia
	
	def save(self, *args, **kwargs):
		#si es insert (id= 0), asignar referencia autoincremental	
		if self.id is None:
			self.referencia = str(sigNumero('presupuesto_referencia'))
			
		super(Presupuesto, self).save(*args, **kwargs) # Call the "real" save() method.

@python_2_unicode_compatible
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

@python_2_unicode_compatible
class Matriz (models.Model):
	nombre_matriz = models.CharField(max_length=100)
	def __str__(self):
		return self.nombre_matriz

@python_2_unicode_compatible
class Familia (models.Model): # también llamada Grupo
	nombre= models.CharField(max_length=100)
	def __str__(self):
		return self.nombre
	
@python_2_unicode_compatible	
class Parametro (models.Model):
	nombre_par = models.CharField('Parametro', max_length=100)
	familia = models.ForeignKey(Familia, blank='true', null='true',on_delete= models.PROTECT )
	def __str__(self):
		return self.nombre_par
	
@python_2_unicode_compatible	
class Tecnica (models.Model):
	nombre_tec = models.CharField('Tecnica', max_length=100)
	derivacion= models.CharField(max_length=100, blank='true')
	link = models.CharField(max_length=100, blank='true')
	observacion = models.TextField(blank='true')
	def __str__(self):
		return self.nombre_tec

@python_2_unicode_compatible
class Unidades (models.Model):
	nombre_unidad = models.CharField('Unidades', max_length=100)
	def __str__(self):
		return self.nombre_unidad

@python_2_unicode_compatible
class MatrizTecnicaLct (models.Model):
	matriz = models.ForeignKey(Matriz, on_delete= models.PROTECT)
	parametro = models.ForeignKey(Parametro, on_delete= models.PROTECT)
	tecnica = models.ForeignKey(Tecnica, on_delete= models.PROTECT)
	lct = models.DecimalField(max_digits=10, decimal_places=6)
	unidad = models.ForeignKey(Unidades, on_delete= models.PROTECT)
	
	def __str__(self):
		return self.matriz.nombre_matriz+', '+self.parametro.nombre_par+', '+self.tecnica.nombre_tec

@python_2_unicode_compatible
class ParametroPrecio  (models.Model):
	matriz = models.ForeignKey(Matriz, on_delete= models.PROTECT)
	parametro = models.ForeignKey(Parametro, on_delete= models.PROTECT)
	tecnica = models.ForeignKey(Tecnica, on_delete= models.PROTECT)
	precio_del_parametro = models.DecimalField(max_digits=8, decimal_places=2)
	fecha_de_precio = models.DateField('Fecha del precio', default=date.today)
	seleccionado = models.BooleanField(default=False)
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
	def __str__(self):
		return self.parametro.nombre_par+', '+self.tecnica.nombre_tec

@python_2_unicode_compatible
class PerfilPrecio (models.Model): # ex GrupoParametroPrecio
	nombre = models.CharField( max_length=100)
	matriz = models.ForeignKey(Matriz, on_delete= models.PROTECT)
	precio = models.DecimalField(max_digits=8, decimal_places=2)
	fecha_precio = models.DateField('Fecha del precio')
	def __str__(self):
		return self.nombre

@python_2_unicode_compatible
class PerfilPrecio_Parametro (models.Model): # ex GrupoParametroPrecio_Parametro
	perfilPrecio = models.ForeignKey(PerfilPrecio, on_delete= models.PROTECT)
	parametro = models.ForeignKey(Parametro, on_delete= models.PROTECT)
	tecnica = models.ForeignKey(Tecnica, on_delete= models.PROTECT)	
	def __str__(self):
		return self.parametro.nombre_par
	#todo:agregar inferida de unidades y lct, que vienen de matriztecnicalct

@python_2_unicode_compatible
class Item (models.Model): #si se elimina el presupuesto. se elimina el Item, junto con sus subitems
	presupuesto = models.ForeignKey(Presupuesto)
	numero = models.IntegerField(default= 0)
	descripcion = models.CharField(max_length= 100, blank='true')
	matriz = models.ForeignKey(Matriz)
	cantidadMuestra = models.IntegerField(default= 0)
	def __str__(self):
		return self.descripcion

@python_2_unicode_compatible
class Subitem_parametro (models.Model): #relacion Item-ParametroPrecio
	item = models.ForeignKey(Item, null=True)
	itemparametro = models.ForeignKey(ParametroPrecio)
	
	def __str__(self):
		return self.itemparametro.parametro.nombre_par #lo agrego para cumplir con decorator python_2

@python_2_unicode_compatible
class Subitem_perfil (models.Model): #relacion Item-PerfilPrecio
	item = models.ForeignKey(Item, null=True)
	itemperfil = models.ForeignKey(PerfilPrecio)
	def __str__(self):
		return self.itemperfil.nombre #lo agrego para cumplir con decorator python_2
	
@python_2_unicode_compatible
class Campania (models.Model):
	presupuesto = models.ForeignKey(Presupuesto, on_delete= models.PROTECT, null=True)
	numero = models.IntegerField(default= 0)
	descripcion = models.CharField(max_length= 100)
	cantidad = models.IntegerField(default= 0)
	unidad_medida = models.CharField(max_length= 100, blank='true')
	valor_unitario = models.DecimalField(max_digits=8, decimal_places=2, default= 0)
	valor_total = models.DecimalField(max_digits=8, decimal_places=2, null='true', blank='true', default=0)
	descuento = models.DecimalField('descuento (%)', max_digits=5, decimal_places=2, null='true', blank='true', default=0)
	def __str__(self):
		return self.descripcion
	def save(self, *args, **kwargs):
		#completa valor_total
		total = self.valor_unitario * self.cantidad	
		if self.descuento != 0:
			total=total * (100-self.descuento)/100
		self.valor_total = total

		# Call the "real" save() method.
		super(Campania, self).save(*args, **kwargs) 
