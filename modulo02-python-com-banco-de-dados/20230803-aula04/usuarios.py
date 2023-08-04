# usuarios.py

from datetime import datetime

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
    command_info = cur.execute(sql, (email, senha,))

    # O comando anterior ainda não salva os dados na tabela, pois internamente a transação não
    # foi confirmada. Para salvarmos as transações pendentes, precisamos chamar o método commit()
    # do objeto Connection
    conexao.commit()

    criar_perfil_usuario(command_info.lastrowid, nome, sobrenome, data_nascimento)


def criar_perfil_usuario(usuario_id, nome, sobrenome, data_de_nascimento):
    cur = conexao.cursor()

    sql = """
        INSERT INTO tb_perfis(id, nome, sobrenome, data_de_nascimento)
        VALUES (?, ?, ?, ?);
    """

    # Aqui estamos convertendo a string no formato de dia/mês/ano para um objeto
    # datetime do Python
    data_de_nascimento = datetime.strptime(data_de_nascimento, "%d/%m/%Y")

    cur.execute(sql, (usuario_id, nome, sobrenome, data_de_nascimento,))

    conexao.commit()


def buscar_usuarios(quantidade):

    sql = """
    SELECT tu.id, tp.nome, tp.sobrenome, tu.email, tp.data_de_nascimento
    FROM tb_usuarios tu
    INNER JOIN tb_perfis tp
    ON tu.id = tp.id;
    """

    cur = conexao.cursor()

    consulta = cur.execute(sql)

    match quantidade:
        case 0:
            return consulta.fetchall()
        
        case 1:
            return consulta.fetchone()
        
        case 2:
            return consulta.fetchmany(quantidade)
        
        case _:
            return consulta.fetchall()