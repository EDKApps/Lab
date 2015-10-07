 # -- coding: utf-8 --
from django import forms
from django.core.urlresolvers import reverse, reverse_lazy
from django.forms.extras.widgets import SelectDateWidget
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
presupuesto_fields = ('cliente','referencia', 'tipo', 'fecha_de_solicitud', 'fecha_de_aprobacion', 'descripcion', 'estado', 'observacion')
fecha_solicitud_anios = ('2015', '2016', '2017')
from .models import Presupuesto

#Presupuesto
class PresupuestoListar(ListView):
    model = Presupuesto
	#context_object_name = 'lista_de_presupuestos' #opcion a object_list

#class CrearForm(forms.ModelForm):
#    class Meta:
#        model = Presupuesto
#        fields = ['cliente','referencia','fecha_de_solicitud'] #presupuesto_fields
#        #fields[2].widget = forms.DateField(widget=SelectDateWidget(empty_label="Nothing"))

class PresupuestoForm(forms.ModelForm):
    #cliente lo uso por defecto
    #fecha_de_solicitud = forms.DateField(widget=SelectDateWidget(empty_label="Nothing"))
    fecha_de_solicitud = forms.DateInput(attrs={'class':'datepicker'})
    fecha_de_aprobacion = forms.DateInput(attrs={'class':'datepicker'})
	#Una clase inline para proveer información adicional en el formulario
    class Meta:
        #Provee una asociación entre el ModelForm y un model
        model = Presupuesto
        fields = presupuesto_fields	
		
		
class PresupuestoCrear(CreateView):
    model = Presupuesto
    success_url = reverse_lazy('presupuestos:presupuesto_listar')
    form_class = PresupuestoForm

	

class PresupuestoDetalle(DetailView):
    model = Presupuesto
    fields = presupuesto_fields

class PresupuestoModificar(UpdateView):
    model = Presupuesto
    #fields = presupuesto_fields
    form_class = PresupuestoForm
	
    def get_success_url(self):
        return reverse('presupuestos:presupuesto_detalle', kwargs={
            'pk': self.object.pk,
        })

class PresupuestoBorrar(DeleteView):
    model = Presupuesto
    success_url = reverse_lazy('presupuestos:presupuesto_listar')
    fields = presupuesto_fields
