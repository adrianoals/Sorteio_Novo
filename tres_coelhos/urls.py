from django.urls import path
from tres_coelhos.views import tres_coelhos_sorteio, tres_coelhos_excel, tres_coelhos_qrcode

urlpatterns = [
        # path('tres-coelhos', index, name='index'), 
        # Rota para iniciar o sorteio
        path('tres-coelhos-sorteio/', tres_coelhos_sorteio, name='tres_coelhos_sorteio'), 
         # Rota para exportar os resultados do sorteio para um arquivo Excel
        path('sorteio/excel/', tres_coelhos_excel, name='tres_coelhos_excel'),
        # Rota para gerar o QR Code do sorteio
        path('sorteio/qrcode/', tres_coelhos_qrcode, name='tres_coelhos_qrcode'),
]

