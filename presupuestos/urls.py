 # -- coding: utf-8 --
from django.conf.urls import patterns, include, url
from .viewcliente import labinicio, ClienteCrear, ClienteBorrar, ClienteDetalle, ClienteListar, ClienteModificar
from .viewpresupuesto import PresupuestoCrear, PresupuestoBorrar, PresupuestoDetalle, PresupuestoListar, PresupuestoModificar, PresupuestoDetalleFull
from .viewmuestra import MuestraListar
from .viewordendetrabajo import OrdenDeTrabajoListar
from .viewmatriz import MatrizCrear, MatrizBorrar, MatrizDetalle, MatrizListar, MatrizModificar
from .viewfamilia import FamiliaCrear, FamiliaBorrar, FamiliaDetalle, FamiliaConfirmaAlta, FamiliaListar, FamiliaModificar
from .viewparametro import ParametroCrear, ParametroBorrar, ParametroDetalle, ParametroListar, ParametroModificar
from .viewtecnica import TecnicaCrear, TecnicaBorrar, TecnicaDetalle, TecnicaListar, TecnicaModificar
from .viewunidades import UnidadesCrear, UnidadesBorrar, UnidadesDetalle, UnidadesListar, UnidadesModificar
from .viewmatriztecnicalct import MatrizTecnicaLctCrear, MatrizTecnicaLctBorrar, MatrizTecnicaLctDetalle,MatrizTecnicaLctConfirmaAlta, MatrizTecnicaLctListar, MatrizTecnicaLctModificar
from .viewparametroprecio import ParametroPrecioCrear, ParametroPrecioBorrar, ParametroPrecioDetalle, ParametroPrecioListar, ParametroPrecioModificar
from .viewperfilprecio import PerfilPrecioCrear, PerfilPrecioBorrar, PerfilPrecioDetalle, PerfilPrecioConfirmaAlta, PerfilPrecioListar, PerfilPrecioModificar
from .viewitem import ItemCrear, ItemBorrar, ItemDetalle, ItemListar, ItemModificar
from .viewpresupuestoitem import PresupuestoItemModificar, PresupuestoItemDetalle
from .viewpresupuestocampania import PresupuestoCampaniaModificar
from .viewitemsubitem import ItemSubitemModificar
from .viewpromptparametros import promptparametros
from .viewpromptperfiles import promptperfiles

urlpatterns = patterns('',
             
    #Base
    url(r'^$', PresupuestoListar.as_view(), name='lab_inicio'), #por defecto va al listar presupuestos                       
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
	url(r'^presupuestosfull/(?P<pk>\d+)/$', PresupuestoDetalleFull.as_view(), name='presupuesto_detalle_full'),
					   
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
	url(r'^familia/(?P<pk>\d+)/confirmaalta$', FamiliaConfirmaAlta.as_view(), name='familia_confirma_alta'),
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


	#MatrizTecnicaLct o Límite de cuantificación
    url(r'^matriztecnicalct/$', MatrizTecnicaLctListar.as_view(), name='matriztecnicalct_listar'),
    url(r'^matriztecnicalct/crear/$', MatrizTecnicaLctCrear.as_view(), name='matriztecnicalct_crear'),
    url(r'^matriztecnicalct/(?P<pk>\d+)/$', MatrizTecnicaLctDetalle.as_view(), name='matriztecnicalct_detalle'),
    url(r'^matriztecnicalct/(?P<pk>\d+)/confirmaalta$', MatrizTecnicaLctConfirmaAlta.as_view(), name='matriztecnicalct_confirma_alta'),                       
    url(r'^matriztecnicalct/(?P<pk>\d+)/modificar/$', MatrizTecnicaLctModificar.as_view(), name='matriztecnicalct_modificar'),
    url(r'^matriztecnicalct/(?P<pk>\d+)/borrar/$', MatrizTecnicaLctBorrar.as_view(), name='matriztecnicalct_borrar'),  
			
	#ParametroPrecio
    url(r'^parametroprecio/$', ParametroPrecioListar.as_view(), name='parametroprecio_listar'),
    url(r'^parametroprecio/crear/$', ParametroPrecioCrear.as_view(), name='parametroprecio_crear'),
    url(r'^parametroprecio/(?P<pk>\d+)/$', ParametroPrecioDetalle.as_view(), name='parametroprecio_detalle'),
    url(r'^parametroprecio/(?P<pk>\d+)/modificar/$', ParametroPrecioModificar.as_view(), name='parametroprecio_modificar'),
    url(r'^parametroprecio/(?P<pk>\d+)/borrar/$', ParametroPrecioBorrar.as_view(), name='parametroprecio_borrar'),
                       
    #PerfilPrecio
    url(r'^perfilprecio/$', PerfilPrecioListar.as_view(), name='perfilprecio_listar'),
    url(r'^perfilprecio/crear/$', PerfilPrecioCrear.as_view(), name='perfilprecio_crear'),
    url(r'^perfilprecio/(?P<pk>\d+)/$', PerfilPrecioDetalle.as_view(), name='perfilprecio_detalle'),
	url(r'^perfilprecio/(?P<pk>\d+)/confirmaalta$', PerfilPrecioConfirmaAlta.as_view(), name='perfilprecio_confirma_alta'),                         
    url(r'^perfilprecio/(?P<pk>\d+)/modificar/$', PerfilPrecioModificar.as_view(), name='perfilprecio_modificar'),
    url(r'^perfilprecio/(?P<pk>\d+)/borrar/$', PerfilPrecioBorrar.as_view(), name='perfilprecio_borrar'),    
                       
	#Item
    url(r'^item/$', ItemListar.as_view(), name='item_listar'),
    url(r'^item/crear/$', ItemCrear.as_view(), name='item_crear'),
    url(r'^item/(?P<pk>\d+)/$', ItemDetalle.as_view(), name='item_detalle'),
    url(r'^item/(?P<pk>\d+)/modificar/$', ItemModificar.as_view(), name='item_modificar'),
    url(r'^item/(?P<pk>\d+)/borrar/$', ItemBorrar.as_view(), name='item_borrar'),
	
    #relacion presupuesto-item
    url(r'^presupuestoitem/(?P<pk>\d+)/$', PresupuestoItemDetalle.as_view(), name='presupuestoitem_detalle'),
    url(r'^presupuestoitem/(?P<pk>\d+)/modificar/$', PresupuestoItemModificar.as_view(), name='presupuestoitem_modificar'),

    #relacion presupuesto-campania
    #url(r'^presupuestoitem/(?P<pk>\d+)/$', PresupuestoItemDetalle.as_view(), name='presupuestoitem_detalle'),
    url(r'^presupuestocampania/(?P<pk>\d+)/modificar/$', PresupuestoCampaniaModificar.as_view(), name='presupuestocampania_modificar'),
    
    #relacion item-subitem (parámetro y perfil)
    url(r'^itemsubitem/(?P<pk>\d+)/modificar/$', ItemSubitemModificar.as_view(), name='itemsubitem_modificar'),
                       
    #multiselección de parámetros
    #http://localhost:8000/presupuestos/promptparametros/1/
    url(r'^promptparametros/(?P<iditem>\d+)/$', promptparametros, name='promptparametros'),
                       
    #multiseleccion de perfiles
    url(r'^promptperfiles/(?P<iditem>\d+)/$', promptperfiles, name='promptperfiles'),
    
)
