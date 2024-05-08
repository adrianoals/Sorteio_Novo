from django.db import models

class Apartamento(models.Model):
    
    APARTAMENTO_CHOICES = [
        ('Apto 101', 'Apto 101'),
        ('Apto 102', 'Apto 102'),
        ('Apto 103', 'Apto 103'),
        ('Apto 104', 'Apto 104'),        
        ('Apto 201', 'Apto 201'),
        ('Apto 202', 'Apto 202'),
        ('Apto 203', 'Apto 203'),
        ('Apto 204', 'Apto 204'),        
        ('Apto 301', 'Apto 301'),
        ('Apto 302', 'Apto 302'),
        ('Apto 303', 'Apto 303'),
        ('Apto 304', 'Apto 304'),        
        ('Apto 401', 'Apto 401'),
        ('Apto 402', 'Apto 402'),
        ('Apto 403', 'Apto 403'),
        ('Apto 404', 'Apto 404'),
        ('Apto 501', 'Apto 501'),
        ('Apto 502', 'Apto 502'),
        ('Apto 503', 'Apto 503'),
        ('Apto 504', 'Apto 504'),
        ('Apto 601', 'Apto 601'),
        ('Apto 602', 'Apto 602'),
        ('Apto 603', 'Apto 603'),
        ('Apto 604', 'Apto 604'),
        ('Apto 701', 'Apto 701'),
        ('Apto 702', 'Apto 702'),
        ('Apto 703', 'Apto 703'),
        ('Apto 704', 'Apto 704'),
        ('Apto 801', 'Apto 801'),
        ('Apto 802', 'Apto 802'),
        ('Apto 803', 'Apto 803'),
        ('Apto 804', 'Apto 804'),
        ('Apto 901', 'Apto 901'),
        ('Apto 902', 'Apto 902'),
        ('Apto 903', 'Apto 903'),
        ('Apto 904', 'Apto 904'),
        ('Apto 1001', 'Apto 1001'),
        ('Apto 1002', 'Apto 1002'),
        ('Apto 1003', 'Apto 1003'),
        ('Apto 1004', 'Apto 1004'),
        ('Apto 1101', 'Apto 1101'),
        ('Apto 1102', 'Apto 1102'),
        ('Apto 1103', 'Apto 1103'),
        ('Apto 1104', 'Apto 1104'),
        ('Apto 1201', 'Apto 1201'),
        ('Apto 1202', 'Apto 1202'),
        ('Apto 1203', 'Apto 1203'),
        ('Apto 1204', 'Apto 1204'),
        ('Apto 1301', 'Apto 1301'),
        ('Apto 1302', 'Apto 1302'),
        ('Apto 1303', 'Apto 1303'),
        ('Apto 1304', 'Apto 1304'),
        ('Apto 1401', 'Apto 1401'),
        ('Apto 1402', 'Apto 1402'),
        ('Apto 1403', 'Apto 1403'),
        ('Apto 1404', 'Apto 1404'),        
    ]

    numero_apartamento = models.CharField(max_length=50, choices=APARTAMENTO_CHOICES)

    def __str__(self):
        return f"{self.numero_apartamento}"


