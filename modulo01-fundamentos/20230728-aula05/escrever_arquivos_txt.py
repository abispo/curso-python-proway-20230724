# escrever_arquivos_txt.py

"""
Manipulação de arquivos txt no Python

Manipulação significa abrir, alterar e criar arquivos
utilizando o python.
"""

# Módulo para manipulação de data/hora em Python
from datetime import datetime

if __name__ == "__main__":
    
    # Podemos alterar o conteúdo de arquivos em python de 2 maneiras:
    # Utilizando o modo de abertura w (Write)
    # Nesse modo, se o arquivo não existe, ele será criado. Se já existir, o seu
    # conteúdo será sobrescrito

    arquivo = open("registros.txt", "w", encoding="utf-8")

    # Podemos utilizar o método write() para escrever no arquivo
    # datetime.now() retorna a data/hora atuais
    # \n é o caractere especial que representa uma quebra de linha
    arquivo.write(f"Registrando ponto {datetime.now()}\n")

    # Ou então, o método writelines() para escrever mais de 1 linha por vez
    linhas = ["Primeiro registro\n", "segundo registro\n", "terceiro registro\n"]
    arquivo.writelines(linhas)

    # Lembrando sempre de fechar o arquivo
    arquivo.close()

    # Além do modo escrita, podemos abrir o arquivo no modo a (append)
    # Nesse modo, se o que arquivo não existir, ele é criado. Se existir, o conteúdo
    # escrito é salvo no final do arquivo

    arquivo = open("registros.txt", "a", encoding="utf-8")

    data_hora = datetime.now()

    # o método strftime formata a maneira que visualizamos a data
    # No caso abaixo, visualizamos como dd/mm/yyyy hh:mm:ss
    arquivo.write(f"Último registro: {data_hora.strftime('%d/%m/%Y %H:%M:%S')}.")

    arquivo.close()
