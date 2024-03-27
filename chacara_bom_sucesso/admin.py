from django.contrib import admin
from chacara_bom_sucesso.models import Apartamento, Bloco, Vaga, Sorteio


class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero_apartamento', 'bloco')
    list_display_links = ('id', 'numero_apartamento', 'bloco')

class BlocoAdmin(admin.ModelAdmin):
    list_display = ('id', 'bloco')
    list_display_links = ('id', 'bloco')

class VagaAdmin(admin.ModelAdmin):
    list_display = ('id', 'vaga')
    list_display_links = ('id', 'vaga')

class SorteioAdmin(admin.ModelAdmin):
    list_display = ('id', 'apartamento', 'vaga')
    list_display_links = ('id', 'apartamento', 'vaga')


admin.site.register(Apartamento, ApartamentoAdmin)
admin.site.register(Bloco, BlocoAdmin)
admin.site.register(Vaga, VagaAdmin)
admin.site.register(Sorteio, SorteioAdmin)




