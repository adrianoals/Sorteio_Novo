from django.urls import path
from helbor.views import helbor_torre1, helbor_zerar_torre1, helbor_excel_torre1, helbor_qrcode_torre1, helbor_torre2, helbor_zerar_torre2, helbor_excel_torre2, helbor_qrcode_torre2


urlpatterns = [
        path('helbor-torre1',helbor_torre1, name='helbor_torre1'), 
        path('helbor-excel-torre1/', helbor_excel_torre1, name='helbor_excel_torre1'),
        path('helbor-zerar-torre1/', helbor_zerar_torre1, name='helbor_zerar_torre1'),
        path('helbor-qrcode-torre1/', helbor_qrcode_torre1, name='helbor_qrcode_torre1'), 
        path('helbor-torre2',helbor_torre2, name='helbor_torre2'), 
        path('helbor-excel-torre2/', helbor_excel_torre2, name='helbor_excel_torre2'),
        path('helbor-zerar-torre2/', helbor_zerar_torre2, name='helbor_zerar_torre2'),
        path('helbor-qrcode-torre2/', helbor_qrcode_torre2, name='helbor_qrcode_torre2'), 

]

