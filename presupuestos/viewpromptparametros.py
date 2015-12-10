 # -- coding: utf-8 --
from django.forms import ModelForm
from django import forms
from django.forms import modelformset_factory
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from .models import ParametroPrecio

#Armo el formset
class ParametroPrecio_Form(ModelForm): 
	success_url = reverse_lazy('presupuestos:presupuesto_listar') #prueba
	class Meta:
		model = ParametroPrecio
		fields= ['seleccionado','matriz']
		
								 
def promptparametros(request, iditem):
	
    #AuthorFormSet = modelformset_factory(Author, fields=('name', 'title'))
    ParametroPrecioFormSet = modelformset_factory(ParametroPrecio, form = ParametroPrecio_Form, extra= 0)
    if request.method == 'POST':
        formset = ParametroPrecioFormSet(request.POST, request.FILES)
        #for form in formset:
			#print form
            #print 'aaa' + form.id + 'bbb'+ form.seleccionado
            #print form.instance.id 	
            #print form.instance.seleccionado
			#print form.field[seleccionado]
            #print form.cleaned_data['id']
        if formset.is_valid():
            print "eeee"+ iditem	
            for form in formset:
                print form.cleaned_data['id']
                print form.cleaned_data['matriz']
                print form.cleaned_data['seleccionado']
            #formset.save()
            # do something.
        else:
            print "fff"+ iditem
			
    else:
        print "dddd"+ iditem
        formset = ParametroPrecioFormSet()
    return render_to_response("presupuestos/promptparametroprecio.html", {
        "ParametroPrecioFormSet": ParametroPrecioFormSet
    },)
	