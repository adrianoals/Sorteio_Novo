from django.urls import path
# from max_club.views import max_club, zerar, excel_max_club, filtro_apartamento
from max_club.views import max_club

urlpatterns = [
        path('max-club', max_club, name='max_club'), 
        # path('excel-max-club/', excel_max_club, name='excel_max_club'),
        # path('max-club-zerar/', zerar, name='zerar'),
        # path('max-club-qrcode/', filtro_apartamento, name='filtro_apartamento')
        
]