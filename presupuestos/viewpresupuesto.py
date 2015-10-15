 # -- coding: utf-8 --
from django import forms
from django.core.urlresolvers import reverse, reverse_lazy
from django.forms.extras.widgets import SelectDateWidget
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
#En el form de alta excluyo la referencia (automática)
presupuesto_fields_crear = ('cliente','referencia_clave', 'tipo', 'fecha_de_solicitud',
                      'fecha_de_aprobacion','fecha_de_vencimiento', 'descripcion', 'estado', 'observacion')
presupuesto_fields_modif = ('cliente','referencia_clave', 'referencia', 'tipo', 'fecha_de_solicitud',
                      'fecha_de_aprobacion','fecha_de_vencimiento', 'descripcion', 'estado', 'observacion')

fecha_solicitud_anios = ('2015', '2016', '2017')
from .models import Presupuesto

#Presupuesto
class PresupuestoListar(ListView):
    model = Presupuesto
    paginate_by = 5
	#context_object_name = 'lista_de_presupuestos' #opcion a object_list

class PresupuestoFormCrear(forms.ModelForm):
    class Meta:
        #Provee una asociación entre el ModelForm y un model
        model = Presupuesto
        fields = presupuesto_fields_crear	

class PresupuestoFormModificar(forms.ModelForm):
    referencia = forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        #Provee una asociación entre el ModelForm y un model
        model = Presupuesto
        fields = presupuesto_fields_modif	

		
class PresupuestoCrear(CreateView):
    model = Presupuesto
    form_class = PresupuestoFormCrear

    def get_success_url(self):
        return reverse('presupuestos:presupuesto_detalle', kwargs={
            'pk': self.object.pk,
        })
	
class PresupuestoDetalle(DetailView):
    model = Presupuesto
    fields = presupuesto_fields_modif

class PresupuestoModificar(UpdateView):
    model = Presupuesto
    #fields = presupuesto_fields
    form_class = PresupuestoFormModificar
	
    def get_success_url(self):
        return reverse('presupuestos:presupuesto_detalle', kwargs={
            'pk': self.object.pk,
        })

class PresupuestoBorrar(DeleteView):
    model = Presupuesto
    success_url = reverse_lazy('presupuestos:presupuesto_listar')
    fields = presupuesto_fields_modif
