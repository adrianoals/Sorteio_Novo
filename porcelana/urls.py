from django.urls import path
from porcelana.views import porcelana_aleatorio, excel_porcelana, zerar_porcelana, qrcode_porcelana, porcelana_inicio, porcelana_presenca, porcelana_filtrar, porcelana_s_apartamento, porcelana_sorteio, porcelana_final

urlpatterns = [
        path('porcelana-aleatorio', porcelana_aleatorio, name='porcelana_aleatorio'), 
        path('porcelana-excel/', excel_porcelana, name='excel_porcelana'),
        path('porcelana-zerar/', zerar_porcelana, name='zerar_porcelana'),
        path('porcelana-qrcode/', qrcode_porcelana, name='qrcode_porcelana'), 
        path('porcelana-inicio/', porcelana_inicio, name='porcelana_inicio'), 
        path('porcelana-presenca/', porcelana_presenca, name='porcelana_presenca'), 
        path('porcelana-filtrar/', porcelana_filtrar, name='porcelana_filtrar'), 
        path('porcelana-s-apartamento/', porcelana_s_apartamento, name='porcelana_s_apartamento'), 
        path('porcelana_sorteio/', porcelana_sorteio, name='porcelana_sorteio'), 
        path('porcelana_final/', porcelana_final, name='porcelana_final'), 
        
]

