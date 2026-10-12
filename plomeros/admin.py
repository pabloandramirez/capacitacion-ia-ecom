from django.contrib import admin

from .models import Documento, Plomero


@admin.register(Plomero)
class PlomeroAdmin(admin.ModelAdmin):
    list_display = ("sucursal", "cuil", "nombre", "desde", "hasta")
    list_filter = ("sucursal",)
    search_fields = ("cuil", "nombre")
    ordering = ("sucursal", "cuil")


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre")
    search_fields = ("nombre",)
