from django.conf.urls import patterns, include, url
from .views import ClienteCrear, ClienteBorrar, ClienteDetalle, ClienteListar, ClienteModificar

urlpatterns = patterns('',
    url(r'^clientes/$', ClienteListar.as_view(), name='cliente_listar'),
    url(r'^clientes/crear/$', ClienteCrear.as_view(), name='cliente_crear'),
    url(r'^clientes/(?P<pk>\d+)/$', ClienteDetalle.as_view(), name='cliente_detalle'),
    url(r'^clientes/(?P<pk>\d+)/modificar/$', ClienteModificar.as_view(), name='cliente_modificar'),
    url(r'^clientes/(?P<pk>\d+)/borrar/$', ClienteBorrar.as_view(), name='cliente_borrar'),
)