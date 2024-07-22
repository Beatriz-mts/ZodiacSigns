from django.urls import path
from . import views

urlpatterns = [
    path('', views.zodiac_sign_list, name='zodiac_sign_list'),
    path('zodiac_sign/<pk>/', views.get_zodiac_sign, name='get_zodiac_sign'),
    path("create_new_famous_person/", views.create_new_famous_person, name="create_new_famous_person"),
    path("get_famous_person/<pk>/", views.get_famous_person, name="get_famous_person"),
    path("delete_famous_person/<pk>/", views.delete_famous_person, name="delete_famous_person"),
    path("update_famous_person/<pk>/", views.update_famous_person, name="update_famous_person"),
]
