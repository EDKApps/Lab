 # -- coding: utf-8 --
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q #para OR en consultas

from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
tecnica_fields = ('nombre_tec','derivacion','link','observacion')

from .models import Tecnica

class TecnicaListar(ListView):
    model = Tecnica
    paginate_by = 10
    
    #búsqueda
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is None:
            return Tecnica.objects.all()
        else:
            return Tecnica.objects.filter( Q(nombre_tec__icontains=query) | 
                                             Q(derivacion__icontains=query))
    #almacenar contexto de la búsqueda
    def get_context_data(self, **kwargs):
        context = super(TecnicaListar, self).get_context_data(**kwargs)
        q = self.request.GET.get('q')
        if q: #si existe el valor, lo agrego/actualizo en el contexto
            q = q.replace(" ","+")
            context['query'] = q
        return context    
    
class TecnicaCrear(CreateView):
    model = Tecnica
    fields = tecnica_fields
	
    def get_success_url(self):
        return reverse('presupuestos:tecnica_detalle', kwargs={
            'pk': self.object.pk,
        })

class TecnicaDetalle(DetailView):
    model = Tecnica
    fields = tecnica_fields

class TecnicaModificar(UpdateView):
    model = Tecnica
    fields = tecnica_fields
	
    def get_success_url(self):
        return reverse('presupuestos:tecnica_detalle', kwargs={
            'pk': self.object.pk,
        })

class TecnicaBorrar(DeleteView):
    model = Tecnica
    success_url = reverse_lazy('presupuestos:tecnica_listar')
    fields = tecnica_fields