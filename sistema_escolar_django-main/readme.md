# portal/ # app principal

# models.py # Professor, Aluno, Aula ← 2 erros (2 Erro corrigido)
## ERRO: O erro é que não foi colocado o import do timezone, então o django não reconhece a função timezone.now e com isso acontece o erro.
## CORREÇÃO: A correção foi simplesmente darpython manage.py runserver import timezone

## ERRO: o matriculo estava charfield
## CORREÇÃO: apenas colocamos para integerfield
=========================================================================================
# views.py # views HTTP ← 1 erro (1 Erro Corrigido)
# ERRO: Cadastro não estava apropriadamente inserido como função no código na view nem como uma variavel funcionando
# SOLUÇÃO: Colocar o cadastro_view em uma pagina no view, url e init
=========================================================================================
# forms.py # formulários ← 1 erro (1 Erro corrigido??)
## O erro é que o models não estava declarado corretamente
## solução: apenas declarei corrtamente o .models
=========================================================================================
# admin.py # painel admin ← 1 erro (1 Erro corrigido)
## Estavam faltando algumas variáveis.
## Inserido as variáveis que estavam faltando.
=========================================================================================
# urls.py # rotas do app ← 1 erro (1 Erro corrigido)
## ERRO: o path de cadastro não estava colocado certamente na url
## SOLUÇÃO: Apenas corrigimos colocando o path de cadastro.
=========================================================================================
=========================================================================================
# sistema/ # configurações do projeto
# urls.py # rotas globais ← 1 erro (1 erro corrigido)
## ERRO: estava faltando o parth do index e cadastro_view
## SOLUÇÃO: apenas colocamos o parth desses itens na linha de código como o index e o cadastro_view
=========================================================================================
# settings.py # configurações ← 1 erro (1 Erro corrigido)
## ERRO: o erro estava que o portal e o sistema não estavam mencionado no INSTALLED_APPS.
## CORREÇÃO: apenas adicionei eles no INSTALLED_APPS.
=========================================================================================
# Grupo: Thiago Costa Bantel, Gabriel Henrique, George Soares

