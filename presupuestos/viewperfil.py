 # -- coding: utf-8 --
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q #para OR en consultas

from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
perfil_fields = ('nombre',)

from .models import Perfil

class PerfilListar(ListView):
    model = Perfil
    paginate_by = 10
    
    #búsqueda
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is None:
            return Perfil.objects.all()
        else:
            return Perfil.objects.filter( Q(nombre__icontains=query))
    #almacenar contexto de la búsqueda
    def get_context_data(self, **kwargs):
        context = super(PerfilListar, self).get_context_data(**kwargs)
        q = self.request.GET.get('q')
        if q: #si existe el valor, lo agrego/actualizo en el contexto
            q = q.replace(" ","+")
            context['query'] = q
        return context    
    
class PerfilCrear(CreateView):
    model = Perfil
    fields = perfil_fields
	
    def get_success_url(self):
        return reverse('presupuestos:perfil_detalle', kwargs={
            'pk': self.object.pk,
        })

class PerfilDetalle(DetailView):
    model = Perfil
    fields = perfil_fields

class PerfilModificar(UpdateView):
    model = Perfil
    fields = perfil_fields
	
    def get_success_url(self):
        return reverse('presupuestos:perfil_detalle', kwargs={
            'pk': self.object.pk,
        })

class PerfilBorrar(DeleteView):
    model = Perfil
    success_url = reverse_lazy('presupuestos:perfil_listar')
    fields = perfil_fields