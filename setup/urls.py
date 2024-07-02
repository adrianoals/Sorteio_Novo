from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('sorteio_novo.urls')), 
    path('', include('assincon.urls')), 
    path('', include('porcelana.urls')), 
    path('', include('lyon.urls')), 
    path('', include('helbor.urls')), 
    path('', include('nova_guarulhos.urls')), 
    path('', include('max_club.urls')), 

]



