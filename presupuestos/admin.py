from django.contrib import admin
from .models import Cliente
from .models import Presupuesto
from .models import Tipo
from .models import Estado

admin.site.register(Cliente)
admin.site.register(Presupuesto)
admin.site.register(Estado)
admin.site.register(Tipo)
