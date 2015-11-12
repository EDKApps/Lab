 # -- coding: utf-8 --
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q #para OR en consultas

from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
grupoparametroprecio_fields = ('matriz','grupo_parametro','tecnica','precio_del_grupo','fecha_de_precio')

from .formgrupoparametroprecio import GrupoParametroPrecioForm, GrupoParametroPrecio_ParametroFormSet
from .models import GrupoParametroPrecio, GrupoParametroPrecio_Parametro

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
    #fields = grupoparametroprecio_fields
    form_class= GrupoParametroPrecioForm
    def get_success_url(self):
        return reverse('presupuestos:grupoparametroprecio_detalle', kwargs={
            'pk': self.object.pk,
        })
    def get(self, request, *args, **kwargs):
        """
        Maneja GET requests e instancia una versión limpia del form y su formset
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        parametro_form = GrupoParametroPrecio_ParametroFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  parametro_form=parametro_form,
                                  ))
    def post(self, request, *args, **kwargs):        
        """
        Maneja POST request instanciando un form con sus formsets,
        con las variables POST pasadas y chequea validez
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        parametro_form = GrupoParametroPrecio_ParametroFormSet(self.request.POST)
        if (form.is_valid() and parametro_form.is_valid()):
            return self.form_valid(form, parametro_form)
        else:
            return self.form_invalid(form, parametro_form)
    
    def form_valid(self, form, parametro_form):
        """
        Llamada si todos los forms son válidos. Crea cabecera junto con
        los parámetros asociados y redirecciona a una página de éxito
        """
        self.object = form.save()
        parametro_form.instance = self.object
        parametro_form.save()
        return HttpResponseRedirect(self.get_success_url())
            
    def form_invalid(self, form, parametro_form):
        """
        Llamada si un formulario es inválido. Re-renders context data con el formulario
        cargado y los errores
        """
        return self.render_to_response(
                self.get_context_data(form=form,
                                      parametro_form = parametro_form))
        
        
        
        
class GrupoParametroPrecioDetalle(DetailView):
    model = GrupoParametroPrecio
    fields = grupoparametroprecio_fields

class GrupoParametroPrecioModificar(UpdateView):
    model = GrupoParametroPrecio
    form_class= GrupoParametroPrecioForm
    
    def get(self, request, *args, **kwargs):
        """
        Maneja GET requests e instancia una versión limpia del form y su formset
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        #obtener parametros
        #parametros = GrupoParametroPrecio_Parametro.objects.filter(grupoparametroprecio=self.object).values() #.order_by('name').values()
        
        #render form
        parametro_form = GrupoParametroPrecio_ParametroFormSet(instance = self.object) #antes (initial = parametros)
        
        return self.render_to_response(
            self.get_context_data(form=form,
                                  parametro_form=parametro_form,
                                  ))
    
    def post(self, request, *args, **kwargs):        
        """
        Maneja POST request instanciando un form con sus formsets,
        con las variables POST pasadas y chequea validez
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        #parametro_form = GrupoParametroPrecio_ParametroFormSet(self.request.POST)
        
        parametro_form = GrupoParametroPrecio_ParametroFormSet(instance = GrupoParametroPrecio())
        parametro_form = GrupoParametroPrecio_ParametroFormSet(request.POST,request.FILES,instance= self.object )
        
        if (form.is_valid() and parametro_form.is_valid()):

            
            self.object = form.save(commit=False)
            
            self.object.save()
            parametro_form.save()
            #Eliminar lo indicado del subnivel
            #GrupoParametroPrecio_Parametro.objects.filter(grupoparametroprecio=self.object, eliminado = True).delete()
            return HttpResponseRedirect(self.get_success_url())
            
            
        else:
            return self.form_invalid(form, parametro_form)
    
    def get_success_url(self):
        return reverse('presupuestos:grupoparametroprecio_detalle', kwargs={
            'pk': self.object.pk,
        })
            
    def form_invalid(self, form, parametro_form):
        """
        Llamada si un formulario es inválido. Re-renders context data con el formulario
        cargado y los errores
        """
        return self.render_to_response(
                self.get_context_data(form=form,
                                      parametro_form = parametro_form))

class GrupoParametroPrecioBorrar(DeleteView):
    model = GrupoParametroPrecio
    success_url = reverse_lazy('presupuestos:grupoparametroprecio_listar')
    fields = grupoparametroprecio_fields