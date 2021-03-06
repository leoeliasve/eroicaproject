from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('grabado/<nombre>/', views.grabar, name="grabar"),
    path('prueba/', views.vistaprueba, name='verprueba'),
]