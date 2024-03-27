from django.contrib import admin
from sorteio_novo.models import ListaDePresenca

class ListaDePresencaAdmin(admin.ModelAdmin):
    list_display = ('id', 'apartamento', 'bloco', 'presenca', 'vaga')
    list_display_links = ('id', 'apartamento', 'bloco',)
    list_editable = ('presenca', 'vaga')


admin.site.register(ListaDePresenca, ListaDePresencaAdmin)


