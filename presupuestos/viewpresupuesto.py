 # -- coding: utf-8 --
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
presupuesto_fields = ('cliente','referencia', 'tipo', 'fecha_de_solicitud', 'fecha_de_aprobacion', 'descripcion', 'estado', 'observacion')

from .models import Presupuesto

#Presupuesto
class PresupuestoListar(ListView):
    model = Presupuesto
	#context_object_name = 'lista_de_presupuestos' #opcion a object_list

class PresupuestoCrear(CreateView):
    model = Presupuesto
    success_url = reverse_lazy('presupuestos:presupuesto_listar')
    fields = presupuesto_fields

class PresupuestoDetalle(DetailView):
    model = Presupuesto
    fields = presupuesto_fields

class PresupuestoModificar(UpdateView):
    model = Presupuesto
    fields = presupuesto_fields
	
    def get_success_url(self):
        return reverse('presupuestos:presupuesto_detalle', kwargs={
            'pk': self.object.pk,
        })

class PresupuestoBorrar(DeleteView):
    model = Presupuesto
    success_url = reverse_lazy('presupuestos:presupuesto_listar')
    fields = presupuesto_fields
