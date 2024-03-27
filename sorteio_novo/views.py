from django.shortcuts import render, redirect
from sorteio_novo.models import ListaDePresenca
import random
from django.contrib import messages

def inicio_sorteio(request):
    	return render(request, 'sorteio_novo/inicio_sorteio.html')

def presenca(request):
    if request.method == 'POST':
        lista_de_presenca = ListaDePresenca.objects.all()
        for item in lista_de_presenca:
            item.presenca = request.POST.get('presenca' + str(item.id)) == 'True'
            item.save()
        return redirect('filtrar_presenca')  # Redireciona para a rota 'filtrar_presenca'
    lista_de_presenca = ListaDePresenca.objects.all()
    return render(request, 'sorteio_novo/presenca.html', {"lista_de_presenca": lista_de_presenca})

def filtrar_presenca(request):
    lista_de_presenca = ListaDePresenca.objects.none()  # Inicia com uma queryset vazia
    if request.method == 'POST':
        lista_de_presenca = ListaDePresenca.objects.all()  # Recupera todos os objetos quando o formulário é submetido
        if 'presentes' in request.POST:
            lista_de_presenca = lista_de_presenca.filter(presenca=True)
        if 'ausentes' in request.POST:
            lista_de_presenca = lista_de_presenca.filter(presenca=False)
    return render(request, 'sorteio_novo/filtrar_presenca.html', {"lista_de_presenca": lista_de_presenca})

def tipo_sorteio(request):
    return render(request, 'sorteio_novo/tipo_sorteio.html')

def apartamento(request):
    item_de_presenca = None
    vagas_atribuidas = ListaDePresenca.objects.exclude(vaga__isnull=True).values_list('vaga', flat=True)
    vagas_disponiveis = [vaga for vaga, _ in ListaDePresenca.VAGA_CHOICES if vaga not in vagas_atribuidas]
    apartamentos_disponiveis = ListaDePresenca.objects.filter(presenca=True, vaga__isnull=True)
    sorteio_finalizado = not apartamentos_disponiveis.exists()  # Sorteio finalizado quando todos os apartamentos com presenca=True têm vagas preenchidas

    if request.method == 'POST':
        if 'vaga_selecionada' in request.POST:  # Confirmação de vaga
            vaga_selecionada = request.POST['vaga_selecionada']
            apartamento_id = request.POST['apartamento_id']
            item_de_presenca = ListaDePresenca.objects.get(id=apartamento_id)
            item_de_presenca.vaga = vaga_selecionada
            item_de_presenca.save()
            messages.success(request, 'Vaga selecionada com sucesso!')
            item_de_presenca = None  # Limpa o apartamento selecionado
            vagas_atribuidas = ListaDePresenca.objects.exclude(vaga__isnull=True).values_list('vaga', flat=True)
            vagas_disponiveis = [vaga for vaga, _ in ListaDePresenca.VAGA_CHOICES if vaga not in vagas_atribuidas]
            sorteio_finalizado = not apartamentos_disponiveis.exists()  # Atualiza o estado do sorteio
        elif apartamentos_disponiveis:  # Sorteio
            item_de_presenca = random.choice(apartamentos_disponiveis)

    return render(request, 'sorteio_novo/apartamento.html', {"sorteio_finalizado": sorteio_finalizado, "item_de_presenca": item_de_presenca, "vagas_disponiveis": vagas_disponiveis, "apartamentos_disponiveis": apartamentos_disponiveis})

# def sorteio_ausentes(request):
#     vagas_atribuidas = ListaDePresenca.objects.exclude(vaga__isnull=True).values_list('vaga', flat=True)
#     vagas_disponiveis = [vaga for vaga, _ in ListaDePresenca.VAGA_CHOICES if vaga not in vagas_atribuidas]
#     apartamentos_ausentes = ListaDePresenca.objects.filter(presenca=False, vaga__isnull=True)

#     if vagas_disponiveis and apartamentos_ausentes:
#         apartamento_sorteado = random.choice(apartamentos_ausentes)
#         vaga_sorteada = random.choice(vagas_disponiveis)
#         apartamento_sorteado.vaga = vaga_sorteada
#         apartamento_sorteado.save()
#         messages.success(request, f'Vaga {vaga_sorteada} atribuída ao {apartamento_sorteado.apartamento}!')

#     return render(request, 'sorteio_novo/sorteio_ausentes.html', {"apartamentos_ausentes": apartamentos_ausentes, "vagas_disponiveis": vagas_disponiveis})


def sorteio_ausentes(request):
    sorteio_concluido = False
    ausentes_com_vagas = []

    if request.method == 'POST' and 'sortear' in request.POST:
        # Lógica para sortear os ausentes e atribuir vagas
        ausentes = ListaDePresenca.objects.filter(presenca=False, vaga__isnull=True)
        vagas_atribuidas = ListaDePresenca.objects.exclude(vaga__isnull=True).values_list('vaga', flat=True)

        for ausente in ausentes:
            # Escolha aleatória de vaga, garantindo que não seja repetida
            vagas_disponiveis = [vaga for vaga, _ in ListaDePresenca.VAGA_CHOICES if vaga not in vagas_atribuidas]
            if vagas_disponiveis:
                vaga_escolhida = random.choice(vagas_disponiveis)
                ausente.vaga = vaga_escolhida
                ausente.save()
                vagas_atribuidas.append(vaga_escolhida)
                ausentes_com_vagas.append(ausente)

        sorteio_concluido = True

    return render(request, 'sorteio_novo/sorteio_ausentes.html', {
        'sorteio_concluido': sorteio_concluido,
        'ausentes_com_vagas': ausentes_com_vagas
    })