class GrupoVaga(models.Model):

    VAGAS_CHOICES = [
        ('Vaga 01, Vaga 10 e Vaga 11', 'Vaga 01, Vaga 10 e Vaga 11'), 
        ('Vaga 02, Vaga 12 e Vaga 13', 'Vaga 02, Vaga 12 e Vaga 13'), 
        ('Vaga 03, Vaga 17 e Vaga 18', 'Vaga 03, Vaga 17 e Vaga 18'), 
        ('Vaga 04, Vaga 19 e Vaga 20', 'Vaga 04, Vaga 19 e Vaga 20'), 
        ('Vaga 05, Vaga 21 e Vaga 22', 'Vaga 05, Vaga 21 e Vaga 22'), 
        ('Vaga 06, Vaga 23 e Vaga 24', 'Vaga 06, Vaga 23 e Vaga 24'), 
        ('Vaga 07, Vaga 25 e Vaga 26', 'Vaga 07, Vaga 25 e Vaga 26'), 
        ('Vaga 08, Vaga 27 e Vaga 28', 'Vaga 08, Vaga 27 e Vaga 28'), 
        ('Vaga 09, Vaga 29 e Vaga 30', 'Vaga 09, Vaga 29 e Vaga 30'), 
        ('Vaga 14, Vaga 31 e Vaga 32', 'Vaga 14, Vaga 31 e Vaga 32'), 
        ('Vaga 15, Vaga 33 e Vaga 34', 'Vaga 15, Vaga 33 e Vaga 34'), 
        ('Vaga 35, Vaga 36 e Vaga 37', 'Vaga 35, Vaga 36 e Vaga 37'), 
        ('Vaga 38, Vaga 39 e Vaga 40', 'Vaga 38, Vaga 39 e Vaga 40'), 
        ('Vaga 41, Vaga 42 e Vaga 43', 'Vaga 41, Vaga 42 e Vaga 43'), 
        ('Vaga 44, Vaga 45 e Vaga 46', 'Vaga 44, Vaga 45 e Vaga 46'), 
        ('Vaga 47, Vaga 56 e Vaga 57', 'Vaga 47, Vaga 56 e Vaga 57'), 
        ('Vaga 48, Vaga 58 e Vaga 59', 'Vaga 48, Vaga 58 e Vaga 59'), 
        ('Vaga 49, Vaga 50 e Vaga 51', 'Vaga 49, Vaga 50 e Vaga 51'), 
        ('Vaga 52, Vaga 53 e Vaga 54', 'Vaga 52, Vaga 53 e Vaga 54'), 
        ('Vaga 55, Vaga 60 e Vaga 61', 'Vaga 55, Vaga 60 e Vaga 61'), 
        ('Vaga 62, Vaga 64 e Vaga 66', 'Vaga 62, Vaga 64 e Vaga 66'), 
        ('Vaga 63, Vaga 65 e Vaga 67', 'Vaga 63, Vaga 65 e Vaga 67'), 
        ('Vaga 79, Vaga 68 e Vaga 69', 'Vaga 79, Vaga 68 e Vaga 69'), 
        ('Vaga 80, Vaga 70 e Vaga 71', 'Vaga 80, Vaga 70 e Vaga 71'), 
        ('Vaga 81, Vaga 72 e Vaga 73', 'Vaga 81, Vaga 72 e Vaga 73'), 
        ('Vaga 82, Vaga 74 e Vaga 75', 'Vaga 82, Vaga 74 e Vaga 75'), 
        ('Vaga 83, Vaga 84 e Vaga 85', 'Vaga 83, Vaga 84 e Vaga 85'), 
        ('Vaga 86, Vaga 87 e Vaga 88', 'Vaga 86, Vaga 87 e Vaga 88'), 
        ('Vaga 76, Vaga 77 e Vaga 78', 'Vaga 76, Vaga 77 e Vaga 78'), 
        ('Vaga 89, Vaga 90 e Vaga 91', 'Vaga 89, Vaga 90 e Vaga 91'), 
        ('Vaga 92, Vaga 102 e Vaga 103', 'Vaga 92, Vaga 102 e Vaga 103'),
        ('Vaga 93, Vaga 104 e Vaga 105', 'Vaga 93, Vaga 104 e Vaga 105'),
        ('Vaga 94, Vaga 95 e Vaga 96', 'Vaga 94, Vaga 95 e Vaga 96'), 
        ('Vaga 97, Vaga 98 e Vaga 99', 'Vaga 97, Vaga 98 e Vaga 99'), 
        ('Vaga 100, Vaga 101 e Vaga 106', 'Vaga 100, Vaga 101 e Vaga 106'),
        ('Vaga 107, Vaga 125 e Vaga 126', 'Vaga 107, Vaga 125 e Vaga 126'),
        ('Vaga 108, Vaga 110 e Vaga 112', 'Vaga 108, Vaga 110 e Vaga 112'), 
        ('Vaga 109, Vaga 111 e Vaga 113', 'Vaga 109, Vaga 111 e Vaga 113'),
        ('Vaga 127, Vaga 114 e Vaga 115', 'Vaga 127, Vaga 114 e Vaga 115'), 
        ('Vaga 128, Vaga 116 e Vaga 117', 'Vaga 128, Vaga 116 e Vaga 117'),
        ('Vaga 129, Vaga 118 e Vaga 119', 'Vaga 129, Vaga 118 e Vaga 119'), 
        ('Vaga 130, Vaga 120 e Vaga 121', 'Vaga 130, Vaga 120 e Vaga 121'), 
        ('Vaga 131, Vaga 132 e Vaga 133', 'Vaga 131, Vaga 132 e Vaga 133'),
        ('Vaga 134, Vaga 135 e Vaga 136', 'Vaga 134, Vaga 135 e Vaga 136'),
        ('Vaga 122, Vaga 123 e Vaga 124', 'Vaga 122, Vaga 123 e Vaga 124'),
        ('Vaga 139, Vaga 137 e Vaga 138', 'Vaga 139, Vaga 137 e Vaga 138'), 
        ('Vaga 140, Vaga 157 e Vaga 158', 'Vaga 140, Vaga 157 e Vaga 158'), 
        ('Vaga 141, Vaga 143 e Vaga 145', 'Vaga 141, Vaga 143 e Vaga 145'), 
        ('Vaga 142, Vaga 144 e Vaga 146', 'Vaga 142, Vaga 144 e Vaga 146'),
        ('Vaga 159, Vaga 160 e Vaga 161', 'Vaga 159, Vaga 160 e Vaga 161'), 
        ('Vaga 16, Vaga 162 e Vaga 163', 'Vaga 16, Vaga 162 e Vaga 163'), 
        ('Vaga 164, Vaga 147 e Vaga 148', 'Vaga 164, Vaga 147 e Vaga 148'),
        ('Vaga 165, Vaga 149 e Vaga 150', 'Vaga 165, Vaga 149 e Vaga 150'), 
        ('Vaga 166, Vaga 151 e Vaga 152', 'Vaga 166, Vaga 151 e Vaga 152'),
        ('Vaga 167, Vaga 153 e Vaga 154', 'Vaga 167, Vaga 153 e Vaga 154'),
        ('Vaga 168, Vaga 155 e Vaga 156', 'Vaga 168, Vaga 155 e Vaga 156'),     
    ]

    vagas = models.CharField(max_length=50, unique=True, choices=VAGAS_CHOICES)

    def __str__(self):
        return self.vagas


