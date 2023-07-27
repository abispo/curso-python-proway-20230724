"""
Estruturas de dados em Python

Tuplas e Sets (conjuntos)

"""

if __name__ == "__main__":
    """
    Tuplas.

    Tuplas são como listas, ou seja, armazenam qualquer tipo de dados. A principal
    diferença, e que tuplas são imutáveis, ou seja, depois de criadas não podem
    ser alteradas
    
    """

    # Criando uma tupla
    tupla = ("Python", "Javascript", "C#",)
    print(tupla)
    tupla = tuple("Curso de Python")
    print(tupla)

    # Como dito anteriormente, não conseguimos alterar os valores de uma tupla
    # A linha abaixo irá gerar uma exceção
    # tupla[4] = "Java"

    # Se por algum motivo, seja necessário alterar um valor em uma tupla, podemos
    # utilizar a estratégia de transformar essa tupla em uma lista, alterar o valor
    # e transformar novamente em tupla
    lista_temporaria = list(tupla)
    lista_temporaria.clear()
    lista_temporaria = ["Python", "C#", "Java", "SQL"]
    tupla = tuple(lista_temporaria)

    print(tupla)

    # Tirando essa questão de imutabilidade, podemos aplicar slices
    # iteração usando o laço for e consulta de valores pelo índice
    # da tupla, assim como nas listas

    print(tupla[0])
    print(tupla[1:3])
    for valor in tupla:
        print(valor)

    # Métodos de tupla
    # count(valor): Conta quantas vezes um valor se repete

    # Não podemos adicionar nem remover itens de uma tupla, porém
    # podemos criar uma nova tupla a partir da concatenação de 2
    # ou mais tuplas
    tupla = tupla + ("Python",)
    print(tupla)
    
    print(f"O valor 'Python' aparece {tupla.count('Python')} vez(es)")

    # index(valor): Retorna a posição da primeira ocorrência do valor
    # informado
    print(f"A primeira ocorrência do valor 'Python' aparece na posição {tupla.index('Python')}.")

    # ------------------------------------------------------------------------
    # ------------------------------------------------------------------------

    # Sets (conjuntos)
    # Set é uma estrutura de dados que armazena um conjunto de valores
    # Sets não são ordenados, não são indexados e são imutáveis*.
    # Sets não permitem valores repetidos.
    # *Imutável no sentido que não conseguimos alterar um valor, porém conseguimos
    # adicionar ou remover valores

    # Criação de um set (conjunto)
    conjunto = {1, 2, 4, 5}
    print(conjunto)

    conjunto = set([1, 2, 3, 4, 5])
    print(conjunto)

    # Não conseguimos acessar o valor de um set utilizando a sintaxe de índices
    # A linha abaixo irá gerar uma exceção
    # print(conjunto[1])

    # Como não conseguimos acessar um item pelo índice, também não conseguimos
    # alterar um item pelo índice. A linha abaixo irá gerar uma exceção
    # conjunto[0] = 10

    # Apenas os valores são imutáveis, o set em si não.
    # Podemos utilizar os métodos add() ou update()

    conjunto.add(10)
    conjunto.update({20, 30})

    print(conjunto)

    # Para remover itens de um set (conjunto), podemos utilizar os métodos
    # remove() ou discard()

    # remove(valor): Se o valor não existir, é gerada uma exceção
    # A linha abaixo irá gerar uma exceção
    # conjunto.remove(100)
    conjunto.remove(20)
    print(conjunto)

    # discard(valor): Se o valor não existir, nada acontece
    conjunto.discard(1000)
    conjunto.discard(10)
    print(conjunto)

    # pop(): Remove um item aleatório do set
    conjunto.pop()
    print(conjunto)

    # clear(): Remove todos os itens do set
    conjunto.clear()

    # del: Remove o objeto
    del conjunto

    for item in {"Python", "Java", "C#"}:
        print(item)

    # Conjuntos não permitem valores duplicados
    conjunto = {1, 1, 2, 2, 2, 3, 4, 5, 5, 5, 5, 5}
    print(conjunto)

    # Essa característica pode ser útil em alguns cenários.
    # Por exemplo: Digamos que temos uma lista de números, com alguns valores 
    # duplicados. Podemos transformar essa lista em um set, depois transformar
    # esse set em uma lista

    # Vamos usar a função randint() do módulo random
    # Essa função gera um número inteiro randômico dentro do intervalo informado
    from random import randint

    lista_numeros = [randint(1, 50) for _ in range(1, 101)]
    # O método sort ordena uma lista
    # Por padrão, se for uma lista de números, ele ordena do menor pro maior
    # Se for uma lista de strings, ele ordena em ordem alfabética
    lista_numeros.sort()
    print(lista_numeros)

    # Podemos remover os valores repetidos criando um set a partir dessa lista
    lista_numeros = list(set(lista_numeros))
    print(lista_numeros)
