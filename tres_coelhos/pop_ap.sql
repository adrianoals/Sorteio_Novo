python manage.py shell

from tres_coelhos.models import Apartamento

# Lista dos apartamentos
apartamentos = [
    1, 2, 3, 4, 5, 6,
    101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 
    201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212,
    301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312,
    401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412,
    501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512,
    601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612,
    701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712,
    801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812
]

# Loop para criar os apartamentos
for numero in apartamentos:
    Apartamento.objects.create(numero=str(numero), is_pne=False, is_idoso=False)

print("Apartamentos inseridos com sucesso!")





