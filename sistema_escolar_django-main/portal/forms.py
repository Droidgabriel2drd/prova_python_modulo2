from django import forms

from .models import Professor

## O erro é que o models não estava declarado corretamente
## solução: apenas declarei corrtamente o .models

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'sobrenome', 'email', 'criacao_data', 'telefone', 'registro', 'disciplina', 'ativo', 'observacao', 'imagem',]
