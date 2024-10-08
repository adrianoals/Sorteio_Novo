from django.shortcuts import render, redirect
from django.utils import timezone
import random
from django.http import HttpResponse
from openpyxl import Workbook  # Para gerar o Excel
import qrcode  # Para gerar o QR Code
from io import BytesIO  # Para manipular imagens em memória
from .models import Apartamento, Vaga, Sorteio

# def tres_coelhos_sorteio(request):
#     if request.method == 'POST':
#         # Limpar registros anteriores de sorteio
#         Sorteio.objects.all().delete()
#         print("Sorteios anteriores apagados.")

#         # Obter apartamentos PNE, Idosos e Normais
#         apartamentos_pne = list(Apartamento.objects.filter(is_pne=True))
#         apartamentos_idoso = list(Apartamento.objects.filter(is_idoso=True))
#         apartamentos_normais = list(Apartamento.objects.filter(is_pne=False, is_idoso=False))

#         print(f"Apartamentos PNE: {len(apartamentos_pne)}")
#         print(f"Apartamentos Idosos: {len(apartamentos_idoso)}")
#         print(f"Apartamentos Normais: {len(apartamentos_normais)}")

#         # Obter vagas do banco de dados separadas por especialidade e tipo
#         vagas_pne = list(Vaga.objects.filter(especial='PNE', tipo='LIVRE'))
#         vagas_pne_duplas = list(Vaga.objects.filter(especial='PNE', tipo='DUPLA'))
#         vagas_idosos = list(Vaga.objects.filter(especial='IDOSO', tipo='LIVRE'))
#         vagas_idosos_duplas = list(Vaga.objects.filter(especial='IDOSO', tipo='DUPLA'))
#         vagas_livres = list(Vaga.objects.filter(especial='NORMAL', tipo='LIVRE'))

#         print(f"Vagas PNE Livres: {len(vagas_pne)}, Vagas PNE Duplas: {len(vagas_pne_duplas)}")
#         print(f"Vagas Idosos Livres: {len(vagas_idosos)}, Vagas Idosos Duplas: {len(vagas_idosos_duplas)}")
#         print(f"Vagas Livres: {len(vagas_livres)}")

#         # Apartamentos que já ganharam vagas especiais (para não concorrerem nas vagas livres)
#         apartamentos_com_vaga = []

#         # **Sorteio Aleatório para PNE**
#         random.shuffle(vagas_pne)  # Aleatoriza as vagas PNE
#         for vaga in vagas_pne + vagas_pne_duplas:
#             if apartamentos_pne:
#                 apartamento_escolhido = random.choice(apartamentos_pne)
#                 Sorteio.objects.create(apartamento=apartamento_escolhido, vaga=vaga)
#                 print(f"Sorteado: {apartamento_escolhido.numero} para a vaga PNE {vaga.numero}")
#                 apartamentos_pne.remove(apartamento_escolhido)
#                 apartamentos_com_vaga.append(apartamento_escolhido)  # Marcar apartamento com vaga
#             else:
#                 # Adiciona as vagas PNE nas vagas livres, já que não há apartamentos PNE
#                 if vaga.is_livre_quando_nao_especial:  # Apenas se a vaga puder ser livre
#                     vagas_livres.append(vaga)
#                     print(f"Vaga PNE {vaga.numero} incluída nas vagas livres.")

#         # **Sorteio Aleatório para Idosos**
#         random.shuffle(vagas_idosos)  # Aleatoriza as vagas Idosos
#         for vaga in vagas_idosos + vagas_idosos_duplas:
#             if apartamentos_idoso:
#                 apartamento_escolhido = random.choice(apartamentos_idoso)
#                 Sorteio.objects.create(apartamento=apartamento_escolhido, vaga=vaga)
#                 print(f"Sorteado: {apartamento_escolhido.numero} para a vaga Idoso {vaga.numero}")
#                 apartamentos_idoso.remove(apartamento_escolhido)
#                 apartamentos_com_vaga.append(apartamento_escolhido)  # Marcar apartamento com vaga
#             else:
#                 # Adiciona as vagas Idosos nas vagas livres, já que não há apartamentos Idosos
#                 if vaga.is_livre_quando_nao_especial:  # Apenas se a vaga puder ser livre
#                     vagas_livres.append(vaga)
#                     print(f"Vaga Idoso {vaga.numero} incluída nas vagas livres.")

