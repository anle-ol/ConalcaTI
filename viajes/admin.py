from django.contrib import admin
from .models import Vehiculo


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'placa', 'tipo_vehiculo', 'cliente', 'fecha_inicio', 'numero_entregas', 'facturacion', 'validado']
    list_filter = ['tipo_vehiculo', 'validado', 'fecha_inicio']
    search_fields = ['placa', 'cliente', 'codigo']
    date_hierarchy = 'fecha_inicio'
