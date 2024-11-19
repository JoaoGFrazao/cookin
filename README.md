# Cookin'

<p>O Cookin' é uma aplicação que permite usuários cadastrados visualizarem, cadastrarem e filtrarem um banco de dados de receitas culinárias. É possível filtrar as receitas fazendo uma busca por nome ou por ingredientes. </p>

<h2>Quickstart</h2>

Para iniciar o projeto localmente é preciso ter o Python3 instalado em seu computador, a versão utilizada foi `Python 3.12.2`. Além disso siga os passos abaixo.

- Baixe ou clone esse repositório para seu computador e navegue até ele no terminal

- Execute o comando a seguir: ` python venv_script.py`

- Ative o ambiente virtual com ` venv/Scripts/Activate` no Windows ou `source venv/bin/activate` no Linux ou Mac

- Em seguida faça as migrações para criar o banco de dados executando `python manage.py makemigrations` e em seguida `python manage.py migrate`

  

<h2>Modelos do Banco de Dados</h2>

## 1. **Ingrediente**

O modelo `Ingrediente` armazena informações sobre os ingredientes disponíveis no sistema.

- Campos:
  - `nome` (`CharField`): Nome do ingrediente. É obrigatório e tem no máximo 100 caracteres.
- Método:
  - `__str__`: Retorna o nome do ingrediente para facilitar a leitura.

Exemplo de uso:

```
python


Copiar código
Ingrediente(nome="Farinha de Trigo")
```

------

## 2. **Receitas**

O modelo `Receitas` armazena informações sobre receitas cadastradas pelos usuários.

- **Campos**:
  - `nome` (`CharField`): Nome da receita. É obrigatório e tem no máximo 200 caracteres.
  - `ingredientes` (`ManyToManyField`): Relacionamento muitos-para-muitos com o modelo `Ingrediente`, gerenciado através do modelo intermediário `ReceitaIngrediente`.
  - `preparo` (`TextField`): Descrição do modo de preparo da receita.
  - `foto` (`ImageField`): Foto opcional da receita, salva no diretório `fotos/%Y/%m/%d/` (ano/mês/dia).
  - `usuario` (`ForeignKey`): Relacionamento com o modelo `User` do Django, indicando o autor da receita. Se o usuário for excluído, o valor é definido como `NULL`.
- **Método**:
  - `__str__`: Retorna o nome da receita para facilitar a leitura.

Exemplo de uso:

```
Receitas(nome="Bolo de Cenoura", preparo="Misture todos os ingredientes e asse por 30 minutos.")
```

------

## 3. **ReceitaIngrediente**

Este é o modelo intermediário para gerenciar a relação entre `Receitas` e `Ingrediente`. Ele adiciona um campo extra para especificar a quantidade de cada ingrediente em uma receita.

- **Campos**:
  - `receita` (`ForeignKey`): Referência à receita associada.
  - `ingrediente` (`ForeignKey`): Referência ao ingrediente associado.
  - `quantidade` (`CharField`): Quantidade do ingrediente usada na receita. É obrigatório e tem no máximo 40 caracteres.
- **Método**:
  - `__str__`: Retorna uma string descrevendo a quantidade do ingrediente usado em uma receita.

Exemplo de uso:

```
ReceitaIngrediente(receita=bolo_de_cenoura, ingrediente=farinha, quantidade="2 xícaras")
```

------

## Resumo dos Relacionamentos

- **`Receitas` e `Ingrediente`**: Relacionamento muitos-para-muitos através do modelo intermediário `ReceitaIngrediente`.
- **`Receitas` e `User`**: Relacionamento um-para-muitos, onde cada receita pertence a um usuário.

------

## Exemplo de Funcionalidade

1. **Cadastrar um Ingrediente**:

   ```
   python
   
   
   Copiar código
   Ingrediente.objects.create(nome="Açúcar")
   ```

2. **Cadastrar uma Receita**:

   ```
   pythonCopiar códigousuario = User.objects.get(username="usuario_exemplo")
   receita = Receitas.objects.create(
       nome="Pudim",
       preparo="Misture tudo e leve ao forno.",
       usuario=usuario
   )
   ```

3. **Adicionar Ingredientes à Receita**:

   ```
   códigopudim = Receitas.objects.get(nome="Pudim")
   leite_condensado = Ingrediente.objects.get(nome="Leite Condensado")
   ReceitaIngrediente.objects.create(receita=pudim, ingrediente=leite_conden
   ```