# forms.py
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import GrupoParametroPrecio, GrupoParametroPrecio_Parametro

class GrupoParametroPrecioForm(ModelForm):
	class Meta:
		model = GrupoParametroPrecio
		fields = ('matriz','grupo_parametro','tecnica','precio_del_grupo','fecha_de_precio')

class Gpp_Parametro_Form(ModelForm):
	class Meta:
		model = GrupoParametroPrecio_Parametro
		fields= '__all__'

	def save(self, commit=True):
		#food_name =  self.cleaned_data['food_name']
		#name, _ = Food.objects.get_or_create(name=food_name)
		instance = super(Gpp_Parametro_Form, self).save(commit=False)
		#instance.food = name
		if commit:
			instance.save()
		return instance 

GrupoParametroPrecio_ParametroFormSet = inlineformset_factory(GrupoParametroPrecio, GrupoParametroPrecio_Parametro, fields='__all__')