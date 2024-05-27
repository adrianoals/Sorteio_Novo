from django.urls import path
from nova_guarulhos.views import ng_aleatorio, ng_excel, ng_zerar, ng_qrcode, ng_inicio, ng_presenca, ng_filtrar, ng_apartamento, ng_pcd, ng_adimplentes, ng_final

urlpatterns = [
        path('ng-aleatorio', ng_aleatorio, name='ng_aleatorio'), 
        path('ng-excel/', ng_excel, name='ng_excel'),
        path('ng-zerar/', ng_zerar, name='ng_zerar'),
        path('ng-qrcode/', ng_qrcode, name='ng_qrcode'), 
        path('ng-inicio/', ng_inicio, name='ng_inicio'), 
        path('ng-presenca/', ng_presenca, name='ng_presenca'), 
        path('ng-filtrar/', ng_filtrar, name='ng_filtrar'), 
        path('ng-apartamento/', ng_apartamento, name='ng_apartamento'), 
        path('ng-pcd/', ng_pcd, name='ng_pcd'), 
        path('ng-adimplentes/', ng_adimplentes, name='ng_adimplentes'),
        path('ng_final/', ng_final, name='ng_final'), 
]

