# Programação WEB com Python e Django

## Instalação do Django
* De preferência, utilizaremos a biblioteca `pipenv` para criar os virtualenvs que serão usados no desenvolvimento do projeto
* Abra um terminal e digite os seguintes comandos:
    * `pip install pipenv` para instalar o pipenv no sistema.
    * Após isso, crie uma pasta para o projeto, entre nessa parte pelo terminal e digite o comando `pipenv install django`;
    * O comando anterior irá criar o virtualenv, o arquivo `Pipfile` com as dependências e irá instalar o `Django` nesse virtualenv.
    * Após isso, vamos criar o projeto em `Django` com o seguinte comando: `django-admin startproject <nome_do_projeto> .`. Substitua `<nome_do_projeto>` pelo nome que desejar. O `.` no final significa que o diretório raiz do projeto será o diretório atual.
    * Para rodar o projeto Django, estando no diretório raiz do projeto (mesmo diretório onde se encontra o arquivo `manage.py`), digite o comando `python manage.py runserver`. Nas configurações padrão, acessando pelo navegador o endereço `http://127.0.0.1:8000` você terá acesso à página de instalação inicial do Django.
    * Para criar um pacote no django, estando no diretório raiz do projeto (mesmo diretório onde se encontra o arquivo `manage.py`), digite o comando `python manage.py startapp <nome_do_pacote>`, substituindo `<nome_do_pacote>` pelo nome que desejar.