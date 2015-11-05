 # -- coding: utf-8 --
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q #para OR en consultas

from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
grupo_parametro_fields = ('nombre_gparametro',)

from .models import Grupo_Parametro

class GrupoParametroListar(ListView):
    model = Grupo_Parametro
    paginate_by = 10
    
    #búsqueda
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is None:
            return Grupo_Parametro.objects.all()
        else:
            return Grupo_Parametro.objects.filter( Q(nombre_gparametro__icontains=query))
    #almacenar contexto de la búsqueda
    def get_context_data(self, **kwargs):
        context = super(GrupoParametroListar, self).get_context_data(**kwargs)
        q = self.request.GET.get('q')
        if q: #si existe el valor, lo agrego/actualizo en el contexto
            q = q.replace(" ","+")
            context['query'] = q
        return context    
    
class GrupoParametroCrear(CreateView):
    model = Grupo_Parametro
    fields = grupo_parametro_fields
	
    def get_success_url(self):
        return reverse('presupuestos:grupoparametro_detalle', kwargs={
            'pk': self.object.pk,
        })

class GrupoParametroDetalle(DetailView):
    model = Grupo_Parametro
    fields = grupo_parametro_fields

class GrupoParametroModificar(UpdateView):
    model = Grupo_Parametro
    fields = grupo_parametro_fields
	
    def get_success_url(self):
        return reverse('presupuestos:grupoparametro_detalle', kwargs={
            'pk': self.object.pk,
        })

class GrupoParametroBorrar(DeleteView):
    model = Grupo_Parametro
    success_url = reverse_lazy('presupuestos:grupoparametro_listar')
    fields = grupo_parametro_fields