 # -- coding: utf-8 --
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q #para OR en consultas

from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
grupoparametroprecio_fields = ('matriz','grupo_parametro','tecnica','precio_del_grupo','fecha_de_precio')

from .models import GrupoParametroPrecio

class GrupoParametroPrecioListar(ListView):
    model = GrupoParametroPrecio
    paginate_by = 10
    
    #búsqueda
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is None:
            return GrupoParametroPrecio.objects.all()
        else:
            return GrupoParametroPrecio.objects.filter( Q(matriz__nombre_matriz__icontains=query) | 
                                          Q(grupo_parametro__nombre_gparametro__icontains=query) | 
                                          Q(tecnica__nombre_tec__icontains=query)  )        
        
    #almacenar contexto de la búsqueda
    def get_context_data(self, **kwargs):
        context = super(GrupoParametroPrecioListar, self).get_context_data(**kwargs)
        q = self.request.GET.get('q')
        if q: #si existe el valor, lo agrego/actualizo en el contexto
            q = q.replace(" ","+")
            context['query'] = q
        return context    
    
class GrupoParametroPrecioCrear(CreateView):
    model = GrupoParametroPrecio
    fields = grupoparametroprecio_fields
    def get_success_url(self):
        return reverse('presupuestos:grupoparametroprecio_detalle', kwargs={
            'pk': self.object.pk,
        })

class GrupoParametroPrecioDetalle(DetailView):
    model = GrupoParametroPrecio
    fields = grupoparametroprecio_fields

class GrupoParametroPrecioModificar(UpdateView):
    model = GrupoParametroPrecio
    fields = grupoparametroprecio_fields
	
    def get_success_url(self):
        return reverse('presupuestos:grupoparametroprecio_detalle', kwargs={
            'pk': self.object.pk,
        })

class GrupoParametroPrecioBorrar(DeleteView):
    model = GrupoParametroPrecio
    success_url = reverse_lazy('presupuestos:grupoparametroprecio_listar')
    fields = grupoparametroprecio_fields