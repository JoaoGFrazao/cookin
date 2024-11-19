import re
from django import forms
from django.core.exceptions import ValidationError

class CadastroForms(forms.Form):
    primeiro_nome = forms.CharField(
        label = "Primeiro Nome",
        required = True,
        max_length = 30,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "João"
            }
        )
    )

    sobrenome = forms.CharField(
        label="sobrenome",
        required=True,
        max_length= 30,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Silva"
            }
        )
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=70,
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "joao.silva@dominio.com"
            }
        )
    )

    senha_1 = forms.CharField(
        label="Senha",
        required = True,
        max_length = 20,
        widget = forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

    senha_2 = forms.CharField(
        label="Confirme sua Senha",
        required = True,
        max_length = 20,
        widget = forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )

    def clean_primeiro_nome(self):
        primeiro_nome = self.cleaned_data.get("primeiro_nome")

        if not re.match(r'^[A-Za-zÀ-ÿ\s]+$', primeiro_nome):
            raise ValidationError('O nome deve conter apenas letras e espaços.')
        else:
            return primeiro_nome
        
    def clean_sobrenome(self):
        sobrenome = self.cleaned_data.get("sobrenome")

        if not re.match(r'^[A-Za-zÀ-ÿ\s]+$', sobrenome):
            raise ValidationError('O nome deve conter apenas letras e espaços.')
        else:
            return sobrenome

    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get("senha_1")
        senha_2 = self.cleaned_data.get("senha_2")

        if senha_1 != senha_2:
            raise ValidationError("As senhas não coincidem")
        else:
            return senha_2

class LoginForms(forms.Form):
        email = forms.EmailField(
        label="Email",
        required=True,
        max_length=70,
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "digite seu email"
            }
        )
    )
        senha = forms.CharField(
        label="Senha",
        required = True,
        max_length = 20,
        widget = forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )