from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('sorteio_novo.urls')), 
    path('', include('assincon.urls')), 
    path('', include('porcelana.urls')), 
    path('', include('lyon.urls')), 
]



