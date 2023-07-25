# Operadores em Python

# Um operador é uma instrução aplicada a valor ou valores
# No Python, podemos trabalhar com operadores unários ou binários

# Geralmente aplicamos os operandos em expressões
# Uma expressão é um conjunto de instruções que resolvem (simplifica) em apenas
# 1 valor

if __name__ == "__main__":
    
    # Exemplo de expressão em Python
    # Utilizando operadores aritméticos
    calculo = 3 * 10 + (15 + (5 ** 9) / 14) + 13 * 2 - (4 ** 8)
    print(calculo)

    numero = 10
    numero = numero + 15
    print(numero)

    # numero = numero - 8
    numero -= 8
    print(numero)

    # Operadores de comparação
    # A função input SEMPRE retorna uma string. Se precisarmos fazer algum tipo
    # de operação matemática nos números, precisamos convertê-los primeiro



    idade = int(input("Informe a sua idade: "))

    if idade < 18:
        print("Você é menor de idade")

        # a palavra reservada and representa o operador lógico E
    elif idade >= 18 and idade < 21:
        print("Já está quase lá")
    else:
        print("Você já é adulto. Sinto muito")


    # A palavra reservada OR representa o operador lógico OU
    print(4 < 5 or 10 > 100)

    # A palavra reservada not representa o operador lógico NÃO
    print(not 5 > 1)

    # Operadores de identidade (is, is not)
    # Verificam se um objeto é igual

    lista1 = ["Python", "C3"]
    lista2 = lista1

    print(lista1 is not lista2)
    print(id(lista1), id(lista2))

    # Operadores de pertencimento (in, not in)
    # Verificam se um valor está contido dentro de uma
    # sequência (ou container)
    lista_usuarios = ["maria", "joao", "jose", "paulo"]

    meu_usuario = "joao"

    if meu_usuario in lista_usuarios:
        print("Você está na lista. Acesso aprovado.")
    else:
        print("Você não está na lista. Acesso negado.")

    # Podemos utilizar esses operadores em strings
    # Strings são *sequências* de caracteres

    if "Y" not in "Python".upper():
        print("Existe a letra Y.")