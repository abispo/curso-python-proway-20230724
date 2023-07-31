"""
Escrevendo arquivos .csv no Python

Utilizamos o módulo csv, que vem na biblioteca padrão do Python, para escrever
arquivos .csv (comma separated values | Valores separados por vírgula).

Podemos escrever arquivos .csv no Python de 2 maneiras: Utilizando csv.writer ou
csv.DictWriter

"""

import csv

from random import randint
from uuid import uuid4

if __name__ == "__main__":

    # Utilizamos o argumento newline="" para evitar que seja criada uma linha
    # vazia entre as linhas de dados
    with open("clientes.csv", "w", encoding="utf-8", newline="") as arquivo:
        

        csv_writer = csv.writer(arquivo, delimiter=';')

        # O método writer escreve uma nova linha no arquivo
        # Esse método recebe uma lista
        csv_writer.writerow(["nome", "idade", "saldo"])

        csv_writer.writerow(["Bárbara", "31", "1000"])

        lista_clientes = (
            ("José", "40", "1200",),
            ("Maria", "23", "1795",),
            ("João", "33", "1900",)
        )

        # writerows escreve várias linhas de uma vez só
        # no arquivo
        csv_writer.writerows(lista_clientes)

    
    with open("acessos.csv", "w", encoding="utf-8", newline="") as arquivo:
        
        fieldnames = ["id", "usuario_id", "timestamp"]

        # O argumento fieldnames recebe a lista de valores que servirão como
        # cabeçalhos do arquivo
        csv_dict_writer = csv.DictWriter(arquivo, fieldnames=fieldnames, delimiter=';')

        # O método writeheader() escreve na primeira linha os valores
        # passados em fieldnames
        csv_dict_writer.writeheader()

        # O método writerow escreve uma linha. Devemos passar um dicionário
        csv_dict_writer.writerow({
            "id": str(uuid4()),
            "usuario_id": str(randint(10, 1000)),
            "timestamp": str(randint(20230701, 20230731))
        })
