# API-Django-Python-

## Django e Django Rest

Ambos são escritos em Python, porém com finalidades diferentes. O Django facilita a construção de sites e aplicações web. Enquanto o Django Rest, é um conjunto de ferramentas poderosas para construir web APIS.


## Configurando

1° Inicialmente criamos um ambinte para manter todas as dependencias do desenvolvimento dentro.

Criamos a famosa Virtual Env, que nada mais seria que um ambinete virtual leve, onde cada um possui seu proprio pacote com conjuntos de dependencias.
```
pyton -m venv ./venv
```

2º Depois precisamos ativar nosso ambinete virtual que foi criado.

```
sintae: nome_da_virtualenv/Scripts/Activate

venv/Scripts/Activate
```

> Lembrando que o modo de ativar a .venv é diferente para cada tipo de ambinete de desenvolvimento, seja ela Linu xou Windows.

3° Baixamos todas as dependencias necessarias para o desenvolvimento.

```
pip install --upgrade pip

pip install Django
```

> Observação: Podemos dar um pip freeze para identificar quais são as dependecias para o projeto, e assim garantir que o Django foi instalado.


4º Criamos o projeto
```
django-admin startproject config .
```

> Usamos esse projeto para cria nosso projeto em si, porem como uma boa pratica nós criamos o projeto com o nome "config" e adicionamos o "." no final para garantir que dentro dessa pasta não seja criada mais nenhuma subpasta. Fazemos isso pois o Django admin é responsavel por todas as configurações da nossa aplicação

Após esses passos a estrutura de pastas deve ficar nesse formato. Deve conter nossa virtuual machine, nosso projeto com a config e nosso arquivo manager.s
<div align="center"><img src="./imagens/arquivosiniciais.png" style="border: 3px solid gray"></div>

5° Iniciando o servidor
```
python manage.py runservers
```


------------------------

## Desenvolvendo com Django

> Podemos modificar a linguagem e o time zone nas configs do projeto.

> Automaticamente o Django tem um banco configurado para si mesmo.

1° Após fazer toda nossa configuração e ligar nosso servidor, é necessário que criemos um projeto e estartemos ele.

```
python manage.py startapp "nome_projeto"

python manage.py startapp escola
```

> Precisamos estar com o ambiente virtual ligado para fazermos isso.

<div align="center"><img src="./imagens/projeto.png" style="border: 3px solid gray"></div>

2° Criar modelo de aluno e migra-lo para o banco de dados. Então vamos até o script "models" quue achamos no nosso projeto escola e criamos um script.

```
class Aluno(models.Model) :
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)

    def __str__(self) -> str:
        return self.nome

Nela especificamos que nosso modelo espera receber nome e rg, cada uma com sua especificação, e irá identificar-los pelo nome.
```

3° Após criar o modelo, é necessário que exportemos essa informação para o banco de dados criado pelo Django. Para fazer isso temos que ir até o arquivo "conf" que temos e incluir o nome do projeto no "INSTALLED_APPS", e após iniciarmos a migração com o código:
```
//Copdigo para identificar migração
python manage.py makemigrations

//Código para fazer a migração
python manage.py migrate
```

> Caso não venhamos a fazer essa modificação, ao rodar o código, não será encontrado migração para fazer.

<br/> 

4° Após fazermos isso, podemos utiliza-lo e fazer cadastros, até mesmo para que possamos testar se está tudo certo. Então podemos ir até o admin.py do projeto escola.

Ao me encontrar no arquivo podemos começar:
```
// Importamos o modelo que criamos
from escola.models import Aluno

//Criamos uma class para as informações
class Alunos(admin.ModelAdmin): 
        //O que será retornado
    list_display = ('id', 'nome', 'rg')
        //O que pode ser modificado pelo usuário
    list_display_links = ('id', 'nome')
        //O que pode ser usado como metodo de busca
    search_fields = ('nome')
```

<div align="center"><img src="./imagens/Login.png" style="border: 3px solid gray"></div>

<br/> 
Ao tentar acessar essas informações, nós vemos que é solicitado um login que não foi configurado, então temos que configurar.
```
python manage.py createsuperuser
```

Dessa forma teremos acesso a interface grafica de configuração do Django. Porém ainda não temos acesso as configurações de "Alunso" pois ainda não configuramos no admin.py

```
admin.site.register(Aluno, Alunos)
```

Ao acessar podemos através da interface grafica podemos adicionar usuário, editar, excluir.

<br/>

## Desenvolvendo com Django Rest Framework

1º Instalando o Djando Rest Framework no projeto
```
pip install djangorestframework

//Para verificar as dependencias
pip freeze
```

Após a instalação devemos adicionar o framework nas configurações como algo que foi instalado. Assim como foi feito ao criar o projeto escola.

2° O objetivo ao utilizar esse é framework é boder disponibilizar todas essas informações que foram criadas para serem consumidas como normalmente as APIs, porem elas são utilizadas usando o JSON, dessa forma utilizamos o "Serializer" para fazer essa convrersão, então criamos um arquivo "serializer.py" dentro do projeto escola.

Dentro dele criaremos uma class de conversão, e dentro dessa class de conversão iremos criar uma class "Meta" para indicar o modelo que iremos utilizar, e qual os campos que serão utilizados.

```
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        Filds = ['id', 'nome', 'rg']

No campo Fields temos somente os campos que queremos retornar, caso tenhamos campos que não queremos, é somente necessário não passar-lo no Fields.
```

3º Devemos dar um jeito de maninular qual o Sereliazador e o Model, que está sendo usado. Para isso usamos o "Controler", porem no Django chamado de "View".

Vamos até o script "views.py" e criamos a seguinte class:
```
from rest_framework import viewsets
from escola.models import Aluno
from escola.serializer import AlunoSerializer

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        Filds = ['id', 'nome', 'rg']

-Importante importar o Serealizardor usado para conversão

-Importante importar o model usado para uso dos dados
```

<br/>

4° Criaremos nossas URLs / Rotas. Para isso iremos no "urls.py" do projeto global e criaremos nosso script.

```
# Adicionamos a funcionalidade de incluir informações
from django.urls import path, include
# Importamos nosso View que criamos
from escola.views import AlunosViewSet
# Importamos a funcionalidade de Rotas que o framework disponibiliza
from rest_framework import routes

# Adicionamos um router principal
router = routers.DefaultRouter()
router.register(r'alunos', AlunosViewSet)

Adicionamos paths de consulta
urlpatterns = [
    path('admin/', admin.site.urls),
    # Ao buscar sem nenhum adicional, ou seja a url pura, teremos como retorno nossa url
    path('', include(router.urls)),
]
```

Com essa url em questão podemos consumir essa API, criando, deletando, modificando e buscando o conteúdo.

