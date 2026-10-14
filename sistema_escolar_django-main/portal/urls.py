from django.urls import path
from portal import views

#ERRO: o path de cadastro não estava colocado certamente na url
#SOLUÇÃO: Apenas corrigimos colocando o path de cadastro.


urlpatterns = [
    path('index/', views.index),
    path('cadastro/', views.cadastro_view),
]
