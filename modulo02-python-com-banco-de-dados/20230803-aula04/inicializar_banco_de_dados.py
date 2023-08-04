"""
inicializar_banco_de_dados.py

Tabelas do sistema de blog

Nesse projeto iremos utilizar o banco de dados SQLite (versão 3). O Python possui
suporte nativo a esse banco de dados, portanto não precisamos instalar
nenhum conector (biblioteca que é utilizada para se conectar a um banco de dados)
"""

from conexao import conexao

if __name__ == "__main__":
    
    # Criando a tabela tb_usuarios

    sql = """
        CREATE TABLE IF NOT EXISTS tb_usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            senha TEXT NOT NULL
        );
    """

    # Utilizamos o método execute do objeto connection para executar comandos
    # SQL
    conexao.execute(sql)

    # Por padrão, o SQLite não assegura que as regras de relação entre
    # as chaves (primária e estrangeira) serão seguidas. Por exemplo, por padrão
    # o SQLite não verifica se o valor associado a uma chave estrangeira em uma
    # tabela filha existe na tabela pai.
    conexao.execute("PRAGMA foreign_keys = ON")

    # Criando a tabela tb_perfis
    sql = """
    CREATE TABLE IF NOT EXISTS tb_perfis(
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        sobrenome TEXT NOT NULL,
        data_de_nascimento DATETIME NOT NULL,

        FOREIGN KEY(id) REFERENCES tb_usuarios(id)
    );

    """

    conexao.execute(sql)

    # Criar a tabela tb_postagens
    sql = """
    CREATE TABLE IF NOT EXISTS tb_postagens(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        perfil_id INTEGER NOT NULL,
        titulo TEXT NOT NULL,
        texto TEXT NOT NULL,
        data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(perfil_id) REFERENCES tb_perfis(id)
    );

    """

    conexao.execute(sql)

    # Criar a tabela tb_categorias
    sql = """
    CREATE TABLE IF NOT EXISTS tb_categorias(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    );
    """

    conexao.execute(sql)

    # Criar a tabela associativa tb_postagens_categorias
    sql = """
    CREATE TABLE IF NOT EXISTS tb_postagens_categorias(
        id_postagem INTEGER NOT NULL,
        id_categoria INTEGER NOT NULL,

        PRIMARY KEY(id_postagem, id_categoria),

        FOREIGN KEY(id_postagem) REFERENCES tb_postagens(id),
        FOREIGN KEY(id_categoria) REFERENCES tb_categorias(id)
    );

    """

    conexao.execute(sql)