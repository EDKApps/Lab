# forms.py
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import PerfilPrecio, PerfilPrecio_Parametro

class PerfilPrecioForm(ModelForm):
	class Meta:
		model = PerfilPrecio
		fields = ('nombre','matriz','precio','fecha_precio')

class Perfil_Parametro_Form(ModelForm):
	class Meta:
		model = PerfilPrecio_Parametro
		fields= '__all__'

	def save(self, commit=True):
		#food_name =  self.cleaned_data['food_name']
		#name, _ = Food.objects.get_or_create(name=food_name)
		instance = super(Perfil_Parametro_Form, self).save(commit=False)
		#instance.food = name
		if commit:
			instance.save()
		return instance 

PerfilPrecio_ParametroFormSet = inlineformset_factory(PerfilPrecio, PerfilPrecio_Parametro, fields='__all__')