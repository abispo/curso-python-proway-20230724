# usuarios.py

from conexao import conexao


def criar_usuario(email, senha, nome, sobrenome, data_nascimento):

    """
    Quando utilizamos comandos SQL para manipulação dos dados das tabelas (SELECT, INSERT, UPDATE, DELETE),
    precisamos criar um objetivo cursor, que fará essas operações
    """
    cur = conexao.cursor()

    sql = """
        INSERT INTO tb_usuarios(email, senha) VALUES (?, ?);
    """

    # Em comandos DML (SELECT, INSERT, UPDATE, DELETE), precisamos executar o SQL utilizando o cursor
    cur.execute(sql, (email, senha,))

    # O comando anterior ainda não salva os dados na tabela, pois internamente a transação não
    # foi confirmada. Para salvarmos as transações pendentes, precisamos chamar o método commit()
    # do objeto Connection
    conexao.commit()