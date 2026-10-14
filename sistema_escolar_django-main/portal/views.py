from django.shortcuts import render
from sistema import *
from django.http import HttpResponse

def index(request):
    return render(
        request,
        'templates/portal/index.html'
    )


def cadastro_view (request):
    print('Página cadastro funcionou!')
    return HttpResponse('Página inicial do cadastro de usuário')

# ERRO: Cadastro não estava apropriadamente inserido como função no código na view nem como uma variavel funcionando
# SOLUÇÃO: Colocar o cadastro_view em uma pagina no view, url e init
