from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.utils import timezone
import random
from django.http import HttpResponse
# from openpyxl import Workbook  # Para gerar o Excel
from openpyxl import load_workbook
import qrcode  # Para gerar o QR Code
from io import BytesIO  # Para manipular imagens em memória
from .models import Apartamento, Vaga, Sorteio, SorteioDupla, DuplaApartamentos


def sky_view_sorteio(request):
    if request.method == 'POST':
        # Limpar registros anteriores de sorteio
        Sorteio.objects.all().delete()
        print("Sorteios anteriores apagados.")

        # Obter apartamentos PNE, Idosos e Normais, excluindo os com apenas_dupla=True onde não aplicável
        apartamentos_pne_apenas_livre = list(Apartamento.objects.filter(is_pne=True, apenas_livre=True, apenas_dupla=False))
        apartamentos_pne_sem_restricao = list(Apartamento.objects.filter(is_pne=True, apenas_livre=False, apenas_dupla=False))
        apartamentos_idoso = list(Apartamento.objects.filter(is_idoso=True, apenas_dupla=False))
        apartamentos_normais = list(Apartamento.objects.filter(is_pne=False, is_idoso=False, apenas_dupla=False))

        print(f"Apartamentos PNE (apenas livres): {len(apartamentos_pne_apenas_livre)}")
        print(f"Apartamentos PNE (sem restrições): {len(apartamentos_pne_sem_restricao)}")
        print(f"Apartamentos Idosos: {len(apartamentos_idoso)}")
        print(f"Apartamentos Normais: {len(apartamentos_normais)}")

        # Obter vagas do banco de dados separadas por especialidade e tipo
        vagas_pne_livres = list(Vaga.objects.filter(especial='PNE', tipo='LIVRE'))
        vagas_pne_duplas = list(Vaga.objects.filter(especial='PNE', tipo='DUPLA'))
        vagas_idosos = list(Vaga.objects.filter(especial='IDOSO', tipo='LIVRE'))
        vagas_idosos_duplas = list(Vaga.objects.filter(especial='IDOSO', tipo='DUPLA'))
        vagas_livres = list(Vaga.objects.filter(especial='NORMAL', tipo='LIVRE'))

        print(f"Vagas PNE Livres: {len(vagas_pne_livres)}, Vagas PNE Duplas: {len(vagas_pne_duplas)}")
        print(f"Vagas Idosos Livres: {len(vagas_idosos)}, Vagas Idosos Duplas: {len(vagas_idosos_duplas)}")
        print(f"Vagas Livres: {len(vagas_livres)}")

        # Apartamentos que já ganharam vagas especiais (para não concorrerem nas vagas livres)
        apartamentos_com_vaga = []

        # **Sorteio prioritário para PNE com apenas_livre=True (vagas livres PNE)**
        random.shuffle(vagas_pne_livres)  # Aleatoriza as vagas PNE livres
        for vaga in vagas_pne_livres:
            if apartamentos_pne_apenas_livre:
                apartamento_escolhido = random.choice(apartamentos_pne_apenas_livre)
                Sorteio.objects.create(apartamento=apartamento_escolhido, vaga=vaga)
                print(f"Sorteado (PNE - apenas_livre): {apartamento_escolhido.numero} para a vaga PNE Livre {vaga.numero}")
                apartamentos_pne_apenas_livre.remove(apartamento_escolhido)
                apartamentos_com_vaga.append(apartamento_escolhido)
            else:
                # Se todos apartamentos com restrição já foram sorteados, preencher as vagas restantes com apartamentos sem restrição
                if apartamentos_pne_sem_restricao:
                    apartamento_escolhido = random.choice(apartamentos_pne_sem_restricao)
                    Sorteio.objects.create(apartamento=apartamento_escolhido, vaga=vaga)
                    print(f"Sorteado (PNE - sem restrição): {apartamento_escolhido.numero} para a vaga PNE Livre {vaga.numero}")
                    apartamentos_pne_sem_restricao.remove(apartamento_escolhido)
                    apartamentos_com_vaga.append(apartamento_escolhido)
                else:
                    if vaga.is_livre_quando_nao_especial:  # Apenas se a vaga puder ser livre
                        vagas_livres.append(vaga)
                        print(f"Vaga PNE {vaga.numero} incluída nas vagas livres.")

        # **Sorteio para PNE sem restrição (vagas duplas PNE)**
        random.shuffle(vagas_pne_duplas)  # Aleatoriza as vagas PNE duplas
        for vaga in vagas_pne_duplas:
            # Filtrar apartamentos que estão no mesmo subsolo da vaga
            apartamentos_elegiveis = [ap for ap in apartamentos_pne_sem_restricao if ap.subsolo == vaga.subsolo]
            if apartamentos_elegiveis:
                apartamento_escolhido = random.choice(apartamentos_elegiveis)
                Sorteio.objects.create(apartamento=apartamento_escolhido, vaga=vaga)
                print(f"Sorteado (PNE - sem restrição): {apartamento_escolhido.numero} para a vaga PNE Dupla {vaga.numero}")
                apartamentos_pne_sem_restricao.remove(apartamento_escolhido)
                apartamentos_com_vaga.append(apartamento_escolhido)
            else:
                if vaga.is_livre_quando_nao_especial:  # Apenas se a vaga puder ser livre
                    vagas_livres.append(vaga)
                    print(f"Vaga PNE Dupla {vaga.numero} incluída nas vagas livres.")

        # **Sorteio Aleatório para Idosos (apenas vagas livres)**
        random.shuffle(vagas_idosos)  # Aleatoriza as vagas Idosos livres
        for vaga in vagas_idosos:
            apartamentos_elegiveis = [ap for ap in apartamentos_idoso if ap.subsolo == vaga.subsolo and not ap.apenas_dupla]
            if apartamentos_elegiveis:
                apartamento_escolhido = random.choice(apartamentos_elegiveis)
                Sorteio.objects.create(apartamento=apartamento_escolhido, vaga=vaga)
                print(f"Sorteado: {apartamento_escolhido.numero} para a vaga Idoso {vaga.numero}")
                apartamentos_idoso.remove(apartamento_escolhido)
                apartamentos_com_vaga.append(apartamento_escolhido)
            else:
                if vaga.is_livre_quando_nao_especial:
                    vagas_livres.append(vaga)

        # **Sorteio Aleatório para Idosos (apenas vagas duplas)**
        random.shuffle(vagas_idosos_duplas)
        for vaga in vagas_idosos_duplas:
            apartamentos_elegiveis = [ap for ap in apartamentos_idoso if ap.subsolo == vaga.subsolo and not ap.apenas_livre]
            if apartamentos_elegiveis:
                apartamento_escolhido = random.choice(apartamentos_elegiveis)
                Sorteio.objects.create(apartamento=apartamento_escolhido, vaga=vaga)
                apartamentos_idoso.remove(apartamento_escolhido)
                apartamentos_com_vaga.append(apartamento_escolhido)
            else:
                if vaga.is_livre_quando_nao_especial:
                    vagas_livres.append(vaga)

        # **Sorteio de apartamentos restantes para vagas livres**
        apartamentos_disponiveis = apartamentos_normais + [ap for ap in apartamentos_pne_apenas_livre + apartamentos_pne_sem_restricao + apartamentos_idoso if ap not in apartamentos_com_vaga]

        random.shuffle(apartamentos_disponiveis)
        for apartamento in apartamentos_disponiveis:
            vagas_filtradas = [v for v in vagas_livres if v.subsolo == apartamento.subsolo]
            if vagas_filtradas:
                vaga_escolhida = random.choice(vagas_filtradas)
                Sorteio.objects.create(apartamento=apartamento, vaga=vaga_escolhida)
                print(f"Sorteado: {apartamento.numero} para a vaga Livre {vaga_escolhida.numero}")
                vagas_livres.remove(vaga_escolhida)
            else:
                print(f"Sem vagas disponíveis para o apartamento {apartamento.numero} no subsolo {apartamento.subsolo}")

        # Armazenar informações do sorteio na sessão
        request.session['sorteio_iniciado'] = True
        request.session['horario_conclusao'] = timezone.localtime().strftime("%d/%m/%Y às %Hh %Mmin e %Ss")

        return redirect('sky_view_sorteio')

    else:
        sorteio_iniciado = request.session.get('sorteio_iniciado', False)
        resultados_sorteio = Sorteio.objects.select_related('apartamento', 'vaga').order_by('apartamento__id').all()
        vagas_atribuidas = resultados_sorteio.exists()

        return render(request, 'sky_view/sky_view_sorteio.html', {
            'resultados_sorteio': resultados_sorteio,
            'vagas_atribuidas': vagas_atribuidas,
            'sorteio_iniciado': sorteio_iniciado,
            'horario_conclusao': request.session.get('horario_conclusao', '')
        })



