from django.urls import path
from . import views

urlpatterns = [
    path('', views.zodiac_sign_list, name='zodiac_sign_list'),
    path('zodiac-signs/', views.zodiac_sign_list, name='zodiac_sign_list'),
    path('aries/', views.aries_list, name='aries_list'),
    path('taurus/', views.taurus_list, name='taurus_list'),
    path('gemini/', views.gemini_list, name='gemini_list'),
    path('cancer/', views.cancer_list, name='cancer_list'),
    path('leo/', views.leo_list, name='leo_list'),
    path('virgo/', views.virgo_list, name='virgo_list'),
    path('libra/', views.libra_list, name='libra_list'),
    path('scorpio/', views.scorpio_list, name='scorpio_list'),
    path('sagittarius/', views.sagittarius_list, name='sagittarius_list'),
    path('capricorn/', views.capricorn_list, name='capricorn_list'),
    path('aquarius/', views.aquarius_list, name='aquarius_list'),
    path('pisces/', views.pisces_list, name='pisces_list'),
]
