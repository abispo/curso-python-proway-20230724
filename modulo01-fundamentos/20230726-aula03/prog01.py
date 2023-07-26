"""
Estruturas de dados em Python

Lista

Uma lista é um dos tipos de estruturas de dados em Python. Ela se caracteriza por
ser ordenada, mutável e que permite valores duplicados.

"""

if __name__ == "__main__":

    # Listas podem ser criadas de 2 maneiras
    lista = []              # Podemos criar uma lista vazia
    lista = [1, 2]          # Maneira mais comum
    print(lista)

    lista = list("Python")  # Não é muito comum
    print(lista)

    # Acessando os itens de uma lista

    # Podemos acessar diretamente um item em uma lista informando o seu índice.
    # Em Python, o índice das listas sempre inicia pelo valor 0

    lista = ["Python", "C#", "Java", "Javascript", "Golang", "SQL"]
    #           0       1       2          3           4       5
    # Índices também podem ser negativos
    #           -6      -5     -4         -3          -2       -1

    # Acessandro o terceiro item da lista (Java)
    print(lista[2])

    # Acessando o segundo item a partir do final da lista
    print(lista[-2])

    # Podemos também pegar um intervalo de itens de uma lista, utilizando a 
    # técnica de "slicing" (fatiamento)

    # Sintaxe: [start:stop:step]
    # start (opcional): Índice de início inclusivo
    # stop (opcional): Índice final exclusivo
    # step (opcional): De quantos em quantos itens serão extraídos

    # Exemplo: Extrair os itens C#, Java e Javascript da lista
    print(lista[1:4])

    # Remoção de itens de uma lista
    # Podemos remover itens de uma lista de 4 maneiras

    # método remove(): Remove um item de uma lista pelo seu valor
    # Caso exista mais de um item com o mesmo valor, apenas o primeiro da
    # esquerda para a direita é removido
    # Removendo o item "Java" da lista
    lista.remove("Java")
    print(lista)

    # Método pop(indice): Remove um item de uma lista pelo seu índice. Além de
    # remover, esse método retorna o item removido
    # Removendo o segundo item da lista
    print(f"O item {lista.pop(1)} foi removido!")
    print(lista)

    # Podemos remover utilizando o comando del
    # Removendo o último item da lista
    del lista[-1]
    print(lista)

    # Método clear(): Remove todos os itens de uma lista
    lista.clear()
    print(lista)
    
    # Adicionando itens a uma lista
    # Podemos utilizar 2 métodos para adicionar itens a uma lista

    # append()
    lista.append("Python")
    print(lista)

    # extend(sequencia)
    # Extende a lista com os itens da sequência (lista, tupla, etc)
    # lista = lista + ("C#", "Javascript", "SQL",)
    lista.extend(("C#", "Javascript", "SQL",))
    print(lista)

    # insert(indice, valor)
    # Insere o valor no índice informado
    # Inserir o valor "Golang" na penúltima posição
    lista.insert(-1, "Golang")
    print(lista)

    # Podemos alterar o valor de um item em uma lista a partir de sua posição, ou
    # seja, do seu índice
    lista[1] = "PHP"
    print(lista)

    # Devemos tomar cuidado ao informar um índice de uma lista, pois se o índice
    # não existir, é gerada a exceção IndexError
    # A linha abaixo irá gerar a exceção IndexError
    # lista[10] = "ABC"