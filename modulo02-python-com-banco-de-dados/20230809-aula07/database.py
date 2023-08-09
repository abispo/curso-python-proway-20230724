# database.py

# create_engine é a função utilizada para criar uma conexão com o banco de dados
from sqlalchemy import create_engine

# A partir da função declarative_base criamos a classe base para todas as nossas models
from sqlalchemy.ext.declarative import declarative_base

# sessionmaker cria a sessão de acesso ao banco de dados. Podemos ter várias sessões abertas
from sqlalchemy.orm import sessionmaker

# String de conexão ao banco de dados
# Aqui é onde definimos o tipo de banco, as credenciais de acesso, servidor, etc...
connection_string = "sqlite:///db.sqlite3"

# A função create_engine retorna um objeto que representa a conexão com o banco de dados
# (semelhando ao conexao.connect())
# O primeiro argumento é a connection_string, e o segundo argumento (echo=True) vai mostrar no
# terminal os comandos SQL enviados para o banco
engine = create_engine(connection_string, echo=True)

# Base vai receber a instância da classe base para criarmos as nossas models.
# Ou seja, toda classe que criarmos vai herdar dessa classe Base
Base = declarative_base()

# sessionmaker retorna um tipo de dados sessão. Uma sessão deve ser aberta se quisermos nos
# comunicar com o banco de dados. Cada sessão deve estar ligada (bind) a uma conexão de banco de
# dados. Podemos ter várias sessões apontando para outros bancos de dados ao mesmo tempo
# session recebe a instância do tipo sessão
Session = sessionmaker(bind=engine)
session = Session()