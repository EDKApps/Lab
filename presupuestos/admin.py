from django.contrib import admin
from .models import Cliente
from .models import Presupuesto, Numerador
from .models import Tipo
from .models import Estado
from .models import Matriz
from .models import Familia
from .models import Parametro
from .models import Tecnica
from .models import Unidades
from .models import MatrizTecnicaLct
from .models import ParametroPrecio 
from .models import PerfilPrecio
from .models import PerfilPrecio_Parametro
from .models import Campania
from .models import Item

admin.site.register(Cliente)
admin.site.register(Presupuesto)
admin.site.register(Numerador)
admin.site.register(Estado)
admin.site.register(Tipo)
admin.site.register(Matriz)
admin.site.register(Familia)
admin.site.register(Parametro)
admin.site.register(Tecnica)
admin.site.register(Unidades)
admin.site.register(MatrizTecnicaLct)
admin.site.register(ParametroPrecio)
admin.site.register(PerfilPrecio)
admin.site.register(PerfilPrecio_Parametro)
admin.site.register(Campania)
admin.site.register(Item)

