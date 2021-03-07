from django.contrib import admin
from .models import Page

#configuracion extra
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at') #para que aparezcan la fc¿echa
    search_fields = ('title', 'content') #buscador
    list_filter = ('visible', 'created_at')
    list_display = ('title', 'visible', 'created_at') #para decir que columnas quiero visble
    ordering = ('-created_at',) #con esto puedo ordenar por atributos

# Register your models here.
admin.site.register(Page, PageAdmin) 

#configuración del panel
title = "Panel de Gestión" #esto debo modificarlo en settings
subtitle = "Proyecto DJango"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle