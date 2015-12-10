 # -- coding: utf-8 --
from django.forms import ModelForm
from django import forms
from django.forms import modelformset_factory
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from .models import ParametroPrecio, Item, Subitem_parametro

#Armo el formset
class ParametroPrecio_Form(ModelForm): 
	#success_url = reverse_lazy('presupuestos:presupuesto_listar') #prueba
	class Meta:
		model = ParametroPrecio
		fields= ['seleccionado']		
								 
def promptparametros(request, iditem):
    ParametroPrecioFormSet = modelformset_factory(ParametroPrecio, form = ParametroPrecio_Form, extra= 0)
    if request.method == 'POST':
        formset = ParametroPrecioFormSet(request.POST, request.FILES)
        if formset.is_valid():
            item = Item.objects.get(id=iditem) #item al que agregar los parámetros
	        
            for form in formset: #recorro los formularios
                if form.cleaned_data['seleccionado']: #Si el parámetro está selecciondo lo agrego al ítem
                    unparametroprecio = form.instance #la instancia relacionada, como figura en la BD
                    subitem_parametro = Subitem_parametro.objects.create(
                        item = item,
                        itemparametro= unparametroprecio
                    )
                    subitem_parametro.save()
            #volver al ítem
            #return   
            return HttpResponseRedirect( reverse('presupuestos:itemsubitem_modificar', kwargs={'pk': iditem,})  )
			
    else:
        print "dddd"+ iditem
        formset = ParametroPrecioFormSet()
    return render_to_response("presupuestos/promptparametroprecio.html", {
        "ParametroPrecioFormSet": ParametroPrecioFormSet
    },)
	