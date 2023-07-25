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