#         # Unir apartamentos que não conseguiram vagas especiais com apartamentos normais
#         apartamentos_disponiveis = apartamentos_normais + [apto for apto in apartamentos_pne + apartamentos_idoso if apto not in apartamentos_com_vaga]

#         # **Aleatorizar apartamentos** para o sorteio, mas exibir em ordem de ID depois
#         random.shuffle(apartamentos_disponiveis)  # Mistura os apartamentos aleatoriamente
#         print(f"Apartamentos disponíveis (misturados aleatoriamente) para vagas livres: {len(apartamentos_disponiveis)}")

#         # Sortear vagas livres para os apartamentos disponíveis
#         for apartamento in apartamentos_disponiveis:
#             if vagas_livres:
#                 vaga_escolhida = random.choice(vagas_livres)
#                 Sorteio.objects.create(apartamento=apartamento, vaga=vaga_escolhida)
#                 print(f"Sorteado: {apartamento.numero} para a vaga Livre {vaga_escolhida.numero}")
#                 vagas_livres.remove(vaga_escolhida)
#             else:
#                 break  # Sem mais vagas livres

#         # Armazenar informações do sorteio na sessão
#         request.session['sorteio_iniciado'] = True
#         request.session['horario_conclusao'] = timezone.localtime().strftime("%d/%m/%Y às %Hh %Mmin e %Ss")

#         return redirect('tres_coelhos_sorteio')

#     else:
#         sorteio_iniciado = request.session.get('sorteio_iniciado', False)
#         # Exibe os resultados sorteados, ordenados por ID do apartamento
#         resultados_sorteio = Sorteio.objects.select_related('apartamento', 'vaga').order_by('apartamento__id').all()
#         vagas_atribuidas = resultados_sorteio.exists()

#         return render(request, 'tres_coelhos/tres_coelhos_sorteio.html', {
#             'resultados_sorteio': resultados_sorteio,
#             'vagas_atribuidas': vagas_atribuidas,
#             'sorteio_iniciado': sorteio_iniciado,
#             'horario_conclusao': request.session.get('horario_conclusao', '')
#         })

