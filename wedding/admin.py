from django.contrib import admin
from .models import *


@admin.register(WebPassword)
class WebPasswordAdmin(admin.ModelAdmin):
    list_display = ['password', 'is_required']


@admin.register(Confirmacion)
class ConfirmacionAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name',
                    'have_a_partner', 'bus_service', 'bus', 'song_name']
    list_filter = ['name', 'surname', 'have_a_partner', 'bus_service']
    search_fields = ['name', 'surname',
                     'partner_name', 'partner_surname', 'song_name']
    fieldsets = (
        ('Datos personales', {
            'fields': ('name', 'surname')
        }),
        ('Datos acompañante', {
            'fields': ('have_a_partner', 'partner_name', 'partner_surname')
        }),
        ('Autobús', {
            'fields': ('bus_service', 'bus', 'bus_place')
        }),
        ('Datos de interés', {
            'fields': ('food_restrictions', 'song_name')
        })
    )


@admin.register(SitiosInteres)
class SitiosInteresAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'web', 'site_type']
    list_filter = ['site_type']
    fieldsets = (
        ('Datos obligatorios', {
            'fields': ('site_type', 'name', 'web',)
        }),
        ('Datos opcionales', {
            'fields': ('phone', 'picture')
        })
    )


@admin.register(Itinerario)
class ItinerarioAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_time', 'end_time']
    list_filter = ['start_time', 'end_time', 'name']
    fieldsets = (
        ('Información evento', {
            'fields': ('name', 'description', 'start_time', 'end_time')
        }),
        ('Localización', {
            'fields': ('location_name', 'location_url', 'image')
        })
    )


@admin.register(InscripcionCampeonato)
class InscripcionCampeonatoAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname','licencia', 'handicap']


@admin.register(BestWishes)
class BestWishesAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'accepted']
    list_filter = ['name', 'surname', 'accepted']
    search_fields = ['name', 'surname']

    fieldsets = (
        ('Datos', {
            'fields': ('name', 'surname')
        }),
        ('Aceptado', {
            'fields': ('message', 'accepted')
        })
    )


@admin.register(CampeonatoGolf)
class CampeonatoGolfAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'lugar', 'location_url', 'fecha']


# MODIFICABLES WEB

@admin.register(LugarDeLaBoda)
class LugarDeLaBodaAdmin(admin.ModelAdmin):
    list_display = ['name', 'mensaje']


@admin.register(ItinerarioHeader)
class ItinerarioHeaderAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(NombresPareja)
class NombresParejaAdmin(admin.ModelAdmin):
    list_display = ['novia', 'novio']

    fieldsets = (
        ('Novia', {
            'fields': ('novia', 'descripcion_novia')
        }),
        ('Novio', {
            'fields': ('novio', 'descripcion_novio')
        })
    )


@admin.register(FechaDeBoda)
class FechaDeBodaAdmin(admin.ModelAdmin):
    list_display = ['fecha']


@admin.register(Autobus)
class AutobusAdmin(admin.ModelAdmin):
    list_display = ['name']
