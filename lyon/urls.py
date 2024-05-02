from django.urls import path
from lyon.views import lyon, lyon_excel, lyon_zerar, lyon_qrcode, lyon_moto, lyon_moto_excel, lyon_moto_zerar, lyon_moto_qrcode

urlpatterns = [
        path('lyon', lyon, name='lyon'),
        path('lyon-excel/', lyon_excel, name='lyon_excel'),
        path('lyon-zerar/', lyon_zerar, name='lyon_zerar'),
        path('lyon-qrcode/', lyon_qrcode, name='lyon_qrcode'),
        path('lyon-moto', lyon_moto, name='lyon_moto'),
        path('lyon-moto-excel/', lyon_moto_excel, name='lyon_moto_excel'),
        path('lyon-moto-zerar/', lyon_moto_zerar, name='lyon_moto_zerar'),
        path('lyon-moto-qrcode/', lyon_moto_qrcode, name='lyon_moto_qrcode'),
]