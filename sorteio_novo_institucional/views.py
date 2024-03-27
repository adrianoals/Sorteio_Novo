from django.shortcuts import render, redirect
from sorteio_novo_institucional.forms import ContatoForm
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.
def home(request):
    	return render(request, 'sorteio_novo_institucional/home.html')

def solucoes(request):
    	return render(request, 'sorteio_novo_institucional/solucoes.html')

# def orcamento(request):
#     	return render(request, 'sorteio_novo_institucional/orcamento.html')

def orcamento(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            # Processar o formulário
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            # Enviar e-mails para você
            send_mail(
                 f'Novo Contato - {assunto}',
                 f'Nome: {nome}\nEmail: {email}\n\nMensagem:\n{mensagem}','adrianotesteapp@gmail.com',  # E-mail remetente
                 ['dri.limasantos@gmail.com'], # E-mail destinatario  
                 fail_silently=False,
                 )

            # Adicionar mensagem de sucesso
            messages.success(request, '*Mensagem enviada com sucesso!')

            # Redirecionar para a mesma página após o POST bem-sucedido
            return redirect('orcamento')

    else:
        form = ContatoForm()

    return render(request, 'sorteio_novo_institucional/orcamento.html', {'form': form})

