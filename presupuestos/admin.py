from django.contrib import admin
from .models import Cliente
from .models import Presupuesto, Numerador

admin.site.register(Cliente)
admin.site.register(Presupuesto)
admin.site.register(Numerador)

