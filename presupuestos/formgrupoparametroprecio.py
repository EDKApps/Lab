# forms.py
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import GrupoParametroPrecio, GrupoParametroPrecio_Parametro

class GrupoParametroPrecioForm(ModelForm):
	class Meta:
		model = GrupoParametroPrecio
		fields = ('matriz','grupo_parametro','tecnica','precio_del_grupo','fecha_de_precio')

GrupoParametroPrecio_ParametroFormSet = inlineformset_factory(GrupoParametroPrecio, GrupoParametroPrecio_Parametro, fields='__all__')