"""
Módulo principal

"""

from mensagens import INFO_USUARIO
from usuarios import criar_usuario, buscar_usuarios

if __name__ == "__main__":

    texto = """
ESCOLHA UMA DAS OPÇÕES ABAIXO
-----------------------------

0 - SAIR
1 - CADASTRAR USUARIO
2 - VISUALIZAR USUARIOS
3 - ATUALIZAR DADOS DE USUÁRIO
4 - REMOVER USUÁRIO

"""

    print(texto)
    
    while True:
        
        opcao = int(input("INFORME A OPÇÃO ESCOLHIDA: "))

        match opcao:
            case 0:
                print("SAINDO...")
                break

            case 1:
                email = input("INFORME O SEU E-MAIL: ")
                senha = input("INFORME A SUA SENHA: ")
                nome = input("INFORME O SEU PRIMEIRO NOME: ")
                sobrenome = input("INFORME O SEU SOBRENOME: ")
                data_nasc = input("INFORME A SUA DATA DE NASCIMENTO NO FORMATO dd/mm/yyyy: ")

                criar_usuario(email, senha, nome, sobrenome, data_nasc)

            case 2:
                texto = "Informe a quantidade de registros (0 para todos, 1 para 1 ou maior do que 1 para mais): "

                quantidade = int(input(texto))

                usuarios = buscar_usuarios(quantidade)

                for usuario in usuarios:
                    
                    # O format aceita uma quantidade arbitrária de argumentos,
                    # desde que essa quantidade seja igual as marcações '{}' na
                    # string. Podemos utilizar a sintaxe de asterisco para
                    # "desempacotar" os valores da tupla no método format, ou seja,
                    # vamos passar todos os valores da tupla no método por posição.
                    # format(1, "joão", "da silva", etc...)
                    
                    print(INFO_USUARIO.format(*usuario))

            case 3:
                print("IMPLEMENTAR")

            case 4:
                print("IMPLEMENTAR")

            case _:
                print("OPÇÃO DESCONHECIDA")
