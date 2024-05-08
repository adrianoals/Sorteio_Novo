from django.contrib import admin
from helbor.models import ApartamentoTorre1, VagaTorre1, SorteioTorre1


class ApartamentoTorre1Admin(admin.ModelAdmin):
    list_display = ('id', 'numero_apartamento')
    list_display_links = ('id', 'numero_apartamento')

class VagaTorre1Admin(admin.ModelAdmin):
    list_display = ('id', 'vaga')
    list_display_links = ('id', 'vaga')

class SorteioTorre1Admin(admin.ModelAdmin):
    list_display = ('id', 'apartamento', 'vaga')
    list_display_links = ('id', 'apartamento', 'vaga')


admin.site.register(ApartamentoTorre1, ApartamentoTorre1Admin)
admin.site.register(VagaTorre1, VagaTorre1Admin)
admin.site.register(SorteioTorre1, SorteioTorre1Admin)

