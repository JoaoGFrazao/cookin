from django.contrib import admin
from receitas.models import Ingrediente, Receitas, ReceitaIngrediente

class ReceitaIngredienteInline(admin.TabularInline):
    model = ReceitaIngrediente
    extra = 1  # Número de formulários extras


class ListarReceitas(admin.ModelAdmin):
    list_display = ("id", 'nome')
    search_fields = ('nome', )
    inlines = [ReceitaIngredienteInline]

class ListarIngrediente(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome', )


admin.site.register(Receitas, ListarReceitas)
admin.site.register(Ingrediente, ListarIngrediente)


# Register your models here.
