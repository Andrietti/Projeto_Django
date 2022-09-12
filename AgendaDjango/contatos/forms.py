from django import forms
from .models import *

class FormularioCadastro(forms.ModelForm):
    class Meta:
        model = Contato
        field = [
            'nome', 'sobrenome', 'telefone', 'email', 'data_nascimento',
            'descricao', 'categoria', 'mostrar'
        ]


class Contato(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=30)
    email = models.EmailField()
    data_nascimento = models.DateField()
    data_cadastro = models.DateTimeField(default = timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)