 # -- coding: utf-8 --
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

cliente_fields = ('empresa','contacto_nombre','contacto_apellido',
			 'domicilio','telefono_fijo','telefono_movil',
			 'email','cuit','nota')

presupuesto_fields = ('cliente','referencia', 'tipo', 'fecha_de_solicitud', 'fecha_de_aprobacion', 'descripcion', 'estado', 'observacion')
	
from .models import Cliente
from .models import Presupuesto

class ClienteListar(ListView):
    model = Cliente
	#context_object_name = 'lista_de_clientes' #opción a object_list

class ClienteCrear(CreateView):
    model = Cliente
    success_url = reverse_lazy('presupuestos:cliente_listar')
    fields = cliente_fields

class ClienteDetalle(DetailView):
    model = Cliente
    fields = cliente_fields

class ClienteModificar(UpdateView):
    model = Cliente
    fields = cliente_fields
	
    def get_success_url(self):
        return reverse('presupuestos:cliente_detalle', kwargs={
            'pk': self.object.pk,
        })

class ClienteBorrar(DeleteView):
    model = Cliente
    success_url = reverse_lazy('presupuestos:cliente_listar')
    fields = cliente_fields
	
#Presupuesto
class PresupuestoListar(ListView):
    model = Presupuesto
	#context_object_name = 'lista_de_Presupuestos' #opción a object_list

class PresupuestoCrear(CreateView):
    model = Presupuesto
    success_url = reverse_lazy('presupuestos:Presupuesto_listar')
    fields = presupuesto_fields

class PresupuestoDetalle(DetailView):
    model = Presupuesto
    fields = presupuesto_fields

class PresupuestoModificar(UpdateView):
    model = Presupuesto
    fields = presupuesto_fields
	
    def get_success_url(self):
        return reverse('presupuestos:Presupuesto_detalle', kwargs={
            'pk': self.object.pk,
        })

class PresupuestoBorrar(DeleteView):
    model = Presupuesto
    success_url = reverse_lazy('presupuestos:Presupuesto_listar')
    fields = presupuesto_fields

	
	