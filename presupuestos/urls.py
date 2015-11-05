 # -- coding: utf-8 --
from django.conf.urls import patterns, include, url
from .viewcliente import labinicio, ClienteCrear, ClienteBorrar, ClienteDetalle, ClienteListar, ClienteModificar
from .viewpresupuesto import PresupuestoCrear, PresupuestoBorrar, PresupuestoDetalle, PresupuestoListar, PresupuestoModificar
from .viewmuestra import MuestraListar
from .viewordendetrabajo import OrdenDeTrabajoListar
from .viewmatriz import MatrizCrear, MatrizBorrar, MatrizDetalle, MatrizListar, MatrizModificar
from .viewfamilia import FamiliaCrear, FamiliaBorrar, FamiliaDetalle, FamiliaListar, FamiliaModificar
from .viewparametro import ParametroCrear, ParametroBorrar, ParametroDetalle, ParametroListar, ParametroModificar
from .viewtecnica import TecnicaCrear, TecnicaBorrar, TecnicaDetalle, TecnicaListar, TecnicaModificar
from .viewunidades import UnidadesCrear, UnidadesBorrar, UnidadesDetalle, UnidadesListar, UnidadesModificar
from .viewmatriztecnicalct import MatrizTecnicaLctCrear, MatrizTecnicaLctBorrar, MatrizTecnicaLctDetalle, MatrizTecnicaLctListar, MatrizTecnicaLctModificar
from .viewparametroprecio import ParametroPrecioCrear, ParametroPrecioBorrar, ParametroPrecioDetalle, ParametroPrecioListar, ParametroPrecioModificar
from .viewgrupoparametro import GrupoParametroCrear, GrupoParametroBorrar, GrupoParametroDetalle, GrupoParametroListar, GrupoParametroModificar
from .viewgrupoparametroprecio import GrupoParametroPrecioCrear, GrupoParametroPrecioBorrar, GrupoParametroPrecioDetalle, GrupoParametroPrecioListar, GrupoParametroPrecioModificar
#from .viewgrupoparametroprecio_parametro import GrupoParametroPrecio_ParametroCrear, GrupoParametroPrecio_ParametroBorrar, GrupoParametroPrecio_ParametroDetalle, GrupoParametroPrecio_ParametroListar, GrupoParametroPrecio_ParametroModificar

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
					 
	#Matriz
    url(r'^matriz/$', MatrizListar.as_view(), name='matriz_listar'),
    url(r'^matriz/crear/$', MatrizCrear.as_view(), name='matriz_crear'),
    url(r'^matriz/(?P<pk>\d+)/$', MatrizDetalle.as_view(), name='matriz_detalle'),
    url(r'^matriz/(?P<pk>\d+)/modificar/$', MatrizModificar.as_view(), name='matriz_modificar'),
    url(r'^matriz/(?P<pk>\d+)/borrar/$', MatrizBorrar.as_view(), name='matriz_borrar'),
						   
	#Familia
    url(r'^familia/$', FamiliaListar.as_view(), name='familia_listar'),
    url(r'^familia/crear/$', FamiliaCrear.as_view(), name='familia_crear'),
    url(r'^familia/(?P<pk>\d+)/$', FamiliaDetalle.as_view(), name='familia_detalle'),
    url(r'^familia/(?P<pk>\d+)/modificar/$', FamiliaModificar.as_view(), name='familia_modificar'),
    url(r'^familia/(?P<pk>\d+)/borrar/$', FamiliaBorrar.as_view(), name='familia_borrar'),					   
					   
	#Parametro
    url(r'^parametro/$', ParametroListar.as_view(), name='parametro_listar'),
    url(r'^parametro/crear/$', ParametroCrear.as_view(), name='parametro_crear'),
    url(r'^parametro/(?P<pk>\d+)/$', ParametroDetalle.as_view(), name='parametro_detalle'),
    url(r'^parametro/(?P<pk>\d+)/modificar/$', ParametroModificar.as_view(), name='parametro_modificar'),
    url(r'^parametro/(?P<pk>\d+)/borrar/$', ParametroBorrar.as_view(), name='parametro_borrar'),					   

	#Tecnica
    url(r'^tecnica/$', TecnicaListar.as_view(), name='tecnica_listar'),
    url(r'^tecnica/crear/$', TecnicaCrear.as_view(), name='tecnica_crear'),
    url(r'^tecnica/(?P<pk>\d+)/$', TecnicaDetalle.as_view(), name='tecnica_detalle'),
    url(r'^tecnica/(?P<pk>\d+)/modificar/$', TecnicaModificar.as_view(), name='tecnica_modificar'),
    url(r'^tecnica/(?P<pk>\d+)/borrar/$', TecnicaBorrar.as_view(), name='tecnica_borrar'),	

    #Unidades
    url(r'^unidades/$', UnidadesListar.as_view(), name='unidades_listar'),
    url(r'^unidades/crear/$', UnidadesCrear.as_view(), name='unidades_crear'),
    url(r'^unidades/(?P<pk>\d+)/$', UnidadesDetalle.as_view(), name='unidades_detalle'),
    url(r'^unidades/(?P<pk>\d+)/modificar/$', UnidadesModificar.as_view(), name='unidades_modificar'),
    url(r'^unidades/(?P<pk>\d+)/borrar/$', UnidadesBorrar.as_view(), name='unidades_borrar'),


	#MatrizTecnicaLct
    url(r'^matriztecnicalct/$', MatrizTecnicaLctListar.as_view(), name='matriztecnicalct_listar'),
    url(r'^matriztecnicalct/crear/$', MatrizTecnicaLctCrear.as_view(), name='matriztecnicalct_crear'),
    url(r'^matriztecnicalct/(?P<pk>\d+)/$', MatrizTecnicaLctDetalle.as_view(), name='matriztecnicalct_detalle'),
    url(r'^matriztecnicalct/(?P<pk>\d+)/modificar/$', MatrizTecnicaLctModificar.as_view(), name='matriztecnicalct_modificar'),
    url(r'^matriztecnicalct/(?P<pk>\d+)/borrar/$', MatrizTecnicaLctBorrar.as_view(), name='matriztecnicalct_borrar'),  
			
	#ParametroPrecio
    url(r'^parametroprecio/$', ParametroPrecioListar.as_view(), name='parametroprecio_listar'),
    url(r'^parametroprecio/crear/$', ParametroPrecioCrear.as_view(), name='parametroprecio_crear'),
    url(r'^parametroprecio/(?P<pk>\d+)/$', ParametroPrecioDetalle.as_view(), name='parametroprecio_detalle'),
    url(r'^parametroprecio/(?P<pk>\d+)/modificar/$', ParametroPrecioModificar.as_view(), name='parametroprecio_modificar'),
    url(r'^parametroprecio/(?P<pk>\d+)/borrar/$', ParametroPrecioBorrar.as_view(), name='parametroprecio_borrar'),
					   
	#Grupo_Parametro
    url(r'^grupoparametro/$', GrupoParametroListar.as_view(), name='grupoparametro_listar'),
    url(r'^grupoparametro/crear/$', GrupoParametroCrear.as_view(), name='grupoparametro_crear'),
    url(r'^grupoparametro/(?P<pk>\d+)/$', GrupoParametroDetalle.as_view(), name='grupoparametro_detalle'),
    url(r'^grupoparametro/(?P<pk>\d+)/modificar/$', GrupoParametroModificar.as_view(), name='grupoparametro_modificar'),
    url(r'^grupoparametro/(?P<pk>\d+)/borrar/$', GrupoParametroBorrar.as_view(), name='grupoparametro_borrar'), 
                       
    #GrupoParametroPrecio
    url(r'^grupoparametroprecio/$', GrupoParametroPrecioListar.as_view(), name='grupoparametroprecio_listar'),
    url(r'^grupoparametroprecio/crear/$', GrupoParametroPrecioCrear.as_view(), name='grupoparametroprecio_crear'),
    url(r'^grupoparametroprecio/(?P<pk>\d+)/$', GrupoParametroPrecioDetalle.as_view(), name='grupoparametroprecio_detalle'),
    url(r'^grupoparametroprecio/(?P<pk>\d+)/modificar/$', GrupoParametroPrecioModificar.as_view(), name='grupoparametroprecio_modificar'),
    url(r'^grupoparametroprecio/(?P<pk>\d+)/borrar/$', GrupoParametroPrecioBorrar.as_view(), name='grupoparametroprecio_borrar'),    
                       
)


"""
       
    

   
                       

    #GrupoParametroPrecio_Parametro
    url(r'^grupoparametroprecio_parametro/$', GrupoParametroPrecioListar.as_view(), name='grupoparametroprecio_parametro_listar'),
    url(r'^grupoparametroprecio_parametro/crear/$', GrupoParametroPrecioCrear.as_view(), name='grupoparametroprecio_parametro_crear'),
    url(r'^grupoparametroprecio_parametro/(?P<pk>\d+)/$', GrupoParametroPrecioDetalle.as_view(), name='grupoparametroprecio_parametro_detalle'),
    url(r'^grupoparametroprecio_parametro/(?P<pk>\d+)/modificar/$', GrupoParametroPrecioModificar.as_view(), name='grupoparametroprecio_parametro_modificar'),
    url(r'^grupoparametroprecio_parametro/(?P<pk>\d+)/borrar/$', GrupoParametroPrecioBorrar.as_view(), name='grupoparametroprecio_parametro_borrar'),    

"""
