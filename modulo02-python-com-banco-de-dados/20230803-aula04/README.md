# Python com banco de dados

## Projeto Blog

### Regras
* Um usuário deverá ter os seguintes dados salvos:
    * id
    * email
    * senha

* Um usuário também deve ter dados de perfil, que serão os seguintes
    * id
    * nome
    * sobrenome
    * data de nascimento

* Um usuário deve ter apenas 1 perfil associado a ele, e vice-versa.

* Toda postagem é feita por 1 usuário (e um usuário pode fazer diversas postagens), e ela deve ter os seguintes campos:
    * id
    * perfil_id
    * titulo
    * texto
    * data_hora

* Teremos também uma tabela para categorias, que serão atreladas às postagens.
    * id
    * nome

* Por fim, vamos associar as categorias as postagens, e vice versa


## Conectando em um banco de dados SQL utilizando Python
* Utilizando o pacote `sqlite3`.
* Criando uma conexão com a base de dados (método `connect()`).
* Executando comandos com `execute()`
* Criando um cursor para retorno dos dados
    * Método fetchone()
    * Método fetchmany(num)
    * Método fetchall()

## Tipos de relacionamentos entre tabelas
* Um Para Um (1:1)
* Um Para Muitos (1:N)
* Muitos Para Muitos (N:N)
