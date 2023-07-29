"""
Manipulação de arquivos txt no Python

Manipulação significa abrir, alterar e criar arquivos
utilizando o python.
"""

if __name__ == "__main__":
    
    # Para abrir arquivos (qualquer tipo) no python, utilizamos a função
    # built-in open()

    # open(nome_do_arquivo, modo_de_abertura)
    # Por padrão, abrimos o arquivo no modo somente-leitura (r)
    arquivo = open("clientes.txt")

    # read() Lê o conteúdo do arquivo e retorna como string
    conteudo = arquivo.read()
    print(conteudo)

    # .close() fecha o arquivo (ou seja, fecha a conexão do objeto com o arquivo)
    arquivo.close()

    # No modo somente leitura, se tentarmos abrir um arquivo que não existe, é
    # gerada uma exceção. A linha abaixo irá causar erro
    # open("erro.txt", "r")
    arquivo = open("clientes.txt", "rt", newline="", encoding="utf-8")

    # Depois que abrimos o arquivo, além do método read(), podemos utilizar as
    # seguintes maneiras pra ler o conteúdo do arquivo:

    # Método readline()
    # Esse método lê uma linha do arquivo, ou seja, lê os caracteres até encontrar
    # o '\n'
    print(arquivo.readline())
    print(arquivo.readline())   # Lê a próxima linha

    # O método readline() tem um argumento opcional size, que representa a
    # quantidade de caracteres que queremos ler na linha
    print(arquivo.readline(10))

    # Método readlines(limite)
    # Esse método lê cada linha do arquivo e armazena como um item de uma lista
    conteudo = arquivo.readlines(86)
    print(conteudo)

    # Lemos todas as linhas do arquivo e retornamos como itens
    # de uma lista
    conteudo = arquivo.readlines()
    print(conteudo)

    # Por fim, conseguimos ler o conteúdo de um arquivo utilizando
    # um laço for
    for linha in arquivo:
        print(linha)

    # O comando acima não irá mostrar nada, pois o cursor do arquivo atingiu
    # o fim. Internamente, o python define um cursor no arquivo que irá ler o
    # conteúdo. Quando abrimos um arquivo em modo somente leitura, esse cursor
    # está na posição 0. Utilizamos o método tell() para saber a posição que o
    # cursor se encontra
    print(f"Posição atual do cursor: {arquivo.tell()}.")

    # Se quisermos ler novamente o conteúdo do arquivo desde o seu
    # início, precisamos "rebobinar" o cursor, ou seja, enviar ele pra posição
    # desejada, que nesse caso é a posição 0. Utilizamos o método seek() pra
    # fazer isso
    arquivo.seek(0)

    # Conferindo se a posição realmente mudou
    print(f"Posição atual do cursor: {arquivo.tell()}.")

    for linha in arquivo:
        print(linha, end="")
