PreRegistro

User

Unidade
    Os tipos de unidades são os seguintes:
        - Apartamento, Casa, Chalé, Cabana, etc...

Reserva
    - A reserva vai associar:
        - O usuário que fez a reserva
        - Qual unidade foi reservada
        - Período da reserva
            - Entrada e saida

* Criar o pacote 'unidades'
    * Nesse pacote unidades, vamos criar 2 models
        * A model Unidade
            nome    string
            tipo    (chave estrangeira para TipoUnidade)
            disponivel (boolean)
            preco       float
            descricao   string

        * A model TipoUnidade
            nome
            descricao
            * Uma Unidade pode ser apenas de 1 Tipo
            * Um tipo pode aparecer em várias Unidades
    
    1) Criar o pacote unidades
        python manage.py startapp unidades
    2) Registrar o pacote unidades
        Adicionar o nome à lista INSTALLED_APPS no arquivo settings.py
    3) Criar as models
        São criadas no arquivo models.py
    4) Gerar os arquivos de migration
        python manage.py makemigrations
    5) Aplicar as migrations
        python manage.py migrate
    6) Registrar no admin
        As models são registradas no arquivo admin.py

========================================================================

1) Criar o pacote reservas
    python manage.py startapp reservas
2) Registrar o pacote reservas
    Adicionar o nome à lista INSTALLED_APPS no arquivo settings.py
3) Criar as models
    São criadas no arquivo models.py
4) Gerar os arquivos de migration
    python manage.py makemigrations
5) Aplicar as migrations
    python manage.py migrate
6) Registrar no admin
    As models são registradas no arquivo admin.py

A model Reserva terá a seguinte estrutura:
    usuario = Usuário que fez a reserva
        Foreign Key para a model User (django.contrib.auth.models User)
    unidade = Unidade que foi reservada
        Foreign Key para a model Unidade (unidades.models Unidade)
    inicio_da_reserva = Campo data/hora indicando o período inicial da reserva
        (DateTime)
    fim_da_reserva = Campo data/hora indicando o período final da reserva
        (DateTime)
    observacoes = text
        CharField ou TextField