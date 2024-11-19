from django.db import models
from django.contrib.auth.models import User

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nome
    
class Receitas(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    ingredientes = models.ManyToManyField('Ingrediente', through='ReceitaIngrediente')
    preparo = models.TextField()
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="receitas",
    )

    def __str__(self):
        return self.nome


class ReceitaIngrediente(models.Model):
    receita = models.ForeignKey(Receitas, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    quantidade = models.CharField(max_length=40, null=False, blank=False)

    def __str__(self):
        return f"{self.quantidade} de {self.ingrediente} em {self.receita}"
