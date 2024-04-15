from django.urls import path
from porcelana.views import porcelana_aleatorio, excel_porcelana, zerar_porcelana, qrcode_porcelana

urlpatterns = [
        path('porcelana-aleatorio', porcelana_aleatorio, name='porcelana_aleatorio'), 
        path('porcelana-excel/', excel_porcelana, name='excel_porcelana'),
        path('porcelana-zerar/', zerar_porcelana, name='zerar_porcelana'),
        path('porcelana-qrcode/', qrcode_porcelana, name='qrcode_porcelana')
        
]