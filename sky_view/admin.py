from django.contrib import admin
from .models import Apartamento, Vaga, Sorteio

# Registro dos modelos no Django Admin com o decorator @admin.register

@admin.register(Apartamento)
class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'andar', 'direito_vaga_dupla', 'direito_duas_vagas_livres')
    list_filter = ('andar', 'direito_vaga_dupla', 'direito_duas_vagas_livres')
    search_fields = ('numero',)

@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'subsolo', 'tipo_vaga', 'dupla_com')
    list_filter = ('subsolo', 'tipo_vaga')
    search_fields = ('numero',)

@admin.register(Sorteio)
class SorteioAdmin(admin.ModelAdmin):
    list_display = ('apartamento', 'vaga', 'data_sorteio')
    list_filter = ('data_sorteio',)
    search_fields = ('apartamento__numero', 'vaga__numero')

