from django.urls import path
from receitas.views import index, receita, buscar, main, buscar_i, compartilhe_receita, add_ingrediente, add_quantidade

urlpatterns = [
    path('index', index, name='index'),
    path('receita/<int:receita_id>', receita, name='receita'),
    path('buscar', buscar, name='buscar'),
    path('', main, name='main'),
    path('buscar_i', buscar_i, name="buscar_i"),
    path('compartilhe_receita', compartilhe_receita, name="compartilhe_receita"),
    path('add_ingrediente', add_ingrediente, name="add_ingrediente"),
    path('add_quantidade/<int:receita_id>', add_quantidade, name='add_quantidade')
]