def tres_coelhos_sorteio(request):
    if request.method == 'POST':
        # Limpar registros anteriores de sorteio
        Sorteio.objects.all().delete()
        print("Sorteios anteriores apagados.")

        # Obter apartamentos PNE, Idosos e Normais
        apartamentos_pne = list(Apartamento.objects.filter(is_pne=True))
        apartamentos_idoso = list(Apartamento.objects.filter(is_idoso=True))
        apartamentos_normais = list(Apartamento.objects.filter(is_pne=False, is_idoso=False))

        print(f"Apartamentos PNE: {len(apartamentos_pne)}")
        print(f"Apartamentos Idosos: {len(apartamentos_idoso)}")
        print(f"Apartamentos Normais: {len(apartamentos_normais)}")

        # Obter vagas do banco de dados separadas por especialidade e tipo
        vagas_pne = list(Vaga.objects.filter(especial='PNE', tipo='LIVRE'))
        vagas_pne_duplas = list(Vaga.objects.filter(especial='PNE', tipo='DUPLA'))
        vagas_idosos = list(Vaga.objects.filter(especial='IDOSO', tipo='LIVRE'))
        vagas_idosos_duplas = list(Vaga.objects.filter(especial='IDOSO', tipo='DUPLA'))
        vagas_livres = list(Vaga.objects.filter(especial='NORMAL', tipo='LIVRE'))

        print(f"Vagas PNE Livres: {len(vagas_pne)}, Vagas PNE Duplas: {len(vagas_pne_duplas)}")
        print(f"Vagas Idosos Livres: {len(vagas_idosos)}, Vagas Idosos Duplas: {len(vagas_idosos_duplas)}")
        print(f"Vagas Livres: {len(vagas_livres)}")

        # Apartamentos que já ganharam vagas especiais (para não concorrerem nas vagas livres)
        apartamentos_com_vaga = []

        # **Sorteio Aleatório para PNE (apenas vagas livres)**
        random.shuffle(vagas_pne)  # Aleatoriza as vagas PNE livres
        for vaga in vagas_pne:
            if apartamentos_pne:
                apartamento_escolhido = random.choice(apartamentos_pne)
                Sorteio.objects.create(apartamento=apartamento_escolhido, vaga=vaga)
                print(f"Sorteado: {apartamento_escolhido.numero} para a vaga PNE {vaga.numero}")
                apartamentos_pne.remove(apartamento_escolhido)
                apartamentos_com_vaga.append(apartamento_escolhido)  # Marcar apartamento com vaga
            else:
                # Adiciona as vagas PNE nas vagas livres, já que não há apartamentos PNE
                if vaga.is_livre_quando_nao_especial:  # Apenas se a vaga puder ser livre
                    vagas_livres.append(vaga)
                    print(f"Vaga PNE {vaga.numero} incluída nas vagas livres.")

        # **Sorteio Aleatório para PNE (apenas vagas duplas)**
        random.shuffle(vagas_pne_duplas)  # Aleatoriza as vagas PNE duplas
        for vaga in vagas_pne_duplas:
            if apartamentos_pne:
                apartamento_escolhido = random.choice(apartamentos_pne)
                Sorteio.objects.create(apartamento=apartamento_escolhido, vaga=vaga)
                print(f"Sorteado: {apartamento_escolhido.numero} para a vaga PNE Dupla {vaga.numero}")
                apartamentos_pne.remove(apartamento_escolhido)
                apartamentos_com_vaga.append(apartamento_escolhido)  # Marcar apartamento com vaga
            else:
                # Adiciona as vagas PNE duplas nas vagas livres, já que não há apartamentos PNE
                if vaga.is_livre_quando_nao_especial:  # Apenas se a vaga puder ser livre
                    vagas_livres.append(vaga)
                    print(f"Vaga PNE Dupla {vaga.numero} incluída nas vagas livres.")

        # **Sorteio Aleatório para Idosos (apenas vagas livres)**
        random.shuffle(vagas_idosos)  # Aleatoriza as vagas Idosos livres
        for vaga in vagas_idosos:
            if apartamentos_idoso:
                apartamento_escolhido = random.choice(apartamentos_idoso)
                Sorteio.objects.create(apartamento=apartamento_escolhido, vaga=vaga)
                print(f"Sorteado: {apartamento_escolhido.numero} para a vaga Idoso {vaga.numero}")
                apartamentos_idoso.remove(apartamento_escolhido)
                apartamentos_com_vaga.append(apartamento_escolhido)  # Marcar apartamento com vaga
            else:
                # Adiciona as vagas Idosos nas vagas livres, já que não há apartamentos Idosos
                if vaga.is_livre_quando_nao_especial:  # Apenas se a vaga puder ser livre
                    vagas_livres.append(vaga)
                    print(f"Vaga Idoso {vaga.numero} incluída nas vagas livres.")

        # **Sorteio Aleatório para Idosos (apenas vagas duplas)**
        random.shuffle(vagas_idosos_duplas)  # Aleatoriza as vagas Idosos duplas
        for vaga in vagas_idosos_duplas:
            if apartamentos_idoso:
                apartamento_escolhido = random.choice(apartamentos_idoso)
                Sorteio.objects.create(apartamento=apartamento_escolhido, vaga=vaga)
                print(f"Sorteado: {apartamento_escolhido.numero} para a vaga Idoso Dupla {vaga.numero}")
                apartamentos_idoso.remove(apartamento_escolhido)
                apartamentos_com_vaga.append(apartamento_escolhido)  # Marcar apartamento com vaga
            else:
                # Adiciona as vagas Idosos duplas nas vagas livres, já que não há apartamentos Idosos
                if vaga.is_livre_quando_nao_especial:  # Apenas se a vaga puder ser livre
                    vagas_livres.append(vaga)
                    print(f"Vaga Idoso Dupla {vaga.numero} incluída nas vagas livres.")

        # Unir apartamentos que não conseguiram vagas especiais com apartamentos normais
        apartamentos_disponiveis = apartamentos_normais + [apto for apto in apartamentos_pne + apartamentos_idoso if apto not in apartamentos_com_vaga]

        # **Aleatorizar apartamentos** para o sorteio, mas exibir em ordem de ID depois
        random.shuffle(apartamentos_disponiveis)  # Mistura os apartamentos aleatoriamente
        print(f"Apartamentos disponíveis (misturados aleatoriamente) para vagas livres: {len(apartamentos_disponiveis)}")

        # Sortear vagas livres para os apartamentos disponíveis
        for apartamento in apartamentos_disponiveis:
            if vagas_livres:
                vaga_escolhida = random.choice(vagas_livres)
                Sorteio.objects.create(apartamento=apartamento, vaga=vaga_escolhida)
                print(f"Sorteado: {apartamento.numero} para a vaga Livre {vaga_escolhida.numero}")
                vagas_livres.remove(vaga_escolhida)
            else:
                break  # Sem mais vagas livres

        # Armazenar informações do sorteio na sessão
        request.session['sorteio_iniciado'] = True
        request.session['horario_conclusao'] = timezone.localtime().strftime("%d/%m/%Y às %Hh %Mmin e %Ss")

        return redirect('tres_coelhos_sorteio')

    else:
        sorteio_iniciado = request.session.get('sorteio_iniciado', False)
        # Exibe os resultados sorteados, ordenados por ID do apartamento
        resultados_sorteio = Sorteio.objects.select_related('apartamento', 'vaga').order_by('apartamento__id').all()
        vagas_atribuidas = resultados_sorteio.exists()

        return render(request, 'tres_coelhos/tres_coelhos_sorteio.html', {
            'resultados_sorteio': resultados_sorteio,
            'vagas_atribuidas': vagas_atribuidas,
            'sorteio_iniciado': sorteio_iniciado,
            'horario_conclusao': request.session.get('horario_conclusao', '')
        })



