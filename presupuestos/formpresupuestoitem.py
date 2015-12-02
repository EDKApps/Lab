from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Presupuesto, Item

class PresupuestoForm(ModelForm):
	class Meta:
		model = Presupuesto
		fields = '__all__'

class Presupuesto_Item_Form(ModelForm):
	class Meta:
		model = Item
		fields= '__all__'

	def save(self, commit=True):
		instance = super(Presupuesto_Item_Form, self).save(commit=False)
		if commit:
			instance.save()
		return instance 

Presupuesto_ItemFormSet = inlineformset_factory(Presupuesto, Item, fields='__all__')