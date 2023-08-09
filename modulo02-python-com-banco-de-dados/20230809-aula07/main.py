# main.py

from database import engine, Base
from messages import MAIN_MENU, USER_INFO
from models import User, Profile, Post
from users import list_users, create_user, update_user


if __name__ == "__main__":

    while True:

        print(MAIN_MENU)

        opcao = int(input("Informe a opção desejada: "))

        match opcao:
            case 0:
                print("Encerrando...")
                break
            case 1:
                
                email = input("Informe o seu e-mail: ")
                password = input("Informe uma senha: ")
                first_name = input("Informe o seu primeiro nome: ")
                last_name = input("Informe o seu sobrenome: ")

                user = create_user(email, password, first_name, last_name)

                print(f"Usuário {user.email} criado com sucesso!")

            case 2:
                users = list_users()

                if len(users) == 0:
                    print("Não existem usuários cadastrados.")

                else:
                    for user in users:
                        print(USER_INFO.format(
                            user.id, user.profile.first_name, user.profile.last_name, user.email
                        ))

            case 3:
                id = int(input("Informe o ID do usuário a ser modificado: "))
                first_name = input("Informe um novo valor para nome: ").strip()
                last_name = input("Informe um novo valor para o sobrenome: ").strip()
                email = input("Informe um novo valor para o email: ").strip()
                password = input("Informe um novo valor para a senha: ").strip()

                user = update_user(id, email, password, first_name, last_name)

                print(f"Usuário {user.email} atualizado com sucesso!")

            case 4:
                pass