class Sorteio(models.Model):
    apartamento = models.OneToOneField(Apartamento, on_delete=models.CASCADE)
    vagas = models.OneToOneField(GrupoVaga, on_delete=models.CASCADE)

    def __str__(self):
        # Acesso ao bloco através do apartamento
        return f"Apartamento {self.apartamento.numero_apartamento}  Vagas: {self.vagas.vagas}"



# class VagaSimples(models.Model):

#     VAGA_SIMPLES_CHOICES = [
#         ('Vaga 01', 'Vaga 01'),
#         ('Vaga 02', 'Vaga 02'),
#         ('Vaga 03', 'Vaga 03'),
#         ('Vaga 04', 'Vaga 04'),
#         ('Vaga 05', 'Vaga 05'), 
#         ('Vaga 06', 'Vaga 06'), 
#         ('Vaga 07', 'Vaga 07'), 
#         ('Vaga 08', 'Vaga 08'), 
#         ('Vaga 09', 'Vaga 09'), 
#         ('Vaga 10', 'Vaga 10'), 
#         ('Vaga 11', 'Vaga 11'), 
#         ('Vaga 12', 'Vaga 12'), 
#         ('Vaga 13', 'Vaga 13'), 
#         ('Vaga 14', 'Vaga 14'), 
#         ('Vaga 15', 'Vaga 15'), 
#         ('Vaga 16', 'Vaga 16'), 
#         ('Vaga 17', 'Vaga 17'), 
#         ('Vaga 18', 'Vaga 18'), 
#         ('Vaga 19', 'Vaga 19'), 
#         ('Vaga 20', 'Vaga 20'),
#         ('Vaga 21', 'Vaga 21'),
#         ('Vaga 22', 'Vaga 22'),
#         ('Vaga 23', 'Vaga 23'),
#         ('Vaga 24', 'Vaga 24'),
#         ('Vaga 25', 'Vaga 25'),
#         ('Vaga 26', 'Vaga 26'),
#         ('Vaga 27', 'Vaga 27'),
#         ('Vaga 28', 'Vaga 28'),
#         ('Vaga 29', 'Vaga 29'),
#         ('Vaga 30', 'Vaga 30'),
#         ('Vaga 31', 'Vaga 31'),
#         ('Vaga 32', 'Vaga 32'),
#         ('Vaga 33', 'Vaga 33'),
#         ('Vaga 34', 'Vaga 34'),
#         ('Vaga 35', 'Vaga 35'),
#         ('Vaga 36', 'Vaga 36'),
#         ('Vaga 37', 'Vaga 37'),
#         ('Vaga 38', 'Vaga 38'),
#         ('Vaga 39', 'Vaga 39'),
#         ('Vaga 40', 'Vaga 40'),
#         ('Vaga 41', 'Vaga 41'),
#         ('Vaga 42', 'Vaga 42'),
#         ('Vaga 43', 'Vaga 43'),
#         ('Vaga 44', 'Vaga 44'),
#         ('Vaga 45', 'Vaga 45'),
#         ('Vaga 46', 'Vaga 46'),
#         ('Vaga 47', 'Vaga 47'),
#         ('Vaga 48', 'Vaga 48'),
#         ('Vaga 49', 'Vaga 49'),
#         ('Vaga 50', 'Vaga 50'),
#         ('Vaga 51', 'Vaga 51'),
#         ('Vaga 52', 'Vaga 52'),
#         ('Vaga 53', 'Vaga 53'),
#         ('Vaga 54', 'Vaga 54'),
#         ('Vaga 55', 'Vaga 55'),
#         ('Vaga 56', 'Vaga 56'),
#     ]

