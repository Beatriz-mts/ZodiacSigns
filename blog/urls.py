from django.urls import path
from . import views

urlpatterns = [
    path('', views.zodiac_signs_list, name='zodiac_signs_list'),
]
