from django.contrib import admin
from portal import models

## Estavam faltando algumas variáveis.
## Inserido as variáveis que estavam faltando.

@admin.register(models.Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'criacao_data', 'telefone', 'registro', 'disciplina', 'ativo', 'observacao', 'imagem',)

@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'telefone', 'matricula', 'criacao_data', 'observacao', 'ativo', 'imagem',)

@admin.register(models.Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno_id', 'professor_id', 'horario', 'observacao', 'status',)
