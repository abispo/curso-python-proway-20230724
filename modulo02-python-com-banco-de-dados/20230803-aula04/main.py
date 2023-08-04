"""
Módulo principal

"""

from usuarios import criar_usuario

if __name__ == "__main__":

    texto = """
ESCOLHA UMA DAS OPÇÕES ABAIXO
-----------------------------

0 - SAIR
1 - CADASTRAR USUARIO
2 - VISUALIZAR USUARIOS

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
                pass