#     vaga_simples = models.CharField(max_length=50, unique=True, choices=VAGA_SIMPLES_CHOICES)

#     def __str__(self):
#         return self.vaga_simples

# class VagaDupla(models.Model):

#     VAGA_DUPLA_CHOICES = [
#         ('Vaga 01 e 02', 'Vaga 01 e 02'),
#         ('Vaga 03 e 04', 'Vaga 03 e 04'),
#         ('Vaga 05 e 06', 'Vaga 05 e 06'),
#         ('Vaga 07 e 08', 'Vaga 07 e 08'),
#         ('Vaga 09 e 10', 'Vaga 09 e 10'),
#         ('Vaga 11 e 12', 'Vaga 11 e 12'),
#         ('Vaga 13 e 14', 'Vaga 13 e 14'),
#         ('Vaga 15 e 16', 'Vaga 15 e 16'),
#         ('Vaga 17 e 18', 'Vaga 17 e 18'),
#         ('Vaga 19 e 20', 'Vaga 19 e 20'),
#         ('Vaga 21 e 22', 'Vaga 21 e 22'),
#         ('Vaga 23 e 24', 'Vaga 23 e 24'),
#         ('Vaga 25 e 26', 'Vaga 25 e 26'),
#         ('Vaga 27 e 28', 'Vaga 27 e 28'),
#         ('Vaga 29 e 30', 'Vaga 29 e 30'),
#         ('Vaga 31 e 32', 'Vaga 31 e 32'),
#         ('Vaga 33 e 34', 'Vaga 33 e 34'),
#         ('Vaga 35 e 36', 'Vaga 35 e 36'),
#         ('Vaga 37 e 38', 'Vaga 37 e 38'),
#         ('Vaga 39 e 40', 'Vaga 39 e 40'),
#         ('Vaga 41 e 42', 'Vaga 41 e 42'),
#         ('Vaga 43 e 44', 'Vaga 43 e 44'),
#         ('Vaga 45 e 46', 'Vaga 45 e 46'),
#         ('Vaga 47 e 48', 'Vaga 47 e 48'),
#         ('Vaga 49 e 50', 'Vaga 49 e 50'),
#         ('Vaga 51 e 52', 'Vaga 51 e 52'),
#         ('Vaga 53 e 54', 'Vaga 53 e 54'),
#         ('Vaga 55 e 56', 'Vaga 55 e 56'),
#         ('Vaga 57 e 58', 'Vaga 57 e 58'),
#         ('Vaga 59 e 60', 'Vaga 59 e 60'),
#         ('Vaga 61 e 62', 'Vaga 61 e 62'),
#         ('Vaga 63 e 64', 'Vaga 63 e 64'),
#         ('Vaga 65 e 66', 'Vaga 65 e 66'),
#         ('Vaga 67 e 68', 'Vaga 67 e 68'),
#         ('Vaga 69 e 70', 'Vaga 69 e 70'),
#         ('Vaga 71 e 72', 'Vaga 71 e 72'),
#         ('Vaga 73 e 74', 'Vaga 73 e 74'),
#         ('Vaga 75 e 76', 'Vaga 75 e 76'),
#         ('Vaga 77 e 78', 'Vaga 77 e 78'),
#         ('Vaga 79 e 80', 'Vaga 79 e 80'),
#         ('Vaga 81 e 82', 'Vaga 81 e 82'),
#         ('Vaga 83 e 84', 'Vaga 83 e 84'),
#         ('Vaga 85 e 86', 'Vaga 85 e 86'),
#         ('Vaga 87 e 88', 'Vaga 87 e 88'),
#         ('Vaga 89 e 90', 'Vaga 89 e 90'),
#         ('Vaga 91 e 92', 'Vaga 91 e 92'),
#         ('Vaga 93 e 94', 'Vaga 93 e 94'),
#         ('Vaga 95 e 96', 'Vaga 95 e 96'),
#         ('Vaga 97 e 98', 'Vaga 97 e 98'),
#         ('Vaga 99 e 100', 'Vaga 99 e 100'),
#         ('Vaga 101 e 102', 'Vaga 101 e 102'),
#         ('Vaga 103 e 104', 'Vaga 103 e 104'),
#         ('Vaga 105 e 106', 'Vaga 105 e 106'),
#         ('Vaga 107 e 108', 'Vaga 107 e 108'),
#         ('Vaga 109 e 110', 'Vaga 109 e 110'),
#         ('Vaga 111 e 112', 'Vaga 111 e 112'),
#     ]

#     vaga_dupla = models.CharField(max_length=50, unique=True, choices=VAGA_DUPLA_CHOICES)

#     def __str__(self):
#         return self.vaga_dupla





