from tres_coelhos.models import Apartamento, Vaga, SorteioDupla

# Apagar todos os registros de SorteioDupla para garantir que os novos dados sejam inseridos sem conflitos
SorteioDupla.objects.all().delete()
print("Todos os registros de SorteioDupla foram deletados.")

# Dados atualizados para inserção
dados_sorteio_dupla = [
    (1, 72, 73), (2, 70, 71), (3, 61, 62), (4, 71, 70), (5, 87, 88), (6, 83, 84),
    (101, 81, 82), (102, 99, 100), (103, 54, 53), (104, 94, 93), (105, 95, None),
    (106, 98, None), (107, 68, 69), (108, 77, None), (109, 64, 63), (110, 63, 64),
    (111, 73, 72), (112, 88, 87), (201, 53, 54), (202, 66, 65), (203, 65, 66),
    (204, 93, 94), (205, 90, 89), (206, 56, 55), (207, 97, None), (208, 60, 59),
    (209, 55, 56), (210, 85, 86), (211, 57, 58), (212, 58, 57), (301, 78, None),
    (302, 69, 68), (303, 101, 102), (304, 92, 91), (305, 79, None), (306, 91, 92),
    (307, 59, 60), (308, 67, None), (309, 62, 61), (310, 80, None), (311, 76, None),
    (312, 96, None), (401, 27, 28), (402, 28, 27), (403, 51, 52), (404, 52, 51),
    (405, 100, 99), (406, 89, 90), (407, 82, 81), (408, 86, 85), (409, 102, 101),
    (410, 84, 83), (411, 74, 75), (412, 75, 74), (501, 7, 8), (502, 5, 6),
    (503, 49, 48), (504, 10, 9), (505, 1, 2), (506, 6, 5), (507, 36, 35),
    (508, 48, 49), (509, 21, 22), (510, 43, 42), (511, 20, 19), (512, 22, 21),
    (601, 39, 40), (602, 47, 46), (603, 8, 7), (604, 41, None), (605, 46, 47),
    (606, 29, 30), (607, 40, 39), (608, 31, 32), (609, 23, None), (610, 11, 12),
    (611, 2, 1), (612, 35, 36), (701, 18, None), (702, 37, 38), (703, 19, 20),
    (704, 38, 37), (705, 17, None), (706, 50, None), (707, 14, 13), (708, 13, 14),
    (709, 26, 25), (710, 34, 33), (711, 25, 26), (712, 42, 43), (801, 30, 29),
    (802, 3, 4), (803, 33, 34), (804, 4, 3), (805, 16, None), (806, 15, None),
    (807, 12, 11), (808, 44, 45), (809, 24, None), (810, 9, 10), (811, 45, 44),
    (812, 32, 31)
]

# Inserindo os dados atualizados no banco de dados
for numero_apartamento, numero_vaga, dupla_com in dados_sorteio_dupla:
    try:
        apartamento = Apartamento.objects.get(numero=numero_apartamento)
        vaga = Vaga.objects.get(numero=numero_vaga)

        # Atualizar a vaga com a informação de com quem ela faz dupla, se aplicável
        if dupla_com:
            vaga_dupla = Vaga.objects.get(numero=dupla_com)
            vaga.dupla_com = vaga_dupla
            vaga.save()

        # Criar o novo registro em SorteioDupla
        SorteioDupla.objects.create(apartamento=apartamento, vaga=vaga)
        print(f"Sorteio atualizado: Apartamento {numero_apartamento} -> Vaga {numero_vaga} (Dupla com {dupla_com if dupla_com else 'N/A'})")

    except (Apartamento.DoesNotExist, Vaga.DoesNotExist):
        print(f"Apartamento {numero_apartamento} ou Vaga {numero_vaga} não encontrado.")
