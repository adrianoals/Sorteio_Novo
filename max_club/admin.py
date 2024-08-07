from django.contrib import admin
from max_club.models import Apartamento, Vaga, Sorteio, ApartamentoBike, VagaBike, SorteioBike

class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero_apartamento')
    list_display_links = ('id', 'numero_apartamento')
    
class VagaAdmin(admin.ModelAdmin):
    list_display = ('id', 'vaga')
    list_display_links = ('id', 'vaga')

class SorteioAdmin(admin.ModelAdmin):
    list_display = ('id', 'apartamento', 'vaga')
    list_display_links = ('id', 'apartamento', 'vaga')


class ApartamentoBikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero_apartamento')
    list_display_links = ('id', 'numero_apartamento')
    
class VagaBikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'vaga')
    list_display_links = ('id', 'vaga')

class SorteioBikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'apartamento', 'vaga')
    list_display_links = ('id', 'apartamento', 'vaga')


admin.site.register(Apartamento, ApartamentoAdmin)
admin.site.register(Vaga, VagaAdmin)
admin.site.register(Sorteio, SorteioAdmin)
admin.site.register(ApartamentoBike, ApartamentoBikeAdmin)
admin.site.register(VagaBike, VagaBikeAdmin)
admin.site.register(SorteioBike, SorteioBikeAdmin)