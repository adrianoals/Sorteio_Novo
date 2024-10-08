python manage.py shell

from tres_coelhos.models import Vaga

# Vagas Duplas no Subsolo 02
vagas_duplas_subsolo_02 = [
    (51, 52, 'NORMAL'),  # Vaga dupla normal (Vaga 51 com Vaga 52)
    (53, 54, 'NORMAL'),  # Vaga dupla normal (Vaga 53 com Vaga 54)
    (55, 56, 'NORMAL'),  # Vaga dupla normal (Vaga 55 com Vaga 56)
    (57, 58, 'NORMAL'),  # Vaga dupla normal (Vaga 57 com Vaga 58)
    (59, 60, 'NORMAL'),  # Vaga dupla normal (Vaga 59 com Vaga 60)
    (61, 62, 'NORMAL'),  # Vaga dupla normal (Vaga 61 com Vaga 62)
    (63, 64, 'NORMAL'),  # Vaga dupla normal (Vaga 63 com Vaga 64)
    (65, 66, 'PNE', 'NORMAL'),  # Vaga dupla PNE (Vaga 65 PNE, Vaga 66 Normal)
    (68, 69, 'NORMAL'),  # Vaga dupla normal (Vaga 68 com Vaga 69)
    (70, 71, 'NORMAL'),  # Vaga dupla normal (Vaga 70 com Vaga 71)
    (72, 73, 'NORMAL'),  # Vaga dupla normal (Vaga 72 com Vaga 73)
    (74, 75, 'NORMAL'),  # Vaga dupla normal (Vaga 74 com Vaga 75)
    (81, 82, 'NORMAL'),  # Vaga dupla normal (Vaga 81 com Vaga 82)
    (83, 84, 'NORMAL'),  # Vaga dupla normal (Vaga 83 com Vaga 84)
    (85, 86, 'NORMAL'),  # Vaga dupla normal (Vaga 85 com Vaga 86)
    (87, 88, 'NORMAL'),  # Vaga dupla normal (Vaga 87 com Vaga 88)
    (89, 90, 'NORMAL'),  # Vaga dupla normal (Vaga 89 com Vaga 90)
    (91, 92, 'NORMAL'),  # Vaga dupla normal (Vaga 91 com Vaga 92)
    (93, 94, 'NORMAL'),  # Vaga dupla normal (Vaga 93 com Vaga 94)
    (99, 100, 'NORMAL'),  # Vaga dupla normal (Vaga 99 com Vaga 100)
    (101, 102, 'NORMAL')  # Vaga dupla normal (Vaga 101 com Vaga 102)
]

# Vagas Livres no Subsolo 02 (inclui vagas PNE e normais)
vagas_livres_subsolo_02 = [
    (67, 'NORMAL'),   # Vaga livre normal
    (76, 'NORMAL'),   # Vaga livre normal
    (77, 'NORMAL'),   # Vaga livre normal
    (78, 'NORMAL'),   # Vaga livre normal
    (79, 'NORMAL'),   # Vaga livre normal
    (80, 'NORMAL'),   # Vaga livre normal
    (95, 'PNE'),      # Vaga PNE
    (96, 'NORMAL'),   # Vaga livre normal
    (97, 'NORMAL'),   # Vaga livre normal
    (98, 'NORMAL')    # Vaga livre normal
]

# Criar vagas duplas e associar a vaga parceira no campo 'dupla_com'
for dupla in vagas_duplas_subsolo_02:
    if len(dupla) == 4:  # Caso especial da vaga 65 e 66 (PNE e normal)
        numero_1, numero_2, especial_1, especial_2 = dupla
        vaga_1 = Vaga.objects.create(numero=str(numero_1), tipo='DUPLA', especial=especial_1, subsolo=2)
        vaga_2 = Vaga.objects.create(numero=str(numero_2), tipo='DUPLA', especial=especial_2, subsolo=2, dupla_com=vaga_1)
    else:
        numero_1, numero_2, especial = dupla
        vaga_1 = Vaga.objects.create(numero=str(numero_1), tipo='DUPLA', especial=especial, subsolo=2)
        vaga_2 = Vaga.objects.create(numero=str(numero_2), tipo='DUPLA', especial=especial, subsolo=2, dupla_com=vaga_1)
    
    # Associar a vaga 1 com a vaga 2 também
    vaga_1.dupla_com = vaga_2
    vaga_1.save()

# Criar vagas livres
for numero, especial in vagas_livres_subsolo_02:
    Vaga.objects.create(numero=str(numero), tipo='LIVRE', especial=especial, subsolo=2)

print("Vagas do Subsolo 02 inseridas corretamente!")
