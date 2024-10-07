from django.shortcuts import render, redirect
from django.utils import timezone
import random
from django.http import HttpResponse
from openpyxl import Workbook  # Para gerar o Excel
import qrcode  # Para gerar o QR Code
from io import BytesIO  # Para manipular imagens em memória
from .models import Apartamento, Vaga, Sorteio


def tres_coelhos_sorteio(request):
    if request.method == 'POST':
        # Limpar registros anteriores de sorteio
        Sorteio.objects.all().delete()
        
        # Obter apartamentos PNE, Idosos e Normais
        apartamentos_pne = list(Apartamento.objects.filter(is_pne=True))
        apartamentos_idosos = list(Apartamento.objects.filter(is_idoso=True))
        apartamentos_normais = list(Apartamento.objects.filter(is_pne=False, is_idoso=False))

        # Obter vagas do banco de dados
        vagas_pne = list(Vaga.objects.filter(especial='PNE'))
        vagas_idosos = list(Vaga.objects.filter(especial='IDOSO'))
        vagas_livres = list(Vaga.objects.filter(especial='NORMAL'))

        # Se não houver apartamentos PNE ou Idosos, incluir as vagas especiais nas vagas livres (se for permitido)
        if not apartamentos_pne:
            vagas_livres.extend(vaga for vaga in vagas_pne if vaga.is_livre_quando_nao_especial)
        if not apartamentos_idosos:
            vagas_livres.extend(vaga for vaga in vagas_idosos if vaga.is_livre_quando_nao_especial)

        # Lista para armazenar apartamentos que não conseguiram vagas especiais
        apartamentos_sem_vaga = []

        # Sortear vagas PNE (se houver vagas PNE e apartamentos PNE)
        for vaga in vagas_pne:
            if apartamentos_pne:
                apartamento_escolhido = random.choice(apartamentos_pne)
                Sorteio.objects.create(apartamento=apartamento_escolhido, vaga=vaga)
                apartamentos_pne.remove(apartamento_escolhido)
            else:
                break  # Sem mais apartamentos PNE para sortear

        # Se houver apartamentos PNE sem vagas, eles devem concorrer às vagas livres
        if apartamentos_pne:
            apartamentos_sem_vaga.extend(apartamentos_pne)

        # Sortear vagas Idosos (se houver vagas Idosos e apartamentos Idosos)
        for vaga in vagas_idosos:
            if apartamentos_idosos:
                apartamento_escolhido = random.choice(apartamentos_idosos)
                Sorteio.objects.create(apartamento=apartamento_escolhido, vaga=vaga)
                apartamentos_idosos.remove(apartamento_escolhido)
            else:
                break  # Sem mais apartamentos Idosos para sortear

        # Se houver apartamentos Idosos sem vagas, eles devem concorrer às vagas livres
        if apartamentos_idosos:
            apartamentos_sem_vaga.extend(apartamentos_idosos)

        # Juntar os apartamentos que não conseguiram vagas especiais com os apartamentos normais
        apartamentos_disponiveis = apartamentos_sem_vaga + apartamentos_normais

        # Sortear vagas Livres para todos os apartamentos disponíveis
        for apartamento in apartamentos_disponiveis:
            if vagas_livres:
                vaga_escolhida = random.choice(vagas_livres)
                Sorteio.objects.create(apartamento=apartamento, vaga=vaga_escolhida)
                vagas_livres.remove(vaga_escolhida)
            else:
                break  # Sem mais vagas livres

        # Armazenar informações do sorteio na sessão
        request.session['sorteio_iniciado'] = True
        request.session['horario_conclusao'] = timezone.localtime().strftime("%d/%m/%Y às %Hh %Mmin e %Ss")

        return redirect('tres_coelhos_sorteio')

    else:
        sorteio_iniciado = request.session.get('sorteio_iniciado', False)
        resultados_sorteio = Sorteio.objects.select_related('apartamento', 'vaga').order_by('apartamento__id').all()
        vagas_atribuidas = resultados_sorteio.exists()

        return render(request, 'tres_coelhos/sorteio.html', {
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


def index(request):
    	return render(request, 'portfolio/index.html')
