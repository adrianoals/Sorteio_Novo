from django.urls import path
from sorteio_novo_institucional.views import home, solucoes, orcamento

urlpatterns = [
        path('', home, name='home'), 
        path('solucoes', solucoes, name='solucoes'), 
        path('orcamento', orcamento, name='orcamento'), 
]


