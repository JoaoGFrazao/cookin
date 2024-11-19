from django.shortcuts import render, redirect, get_object_or_404
from usuarios.forms import CadastroForms, LoginForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def cadastro(request):
    if request.user.is_authenticated:
        messages.error(request, f"Você já está logado como {request.user.first_name} {request.user.last_name}. Para cadastrar-se faça logout primeiro ")
        return redirect('index')
    
    form = CadastroForms()

    if request.method == "POST":
        form = CadastroForms(request.POST)
        if form.is_valid():
            primeiro_nome = form["primeiro_nome"].value().title()
            sobrenome = form["sobrenome"].value().title()
            email = form["email"].value()
            senha = form["senha_1"].value()

            if User.objects.filter(username=email).exists():
                messages.error (request, "Já existe uma conta com esse email")
                return redirect("cadastro")

            User.objects.create_user(
                first_name = primeiro_nome,
                last_name = sobrenome,
                username = email,
                email = email,
                password = senha
            )
            messages.success(request, "Usuário criado com sucesso!")
            return redirect('login')


    return render(request, 'usuarios/cadastro.html', {"form" : form})

def login(request):
    if request.user.is_authenticated:
        messages.error(request, f"Você já está logado como {request.user.first_name} {request.user.last_name}. Para logar com outra conta faça logout primeiro ")
        return redirect('index')

    form = LoginForms()

    if request.method == "POST":
        form = LoginForms(request.POST)

        if form.is_valid():
            email = form["email"].value()
            senha = form["senha"].value()

        usuario = auth.authenticate(
            request,
            username = email,
            password = senha
        )

        nome = get_object_or_404(User, username = email).first_name

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f"{nome} logado(a) com sucesso!")
            return redirect('index')


    return render (request, 'usuarios/login.html', {"form" : form})


def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso")
    return redirect("login")


# Create your views here.
