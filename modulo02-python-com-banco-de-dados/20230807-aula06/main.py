# main.py

from database import engine, Base
from messages import MAIN_MENU, USER_INFO
from models import User, Profile, Post
from users import list_users, create_user, get_profile_by_id


if __name__ == "__main__":

    Base.metadata.create_all(engine)

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
                        profile = get_profile_by_id(user.id)
                        print(USER_INFO.format(
                            user.id, profile.first_name, profile.last_name, user.email
                        ))

            case 3:
                pass
            case 4:
                pass