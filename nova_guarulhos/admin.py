from django.contrib import admin
from nova_guarulhos.models import Apartamento, Sorteio, Vaga


class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'bloco', 'numero_apartamento', 'pcd', 'idoso', 'adimplentes', 'presenca')
    list_display_links = ('id', 'bloco', 'numero_apartamento')
    
class VagaAdmin(admin.ModelAdmin):
    list_display = ('id', 'vaga')
    list_display_links = ('id', 'vaga')

class SorteioAdmin(admin.ModelAdmin):
    list_display = ('id', 'apartamento', 'vaga')
    list_display_links = ('id', 'apartamento', 'vaga')


admin.site.register(Apartamento, ApartamentoAdmin)
admin.site.register(Vaga, VagaAdmin)
admin.site.register(Sorteio, SorteioAdmin)

