# models.py

from datetime import datetime

# Classe Base que nossas models irão herdar
from database import Base

# Importação dos tipos de dados das colunas
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text


# Todas as classes que quisermos que sejam models, devem OBRIGATORIAMENTE herdar da classe Base
class User(Base):
    
    # O valor de __tablename__ será usado para definir o nome da tabela no banco de dados
    __tablename__ = "tb_users"

    # Criamos o campo id, do tipo inteiro, chave primária e auto incremento
    # id INT PRIMARY KEY AUTO_INCREMENT
    id = Column(Integer, primary_key=True, autoincrement=True)

    # Criamos o campo email, do tipo string e tamanho máximo 100.
    # nullable=True significa que o campo não pode receber valores nulos
    # email VARCHAR(100) NOT NULL
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)


class Profile(Base):

    __tablename__ = "tb_profiles"

    id = Column(Integer, ForeignKey("tb_users.id"), primary_key=True)

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)


class Post(Base):

    __tablename__ = "tb_posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    profile_id = Column(Integer, ForeignKey("tb_profiles.id"), nullable=False)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
