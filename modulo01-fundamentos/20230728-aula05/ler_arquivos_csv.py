"""
Lendo arquivos .csv no Python

Utilizamos o módulo csv, que vem na biblioteca padrão do Python, para ler
arquivos .csv (comma separated values | Valores separados por vírgula).

Podemos ler arquivos .csv no Python de 2 maneiras: Utilizando csv.reader ou
csv.DictReader

"""

import csv

if __name__ == "__main__":
    
    """
    with é uma palavra reservada do python que serve para criação e gerenciamento
    de contexto de execução.

    A vantagem desse método é que não precisamos fechar o arquivo que abrimos
    explícitamente, ou seja, não precisamos digitar arquivo.close() no final
    da execução, pois ele é fechado de forma automática quando o contexto é
    encerrado

    """
    with open(file="notas.csv", mode="r", encoding="utf-8") as arquivo:
        
        # Como os valores do arquivo são separados por ponto-e-vírgula, precisamos
        # especificar na hora da leitura, passando valor para o parâmetro
        csv_reader = csv.reader(arquivo, delimiter=';')

        """
        Quando utilizamos csv.reader, as linhas são retornadas como listas,
        e cada valor separado pelo ponto-e-vírgula é mostrado como um elemento
        dessa lista

        Desafio! Mostrar a média aritmética de cada aluno, ignorando a maior e a
        menor nota.
        """
        for linha in csv_reader:
            print(linha)


    with open("cursos.csv", "r", encoding="utf-8") as arquivo:

        csv_dict_reader = csv.DictReader(arquivo, delimiter=';')

        """
        No caso do DictReader, a cada iteração no objeto DictReader, é retornado
        um dicionário. As chaves desse dicionário serão os itens que estão
        na primeira linha do arquivo, que o Python considera sendo os nomes das
        colunas. As linhas a partir daí são consideradas os valores associados
        a essas chaves

        Desafio: Ler o arquivo CSV e formatar a saida da seguinte maneira:
        Curso: <nome_do_curso>
        Data de início: <data_inicio:dd/mm/yyyy>
        Carga horário: <carga_horaria>
        Preço: <preço>

        """
        for linha in csv_dict_reader:
            print(linha)
