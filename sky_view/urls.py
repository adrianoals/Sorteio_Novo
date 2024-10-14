from django.urls import path
from sky_view.views import sky_view_sorteio, sky_view_excel, sky_view_qrcode, sky_view_dupla, sky_view_dupla_excel, sky_view_zerar, sky_view_resultado

urlpatterns = [
        # Rota para iniciar o sorteio
        path('sky_view-sorteio/', sky_view_sorteio, name='sky_view_sorteio'), 
        # Rota para exportar os resultados do sorteio para um arquivo Excel
        path('sorteio/excel/', sky_view_excel, name='sky_view_excel'),

        # Rota para gerar o QR Code do sorteio
        path('sky_view-qrcode', sky_view_qrcode, name='sky_view_qrcode'),
        
        # Rota para zerar o sorteio
        path('sky_view-zerar/', sky_view_zerar, name='sky_view_zerar'),

        # Rota para o resultado
        path('sky_view-resultado/', sky_view_resultado, name='sky_view_resultado'),

]

