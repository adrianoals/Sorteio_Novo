from django.urls import path
from tres_coelhos.views import tres_coelhos_sorteio, tres_coelhos_excel, tres_coelhos_qrcode, tres_coelhos_dupla, tres_coelhos_dupla_excel, tres_coelhos_zerar

urlpatterns = [
        # Rota para iniciar o sorteio
        path('tres-coelhos-sorteio/', tres_coelhos_sorteio, name='tres_coelhos_sorteio'), 
        # Rota para exportar os resultados do sorteio para um arquivo Excel
        path('sorteio/excel/', tres_coelhos_excel, name='tres_coelhos_excel'),

        # Rota para gerar o QR Code do sorteio
        path('tres-coelhos-qrcode', tres_coelhos_qrcode, name='tres_coelhos_qrcode'),
        
        # Rota para iniciar o sorteio dupla
        path('tres-coelhos-dupla/', tres_coelhos_dupla, name='tres_coelhos_dupla'), 
        # Rota para exportar os resultados do sorteio para um arquivo Excel
        path('sorteio/dupla/excel/', tres_coelhos_dupla_excel, name='tres_coelhos_dupla_excel'),
        
        # Rota para zerar o sorteio
        path('tres-coelhos-zerar/', tres_coelhos_zerar, name='tres_coelhos_zerar')

]

