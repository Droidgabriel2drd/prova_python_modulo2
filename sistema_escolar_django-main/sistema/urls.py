from django.contrib import admin
from django.urls import path
from portal import views

# ERRO: estava faltando o parth do index e cadastro_view
# SOLUÇÃO: apenas colocamos o parth desses itens na linha de código como o index e o cadastro_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('cadastro/', views.cadastro_view, name='cadastro'),

]