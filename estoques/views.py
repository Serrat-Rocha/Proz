from django.shortcuts import render, get_object_or_404
from .models import Estoque
from .forms import EstoqueForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

def landing_page(request):
    return render(request, 'estoques/login.html')

@login_required
def index(request):
    produtos = Estoque.objects.all()
    return render(request, 'estoques/index.html', {'produtos': produtos})


@login_required
def novo_produto(request):
    if request.method == 'POST':
        produto = request.POST.get('produto')
        quantidade = request.POST.get('quantidade_disponivel')
        valor = request.POST.get('valor_unitario')

        # Pegue os campos extras, se estiver usando
        categoria = request.POST.get('categoria')
        validade = request.POST.get('validade')
        raridade = request.POST.get('raridade')

        Estoque.objects.create(
            produto=produto,
            quantidade_disponivel=quantidade,
            valor_unitario=valor,
            categoria=categoria,
            validade=validade,
            raridade=raridade
        )

        return HttpResponseRedirect('index')  # Certifique-se de que 'index' lista os produtos
    return render(request, 'estoques/novo_produto.html')


@login_required
def deletar_produto(request, produto_id):
    produto = get_object_or_404(Estoque, id=produto_id)
    produto.delete()
    return HttpResponseRedirect(reverse('index'))

@login_required
def editar_produto(request, produto_id):
    produto = get_object_or_404(Estoque, id=produto_id)
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = EstoqueForm(instance=produto)

    return render(request, 'estoques/editar_produto.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('landing'))

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticate_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse('index'))
    context = {'form': form}
    return render(request, 'estoques/registrar.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'estoques/fazer_login.html', {'error': 'Credenciais inválidas.'})
    return render(request, 'estoques/fazer_login.html')