# Função para gerar o arquivo Excel
def tres_coelhos_excel(request):
    # Criar o Workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Resultados do Sorteio"

    # Cabeçalho
    ws.append(['Número Apartamento', 'Número Vaga'])

    # Adicionar resultados do sorteio
    resultados_sorteio = Sorteio.objects.select_related('apartamento', 'vaga').order_by('apartamento__id').all()

    for sorteio in resultados_sorteio:
        ws.append([sorteio.apartamento.numero, sorteio.vaga.numero])

    # Configurar a resposta para o download do Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="resultado_sorteio_tres_coelhos.xlsx"'
    
    # Salvar o arquivo Excel na resposta
    wb.save(response)
    
    return response

# Função para gerar o QR Code com os resultados do sorteio
def tres_coelhos_qrcode(request):
    numero_apartamento = request.GET.get('apartamento')
    sorteio_apartamento = Sorteio.objects.filter(apartamento__numero=numero_apartamento).first()

    if sorteio_apartamento:
        # Gerar o conteúdo do QR Code
        qr_text = f"Apartamento: {sorteio_apartamento.apartamento.numero}\nVaga: {sorteio_apartamento.vaga.numero}"
        img = qrcode.make(qr_text)
        
        # Converter a imagem do QR Code em uma resposta de imagem
        response = HttpResponse(content_type="image/png")
        img.save(response, "PNG")
        return response
    else:
        return HttpResponse("Apartamento não encontrado ou não sorteado.")



