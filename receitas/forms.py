from django import forms
from .models import Ingrediente, Receitas

class IngredienteForms(forms.Form):
    nome = forms.CharField(
        label="Ingrediente",
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs= {
                "class": "form-control",
                "placeholder": "Digite seu ingrediente",
            }
        )
    )


class CompartilheForms(forms.Form):
    nome_receita = forms.CharField(
        label="Nome da Receita",
        required=True,
        max_length=100,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nome da sua receita"
            } 
        )
    )

    preparo = forms.CharField(
        label="Modo de Preparo",
        required= True,
        max_length= 800,
        widget= forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Digite aqui o modo de preparo da sua receita"
            }
        )
    )


    foto = forms.ImageField(
        label="Adicione uma foto da sua receita",
        required=True,
        widget=forms.ClearableFileInput(
            attrs ={
                "class": "form-control-file"
            }
        )
    )

    ingredientes = forms.ModelMultipleChoiceField(
        queryset=Ingrediente.objects.all().order_by('nome'),  
        widget=forms.CheckboxSelectMultiple,
        label="Selecione os ingredientes"
    )
