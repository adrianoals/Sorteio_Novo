from django.contrib import admin
from helbor.models import ApartamentoTorre1, VagaTorre1, SorteioTorre1, ApartamentoTorre2, VagaTorre2, SorteioTorre2


class ApartamentoTorre1Admin(admin.ModelAdmin):
    list_display = ('id', 'numero_apartamento')
    list_display_links = ('id', 'numero_apartamento')

class VagaTorre1Admin(admin.ModelAdmin):
    list_display = ('id', 'vaga')
    list_display_links = ('id', 'vaga')

class SorteioTorre1Admin(admin.ModelAdmin):
    list_display = ('id', 'apartamento', 'vaga')
    list_display_links = ('id', 'apartamento', 'vaga')

class ApartamentoTorre2Admin(admin.ModelAdmin):
    list_display = ('id', 'numero_apartamento')
    list_display_links = ('id', 'numero_apartamento')

class VagaTorre2Admin(admin.ModelAdmin):
    list_display = ('id', 'vaga')
    list_display_links = ('id', 'vaga')

class SorteioTorre2Admin(admin.ModelAdmin):
    list_display = ('id', 'apartamento', 'vaga')
    list_display_links = ('id', 'apartamento', 'vaga')


admin.site.register(ApartamentoTorre1, ApartamentoTorre1Admin)
admin.site.register(VagaTorre1, VagaTorre1Admin)
admin.site.register(SorteioTorre1, SorteioTorre1Admin)
admin.site.register(ApartamentoTorre2, ApartamentoTorre2Admin)
admin.site.register(VagaTorre2, VagaTorre2Admin)
admin.site.register(SorteioTorre2, SorteioTorre2Admin)

