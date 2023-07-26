# Estruturas de controle de repetição

if __name__ == "__main__":
    """
    O Python possui 2 estruturas de controle de repetição:

    for
    * Geralmente usado pra percorrer uma sequência (ou container).
    Ou seja, ele é executado enquanto houverem itens nessa sequência
    a serem processados
    """

    # Exemplo: Calcular e mostrar o quadrado dos itens de uma lista de
    # números
    lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for numero in lista_numeros:
        # print("O quadrado de " + numero + " é igual a " + numero * numero + ".")
        # print("O quadrado de %s é igual a %s." % (numero, numero * numero))
        # print("O quadrado de {} é igual a {}.".format(numero, numero * numero))
        print(f"O quadrado de {numero} é igual a {numero * numero}.")


    # Exemplo 2: Identificando os dados em uma lista
    # Listas podem conter qualquer tipo de valor, inclusive outras
    # listas
    lista_de_valores = [
        10,
        56.7,
        "Curso de Python",
        "Curso de C#",
        [1, 2, 3],
        (1, 4, 6,),
        {"nome": "jose", "idade": 30},
    ]

    for valor in lista_de_valores:
        print(f"O tipo do valor {valor} é {[type(valor)]}.")

    # break
    # Dentro de um loop, se for encontrada uma cláusula break, o loop
    # é imediatamente finalizado

    # Exemplo: Utilizando a lista anterior, vamos percorrê-la até ser
    # encontrado um tipo de dado Lista. Se for encontrado, o loop é
    # imediatamente finalizado

    for valor in lista_de_valores:
        if isinstance(valor, list):
            print("Lista encontrada! Finalizando loop")
            break

        print(f"O tipo do valor {valor} é {type(valor)}.")

    # continue
    # Dentro de um loop, se for encontrada a cláusula continue, a execução
    # atual é cancelada e o próximo item da sequência é lido

    # Exemplo: Utilizando a lista anterior, vamos percorrê-la somando
    # os tipos númericos e imprimindo o resultado no final. Outros
    # tipos de dados serão ignorados.

    # Bônus: Aqui vamos utilizar o método append() para adicionar mais
    # valores à lista.

    lista_de_valores.append(4)
    lista_de_valores.append(12.9)

    soma = 0

    for valor in lista_de_valores:
        if not isinstance(valor, int) and not isinstance(valor, float):
            print(f"O valor {valor} não é numérico. Ignorando...")
            continue

        # soma = soma + valor
        soma += valor

    """
    while

    O laço while é a segunda estrutura de controle de repetição do Python.
    Diferentemente do laço for, o laço while vai executar um bloco de código
    enquanto uma expressão for verdadeira
    
    """

    # Exemplo: Dada uma lista de palavras, uma delas será sorteada de forma
    # randômica. Crie um laço for para a palavra ser adivinhada em no máximo
    # 3 tentativas

    lista_de_palavras = [
        "python", "php", "golang",
        "java", "haskell", "javascript",
        "elixir", "dart", "perl"
    ]

    # A linha abaixo importa a função choice do módulo random, que faz parte da
    # biblioteca padrão do python (Python Standard Library)
    # A função choice escolhe uma opção randomicamente de uma sequência
    from random import choice

    palavra_secreta = choice(lista_de_palavras)
    chances = 3

    while chances > 0:

        palavra = input("Adivinhe a palavra secreta: ")

        if palavra.lower() == palavra_secreta:
            print(f"Parabéns! Você acertou a palavra secreta '{palavra_secreta}'.")
            break

        else:
            chances = chances - 1
            texto = f"Você errou! Você tem mais {chances} tentativa(s)."

            print(texto)

    # O bloco else é executado quando o laço while é finalizado. É importante
    # notar que ele só é executado se nenhuma cláusula break for executada
    else:
        print(f"Você errou todas as tentativas. A palavra secreta era {palavra_secreta}.")