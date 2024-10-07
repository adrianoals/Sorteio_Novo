from django.contrib import admin
from .models import Apartamento, Vaga, Sorteio, DuplaSorteio

# Customizando a exibição do model Apartamento no admin
@admin.register(Apartamento)
class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero', 'is_pne', 'is_idoso')  # Exibe o ID, o número, e se é PNE ou Idoso
    list_display_links = ('id', 'numero')  # Links clicáveis para edição
    list_filter = ('is_pne', 'is_idoso')  # Filtros para facilitar a seleção

# Customizando a exibição do model Vaga no admin
@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero', 'tipo', 'especial', 'subsolo', 'is_livre_quando_nao_especial')  # Exibe informações importantes das vagas
    list_display_links = ('id', 'numero')  # Links clicáveis para edição
    list_filter = ('tipo', 'especial', 'subsolo', 'is_livre_quando_nao_especial')  # Filtros para facilitar a navegação no admin
    search_fields = ['numero']  # Permite busca por número da vaga

# Customizando a exibição do model Sorteio no admin
@admin.register(Sorteio)
class SorteioAdmin(admin.ModelAdmin):
    list_display = ('id', 'apartamento', 'vaga', 'data_sorteio')  # Exibe o ID, apartamento, vaga e data do sorteio
    list_display_links = ('id', 'apartamento', 'vaga')  # Links clicáveis para edição
    list_filter = ('apartamento', 'vaga')  # Filtros para facilitar a navegação
    date_hierarchy = 'data_sorteio'  # Permite filtragem por data do sorteio


# Customizando a exibição do model DuplaSorteio no admin
@admin.register(DuplaSorteio)
class DuplaSorteioAdmin(admin.ModelAdmin):
    list_display = ('id', 'apartamento_1', 'apartamento_2', 'vaga_1', 'vaga_2', 'data_sorteio')
    list_display_links = ('id', 'apartamento_1', 'vaga_1')
    list_filter = ('apartamento_1', 'apartamento_2', 'vaga_1', 'vaga_2')  # Filtros para duplas

    # Filtra as vagas disponíveis para mostrar apenas aquelas que ainda não foram sorteadas
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name in ['vaga_1', 'vaga_2']:
            # Filtrar para exibir apenas vagas que ainda não estão associadas a sorteios
            kwargs["queryset"] = Vaga.objects.filter(sorteio__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
