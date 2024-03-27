from django.contrib import admin
from nova_colina.models import Apartamento, Sorteio, GrupoVaga


class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero_apartamento')
    list_display_links = ('id', 'numero_apartamento')

class GrupoVagaAdmin(admin.ModelAdmin):
    list_display = ('id', 'vagas')
    list_display_links = ('id', 'vagas')

# class VagaSimplesAdmin(admin.ModelAdmin):
#     list_display = ('id', 'vaga_simples')
#     list_display_links = ('id', 'vaga_simples')

# class VagaDuplaAdmin(admin.ModelAdmin):
#     list_display = ('id', 'vaga_dupla')
#     list_display_links = ('id', 'vaga_dupla')

class SorteioAdmin(admin.ModelAdmin):
    list_display = ('id', 'apartamento', 'vagas')
    list_display_links = ('id', 'apartamento', 'vagas')


admin.site.register(Apartamento, ApartamentoAdmin)
admin.site.register(GrupoVaga, GrupoVagaAdmin)
admin.site.register(Sorteio, SorteioAdmin)