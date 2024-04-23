from django.contrib import admin
from assincon.models import ListaSindicos, Sorteio

class ListaSindicosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')	

class SorteioAdmin(admin.ModelAdmin):
    list_display = ('id', 'sindico', 'sorteado')
    list_display_links = ('id', 'sindico', 'sorteado')	

admin.site.register(ListaSindicos, ListaSindicosAdmin)
admin.site.register(Sorteio, SorteioAdmin)

