# Importar os modelos
from nova_colina.models import Apartamento, GrupoVaga

# Função para popular Apartamentos
def popular_apartamentos():
    for numero in Apartamento.APARTAMENTO_CHOICES:
        Apartamento.objects.get_or_create(numero_apartamento=numero[0])

# Função para popular Vagas Simples
def popular_vagas():
    for vaga in GrupoVaga.VAGAS_CHOICES:
        GrupoVaga.objects.get_or_create(vagas=vaga[0])


# Executar as funções
if __name__ == "__main__":
    popular_apartamentos()
    popular_vagas()
