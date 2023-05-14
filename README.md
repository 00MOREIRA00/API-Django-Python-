# API-Django-Python-

## Django e Django Rest

Ambos são escritos em Python, porém com finalidades diferentes. O Django facilita a construção de sites e aplicações web. Enquanto o Django Rest, é um conjunto de ferramentas poderosas para construir web APIS.


## Desenvolvimento

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



