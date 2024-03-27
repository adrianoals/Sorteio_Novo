from django.urls import path
from assincon.views import assincon_sorteio

urlpatterns = [
        path('assincon', assincon_sorteio, name='assincon_sorteio'), 
]