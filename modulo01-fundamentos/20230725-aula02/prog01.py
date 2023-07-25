
if __name__ == "__main__":
    
    # if/elif/else
    # Estrutura de controle de condição
    # Se uma condição é verdadeira, executa o bloco de código
    # Se não, passa para a próxima comparação ou sai

    usuario = input("Informe o seu usuário: ")

    if usuario == "user":
        print("Usuário padrão do sistema")

    elif usuario == "redator":
        print("Usuário redator. Pode criar postagens")

    elif usuario == "moderador":
        print("Usuário moderador. Pode moderar o conteúdo")

    elif usuario == "admin":
        print("Usuário administrador. Gerencia outros usuários")

    else:
        print("Usuário desconhecido. Sem informações.")

    # match case
    # Mais indicado para comparações simples

    match usuario:
        case "user":
            print("Usuário padrão do sistema")

        case "redator":
            print("Usuário redator. Pode criar postagens")

        case "moderador":
            print("Usuário moderador. Pode moderar o conteúdo")

        case "admin":
            print("Usuário administrador. Gerencia outros usuários")

        # Caso padrão. Se nenhuma das comparações anteriores
        # for verdadeira, executa o bloco abaixo
        case _:
            print("Usuário desconhecido. Sem informações.")