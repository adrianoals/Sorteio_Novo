from django.urls import path
from sorteio_novo.views import inicio_sorteio, presenca, filtrar_presenca, tipo_sorteio, apartamento, sorteio_ausentes

urlpatterns = [
        path('inicio_sorteio', inicio_sorteio, name='inicio_sorteio'), 
        path('presenca/', presenca, name='presenca'),
        path('filtrar-presenca/', filtrar_presenca, name='filtrar_presenca'),
        path('tipo-sorteio/', tipo_sorteio, name='tipo_sorteio'),
        path('apartamento/', apartamento, name='apartamento'),
        path('sorteio-ausentes/', sorteio_ausentes, name='sorteio_ausentes'),
]