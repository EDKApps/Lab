 # -- coding: utf-8 --
from django.conf.urls import patterns, include, url
from .viewcliente import labinicio, ClienteCrear, ClienteBorrar, ClienteDetalle, ClienteListar, ClienteModificar
from .viewpresupuesto import PresupuestoCrear, PresupuestoBorrar, PresupuestoDetalle, PresupuestoListar, PresupuestoModificar
from .viewmuestra import MuestraListar
from .viewordendetrabajo import OrdenDeTrabajoListar
urlpatterns = patterns('',
             
    #Base
    url(r'^$', labinicio, name='lab_inicio'),                       
    #Clientes
    url(r'^clientes/$', ClienteListar.as_view(), name='cliente_listar'),
    url(r'^clientes/crear/$', ClienteCrear.as_view(), name='cliente_crear'),
    url(r'^clientes/(?P<pk>\d+)/$', ClienteDetalle.as_view(), name='cliente_detalle'),
    url(r'^clientes/(?P<pk>\d+)/modificar/$', ClienteModificar.as_view(), name='cliente_modificar'),
    url(r'^clientes/(?P<pk>\d+)/borrar/$', ClienteBorrar.as_view(), name='cliente_borrar'),

    #Presupuestos
	url(r'^presupuestos/$', PresupuestoListar.as_view(), name='presupuesto_listar'),
    url(r'^presupuestos/crear/$', PresupuestoCrear.as_view(), name='presupuesto_crear'),
    url(r'^presupuestos/(?P<pk>\d+)/$', PresupuestoDetalle.as_view(), name='presupuesto_detalle'),
    url(r'^presupuestos/(?P<pk>\d+)/modificar/$', PresupuestoModificar.as_view(), name='presupuesto_modificar'),
    url(r'^presupuestos/(?P<pk>\d+)/borrar/$', PresupuestoBorrar.as_view(), name='presupuesto_borrar'),
					   
    #Ordenes de trabajo
    url(r'^ordenesdetrabajo/$', OrdenDeTrabajoListar, name='ordendetrabajo_listar'), #pasar a .as_view()
                       
    #Muestras
    url(r'^muestras/$', MuestraListar, name='muestra_listar'), #pasar a .as_view() 
    
)