python manage.py shell

from tres_coelhos.models import Vaga

# Vagas Duplas com numeração única e referência à vaga "parceira"
vagas_duplas = [
    (1, 2, 'IDOSO'),  # Vaga dupla Idoso (Vaga 01 com Vaga 02)
    (3, 4, 'NORMAL'),  # Vaga dupla normal (Vaga 03 com Vaga 04)
    (5, 6, 'NORMAL'),  # Vaga dupla normal (Vaga 05 com Vaga 06)
    (7, 8, 'NORMAL'),  # Vaga dupla normal (Vaga 07 com Vaga 08)
    (9, 10, 'NORMAL'),  # Vaga dupla normal (Vaga 09 com Vaga 10)
    (11, 12, 'NORMAL'),  # Vaga dupla normal (Vaga 11 com Vaga 12)
    (13, 14, 'NORMAL'),  # Vaga dupla normal (Vaga 13 com Vaga 14)
    (19, 20, 'NORMAL'),  # Vaga dupla normal (Vaga 19 com Vaga 20)
    (21, 22, 'NORMAL'),  # Vaga dupla normal (Vaga 21 com Vaga 22)
    (25, 26, 'PNE', 'NORMAL'),  # Vaga dupla PNE (Vaga 25 PNE, Vaga 26 Normal)
    (27, 28, 'NORMAL'),  # Vaga dupla normal (Vaga 27 com Vaga 28)
    (29, 30, 'NORMAL'),  # Vaga dupla normal (Vaga 29 com Vaga 30)
    (31, 32, 'NORMAL'),  # Vaga dupla normal (Vaga 31 com Vaga 32)
    (33, 34, 'NORMAL'),  # Vaga dupla normal (Vaga 33 com Vaga 34)
    (35, 36, 'NORMAL'),  # Vaga dupla normal (Vaga 35 com Vaga 36)
    (37, 38, 'NORMAL'),  # Vaga dupla normal (Vaga 37 com Vaga 38)
    (39, 40, 'NORMAL'),  # Vaga dupla normal (Vaga 39 com Vaga 40)
    (42, 43, 'NORMAL'),  # Vaga dupla normal (Vaga 42 com Vaga 43)
    (44, 45, 'NORMAL'),  # Vaga dupla normal (Vaga 44 com Vaga 45)
    (46, 47, 'NORMAL'),  # Vaga dupla normal (Vaga 46 com Vaga 47)
    (48, 49, 'NORMAL')   # Vaga dupla normal (Vaga 48 com Vaga 49)
]

# Vagas Livres
vagas_livres = [
    (15, 'PNE'),  # Vaga PNE
    (16, 'NORMAL'),  # Vaga livre normal
    (17, 'NORMAL'),  # Vaga livre normal
    (18, 'NORMAL'),  # Vaga livre normal
    (23, 'NORMAL'),  # Vaga livre normal
    (24, 'NORMAL'),  # Vaga livre normal
    (41, 'NORMAL'),  # Vaga livre normal
    (50, 'NORMAL')   # Vaga livre normal
]

# Criar vagas duplas e associar a vaga parceira no campo 'dupla_com'
for dupla in vagas_duplas:
    if len(dupla) == 4:  # Caso especial da vaga 25 e 26
        numero_1, numero_2, especial_1, especial_2 = dupla
        vaga_1 = Vaga.objects.create(numero=str(numero_1), tipo='DUPLA', especial=especial_1, subsolo=1)
        vaga_2 = Vaga.objects.create(numero=str(numero_2), tipo='DUPLA', especial=especial_2, subsolo=1, dupla_com=vaga_1)
    else:
        numero_1, numero_2, especial = dupla
        vaga_1 = Vaga.objects.create(numero=str(numero_1), tipo='DUPLA', especial=especial, subsolo=1)
        vaga_2 = Vaga.objects.create(numero=str(numero_2), tipo='DUPLA', especial=especial, subsolo=1, dupla_com=vaga_1)
    
    # Associar a vaga 1 com a vaga 2 também
    vaga_1.dupla_com = vaga_2
    vaga_1.save()

# Criar vagas livres
for numero, especial in vagas_livres:
    Vaga.objects.create(numero=str(numero), tipo='LIVRE', especial=especial, subsolo=1)

print("Vagas do Subsolo 01 inseridas corretamente!")
