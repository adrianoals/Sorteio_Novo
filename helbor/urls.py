from django.urls import path
from helbor.views import helbor_torre1, helbor_zerar_torre1, helbor_excel_torre1, helbor_qrcode_torre1


urlpatterns = [
        path('helbor-torre1',helbor_torre1, name='helbor_torre1'), 
        path('helbor-excel-torre1/', helbor_excel_torre1, name='helbor_excel_torre1'),
        path('helbor-zerar-torre1/', helbor_zerar_torre1, name='helbor_zerar_torre1'),
        path('helbor-qrcode-torre1/', helbor_qrcode_torre1, name='helbor_qrcode_torre1'), 

]

