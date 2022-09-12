from django.shortcuts import render, get_object_or_404

from .forms import FormularioCadastro
from .models import Contato


# Create your views here.

def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html',
                  {'contatos': contatos})


def amigos(request):
    contatos = Contato.objects.all().filter(categoria = '3')
    return render(request, 'contatos/index.html',
                  {'contatos': contatos})

# TODO> criar função filtro amigos

def familia(request):
    contatos = Contato.objects.all().filter(categoria='1')
    return render(request, 'contatos/index.html',
                  {'contatos': contatos})
    pass

# TODO> criar função filtro amigos

def empresa(request):
    contatos = Contato.objects.all().filter(categoria='2')
    return render(request, 'contatos/index.html',
                  {'contatos': contatos})
    pass

# TODO> criar função filtro amigos


def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })


def cadastrar_contato(request):
    form = FormularioCadastro()
    return render(request, 'contatos/form.html', {'form': form})


