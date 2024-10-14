from sky_view.models import Apartamento

# Relação dos apartamentos com base nas regras fornecidas
apartamentos = [
    '0101', '0102', '0103', '0104', '0105',
    '0201', '0202', '0204', '0205', '0223',
    '0301', '0302', '0303', '0304', '0305',
    '0401', '0402', '0403', '0404', '0405',
    '0501', '0502', '0503', '0504', '0505',
    '0601', '0602', '0603', '0604', '0605',
    '0701', '0702', '0703', '0704', '0705',
    '0801', '0802', '0803', '0804', '0805',
    '0901', '0902', '0903', '0904', '0905',
    '1001', '1002', '1003', '1004', '1005',
    '1101', '1102', '1103', '1104', '1105',
    '1201', '1202', '1203', '1204', '1205',
    '1301', '1302', '1303', '1304', '1305',
    '1401', '1402', '1403', '1404', '1405',
    '1501', '1502', '1503', '1504', '1505',
    '1601', '1602', '1603', '1604', '1605'
]

# Apartamentos com direito a vagas duplas
vagas_duplas = ['1601', '1602', '1603', '1604', '1605', '1501', '1502', '1503', '1504', '1505', '1401', '1402']

# Apartamento 1404 tem direito a duas vagas simples
apartamento_duas_vagas_livres = ['1404']

# Função para popular os apartamentos
for apt_num in apartamentos:
    Apartamento.objects.create(
        numero=apt_num,
        direito_vaga_dupla=apt_num in vagas_duplas,
        direito_duas_vagas_livres=apt_num in apartamento_duas_vagas_livres
    )

print("Apartamentos populados com sucesso!")
