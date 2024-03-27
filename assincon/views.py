from django.shortcuts import render
from .models import ListaSindicos, Sorteio
from django.contrib import messages
import random

def assincon_sorteio(request):
    sindicos_disponiveis = ListaSindicos.objects.exclude(id__in=Sorteio.objects.filter(sorteado=True).values_list('sindico_id', flat=True))
    sorteio_finalizado = False
    sindico_selecionado = None  # Vai guardar o objeto do síndico selecionado

    if request.method == 'POST':
        if sindicos_disponiveis:
            sindico_selecionado = random.choice(sindicos_disponiveis)
            Sorteio.objects.create(sindico=sindico_selecionado, sorteado=True)
        else:
            sorteio_finalizado = True
            messages.info(request, 'Todos os síndicos já foram sorteados.')
    
    return render(request, 'assincon/assincon_sorteio.html', {
        "sorteio_finalizado": sorteio_finalizado,
        "sindico_selecionado": sindico_selecionado,  # Passando o objeto para o template
        "sindicos_disponiveis": sindicos_disponiveis
    })