def sky_view_excel(request):
    # Caminho do modelo Excel
    caminho_modelo = 'setup/static/assets/modelos/sorteio_novo.xlsx'

    # Carregar o modelo existente
    wb = load_workbook(caminho_modelo)
    ws = wb.active

    # Ordenar os resultados do sorteio pelo ID do apartamento
    resultados_sorteio = Sorteio.objects.select_related('apartamento', 'vaga').order_by('apartamento__id').all()

    # Pegar o horário de conclusão do sorteio
    horario_conclusao = request.session.get('horario_conclusao', 'Horário não disponível')
    ws['B8'] = f"Sorteio realizado em: {horario_conclusao}"

    # Começar a partir da linha 10 (baseado no layout do seu modelo)
    linha = 10
    for sorteio in resultados_sorteio:
        ws[f'B{linha}'] = sorteio.apartamento.numero  # Número do apartamento
        ws[f'C{linha}'] = sorteio.vaga.numero  # Número da vaga
        ws[f'D{linha}'] = f'Subsolo {sorteio.vaga.subsolo}'  # Subsolo
        ws[f'E{linha}'] = sorteio.vaga.get_tipo_display()  # Tipo da vaga
        ws[f'F{linha}'] = sorteio.vaga.get_especial_display()  # Especialidade da vaga
        linha += 1

    # Configurar a resposta para o download do Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="resultado_sorteio_sky_view.xlsx"'

    # Salvar o arquivo Excel na resposta
    wb.save(response)

    return response



def sky_view_qrcode(request):
    # Obter todos os apartamentos para preencher o dropdown
    apartamentos_disponiveis = Apartamento.objects.all()
    
    # Obter o apartamento selecionado através do filtro (via GET)
    numero_apartamento = request.GET.get('apartamento')
    
    # Inicializar a variável de resultados filtrados como uma lista vazia
    resultados_filtrados = []

    # Se o apartamento foi selecionado, realizar a filtragem dos resultados do sorteio
    if numero_apartamento:
        # Buscar os sorteios para o apartamento selecionado
        sorteios_duplas = SorteioDupla.objects.filter(apartamento__numero=numero_apartamento)

        # Armazenar os resultados filtrados
        resultados_filtrados = sorteios_duplas

    return render(request, 'sky_view/sky_view_qrcode.html', {
        'resultados_filtrados': resultados_filtrados,
        'apartamento_selecionado': numero_apartamento,
        'apartamentos_disponiveis': apartamentos_disponiveis,
    })


def sky_view_zerar(request):
    if request.method == 'POST':
        Sorteio.objects.all().delete()
        SorteioDupla.objects.all().delete()
        return redirect('sky_view_sorteio')
    else:
        return render(request, 'sky_view/sky_view_zerar.html')
    

