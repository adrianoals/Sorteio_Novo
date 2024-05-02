# Criando uma lista de números de apartamento
apartamentos = []
for andar in range(1, 20):  # Para andares de 1 a 15
    for unidade in range(1, 5):  # Para unidades de 1 a 4 em cada andar
        numero_apartamento = str(andar * 10 + unidade)  # Calcula o número do apartamento
        apartamentos.append(numero_apartamento)

# Exibindo a lista de apartamentos
print(apartamentos)

