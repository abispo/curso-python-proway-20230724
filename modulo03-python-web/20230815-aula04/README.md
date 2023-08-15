# Criar um módulo de estatísticas

* Criar o pacote estatisticas
    * No terminal, digitar o comando python manage.py startapp estatisticas

* Dentro do pacote estatisticas, criar o arquivo urls.py

* A rota desse pacote será /statistics
* No arquivo views do pacote estatisticas, criar a funçao index
    * Essa função index irá renderizar um template (statistics.html) com 2 informações:
        * A quantidade de perguntas cadastradas
        * A quantidade de opções cadastradas
    * Essas informações serão trazidas do banco de dados

* No arquivo urls.py do pacote estatisticas, criar a rota que será associada a essa função index

* Na página index do pacote polls, criar um link que levará o usuário a página de estatísticas