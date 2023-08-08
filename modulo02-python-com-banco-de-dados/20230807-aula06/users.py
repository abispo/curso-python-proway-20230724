from database import session
from models import User, Profile


def list_users():
    return session.query(User).all()

def create_user(email, password, first_name, last_name):

    # Instanciamos a model User passando os valores que a função recebeu
    user = User(email=email, password=password)

    # Adicionamos a instância de User no objeto session. Nesse momento
    # o registro ainda não foi salvo na tabela
    session.add(user)

    # O commit confirma a transação e salva os dados na tabela fisicamente
    session.commit()

    # Chamamos a função para criação de perfil
    create_profile(user, first_name, last_name)

    # Retornamos o objeto salvo na tabela
    return user

def create_profile(user, first_name, last_name):

    profile = Profile(id=user.id, first_name=first_name, last_name=last_name)

    session.add(profile)

    session.commit()

    return profile


def get_profile_by_id(id):
    
    profile = session.query(Profile).get(id)

    return profile