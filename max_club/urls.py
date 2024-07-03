from django.urls import path
from max_club.views import max_club, max_club_zerar, max_club_excel, max_club_qrcode, max_club_bike, max_club_bike_zerar, max_club_bike_excel, max_club_bike_qrcode

urlpatterns = [
        path('max-club', max_club, name='max_club'), 
        path('max-club-zerar/', max_club_zerar, name='max_club_zerar'),
        path('max-club-bike', max_club_bike, name='max_club_bike'), 
        path('max-club-bike-zerar', max_club_bike_zerar, name='max_club_bike_zerar'), 
        path('max-club-excel/', max_club_excel, name='max_club_excel'),
        path('max-club-bike-excel/', max_club_bike_excel, name='max_club_bike_excel'),
        path('max-club-qrcode/', max_club_qrcode, name='max_club_qrcode'), 
        path('max-club-bike-qrcode/', max_club_bike_qrcode, name='max_club_bike_qrcode')
        
]