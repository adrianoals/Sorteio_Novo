from django.contrib import admin
from lyon.models import Apartamento, Sorteio, Vaga, ApartamentoMoto, SorteioMoto, VagaMoto

class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero_apartamento', 'pcd')
    list_display_links = ('id', 'numero_apartamento', 'pcd')

class VagaAdmin(admin.ModelAdmin):
    list_display = ('id', 'vaga', 'coberta', 'pcd')
    list_display_links = ('id', 'vaga', 'coberta', 'pcd')

class SorteioAdmin(admin.ModelAdmin):
    list_display = ('id', 'apartamento', 'vaga')
    list_display_links = ('id', 'apartamento', 'vaga')

class ApartamentoMotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero_apartamento')
    list_display_links = ('id', 'numero_apartamento')

class VagaMotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'vaga')
    list_display_links = ('id', 'vaga')

class SorteioMotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'apartamento', 'vaga')
    list_display_links = ('id', 'apartamento', 'vaga')


admin.site.register(Apartamento, ApartamentoAdmin)
admin.site.register(Vaga, VagaAdmin)
admin.site.register(Sorteio, SorteioAdmin)

admin.site.register(ApartamentoMoto, ApartamentoMotoAdmin)
admin.site.register(VagaMoto, VagaMotoAdmin)
admin.site.register(SorteioMoto, SorteioMotoAdmin)
