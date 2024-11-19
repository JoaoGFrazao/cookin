from django.shortcuts import render, get_object_or_404, redirect
from receitas.models import Receitas, Ingrediente, ReceitaIngrediente
from django.contrib import messages
from receitas.forms import CompartilheForms, IngredienteForms
from django.contrib.auth.models import User

#Para criar a view do Index e enviar os dados do BD ao HTML
def index(request):
    receitas = Receitas.objects.all()
    return render(request, 'receitas/index.html', {"cards": receitas})

def receita(request, receita_id):
    if not request.user.is_authenticated:
         messages.error(request, "Faça login para ver as receitas")
         return redirect('login')

    receitas = get_object_or_404(Receitas, pk=receita_id)

    if receitas.usuario == None or receitas.usuario == "":
         return render(request, 'receitas/recipe.html', {"info" : receitas})
    
    ingredientes_com_quantidades = ReceitaIngrediente.objects.filter(receita=receitas)
    user_id = receitas.usuario_id
    usuario = get_object_or_404(User, id=user_id)


    return render(request, 'receitas/recipe.html', {"info" : receitas, 'usuario': usuario, 'ingredientes_com_quantidade': ingredientes_com_quantidades})

def buscar(request):
        
     if not request.user.is_authenticated:
          messages.error(request, "Faça login para pesquisar receitas")
          return redirect('login')
     
     receitas = Receitas.objects.all()
     if "buscar" in request.GET:
          nome_a_buscar = request.GET['buscar']
          if nome_a_buscar:
               receitas = receitas.filter(nome__icontains = nome_a_buscar)
        
     return render(request, "receitas/index.html", {"cards": receitas})

def main(request):
     return render(request, 'receitas/main.html')

def buscar_i(request):
     if not request.user.is_authenticated:
          messages.error(request, "Faça login para buscar receitas por ingredientes")
          return redirect('login')



     if request.method == 'POST':
        #Pegando os dados enviados pelo formulário e transformando numa lista, depois transformando o número em inteiros e por ultimo em um set para a comparação
        ingredientes_selecionados = request.POST.getlist('ingredientes')   
        ingredientes_selecionados = list(map(int, ingredientes_selecionados))
        ingredientes_selecionados_set = set(ingredientes_selecionados)

        receitas = Receitas.objects.all()

        # Filtrar receitas que têm todos os seus ingredientes dentro dos ingredientes selecionados
        receitas_filtradas = []

        for receita in receitas:
             receitas_set = set(receita.ingredientes.values_list('id', flat=True))
             print(receitas_set)
             if receitas_set <= ingredientes_selecionados_set:
                  receitas_filtradas.append(receita)

        print(f'Receitas filtradas: {[receita.nome for receita in receitas_filtradas]}')

        
        return render(request, 'receitas/index.html', {'cards': receitas_filtradas})
     
     ingredientes = Ingrediente.objects.all().order_by("nome")
     return render(request, "receitas/ingredientes.html", {"options": ingredientes})
    
def compartilhe_receita(request):
    form = CompartilheForms()

    if not request.user.is_authenticated:
        messages.error(request, "Faça login para compartilhar uma receita")
        return redirect('login')

    if request.user.is_superuser:
        messages.error(request, "Superusuários não podem cadastrar receitas")
        return redirect('index')

    if request.method == 'POST':
        form = CompartilheForms(request.POST, request.FILES)

        if form.is_valid():
          receita = Receitas.objects.create(
               nome=form.cleaned_data['nome_receita'].title(),
               preparo=form.cleaned_data['preparo'].capitalize(),
               foto=form.cleaned_data['foto'],
               usuario=request.user
            )
          ingredeintes_selecionados = form.cleaned_data['ingredientes']
          receita.ingredientes.set(ingredeintes_selecionados)

          receita_id = receita.id
          messages.success(request, "Receita adicionada com sucesso")
          return redirect('add_quantidade', receita_id = receita_id)

    return render(request, 'receitas/compartilhe_receita.html', {
        'form': form,
    })

def add_ingrediente(request):

     if request.method == 'POST':
          form = IngredienteForms(request.POST)
          if form.is_valid():
               ingrediente_novo = form['nome'].value().capitalize()
               ingredientes_existentes = Ingrediente.objects.all()

               for ingrediente in ingredientes_existentes:
                    if ingrediente.nome == ingrediente_novo:
                         messages.error(request, "Ingrediente já estava cadastrado"),
                         return redirect('add_ingrediente')

               Ingrediente(nome = ingrediente_novo).save()
               messages.success(request, "Ingrediente adicionado com sucesso")
               return redirect ('add_ingrediente')


     form = IngredienteForms()
     return render(request, "receitas/add_ingrediente.html", {"form": form})

def add_quantidade(request, receita_id):
     if request.method == 'POST':
          ingredientes = ReceitaIngrediente.objects.filter(receita_id=receita_id).select_related('ingrediente')

          for ingrediente_receita in ingredientes:
               ingrediente_id = ingrediente_receita.ingrediente.id
               quantidade = request.POST.get(f'quantidade_{ingrediente_id}')

               if quantidade:
                    ingrediente_receita.quantidade = quantidade
                    ingrediente_receita.save()
          return redirect('index')

     ingredientes = ReceitaIngrediente.objects.all().filter(receita_id = receita_id).select_related('ingrediente')
     receita_id = receita_id
     return render (request, 'receitas/quantidades.html', {'ingredientes': ingredientes, 'receita_id': receita_id})