 # -- coding: utf-8 --
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q #para OR en consultas

from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
matriztecnicalct_fields = ('matriz','parametro','tecnica','lct','unidad')

from .models import MatrizTecnicaLct


class MatrizTecnicaLctListar(ListView):
    model = MatrizTecnicaLct
    paginate_by = 10
"""    
    #búsqueda
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is None:
            return MatrizTecnicaLct.objects.all()
        else:
            return MatrizTecnicaLct.objects.filter( Q(matriz__nombre_matriz__icontains=query) | 
                                          Q(parametro__nombre_par__icontains=query) | 
                                          Q(tecnica__nombre_tec__icontains=query)  )
                                  
    #almacenar contexto de la búsqueda
    def get_context_data(self, **kwargs):
        context = super(MatrizTecnicaLctListar, self).get_context_data(**kwargs)
        q = self.request.GET.get('q')
        if q: #si existe el valor, lo agrego/actualizo en el contexto
            q = q.replace(" ","+")
            context['query'] = q
        return context    
 """   
class MatrizTecnicaLctCrear(CreateView):
    model = MatrizTecnicaLct
    fields = matriztecnicalct_fields
	
    def get_success_url(self):
        return reverse('presupuestos:matriztecnicalct_detalle', kwargs={
            'pk': self.object.pk,
        })

class MatrizTecnicaLctDetalle(DetailView):
    model = MatrizTecnicaLct
    fields = matriztecnicalct_fields

class MatrizTecnicaLctModificar(UpdateView):
    model = MatrizTecnicaLct
    fields = matriztecnicalct_fields
	
    def get_success_url(self):
        return reverse('presupuestos:matriztecnicalct_detalle', kwargs={
            'pk': self.object.pk,
        })

class MatrizTecnicaLctBorrar(DeleteView):
    model = MatrizTecnicaLct
    success_url = reverse_lazy('presupuestos:matriztecnicalct_listar')
    fields = matriztecnicalct_fields