"""
Exercício 01

Crie um programa que peça ao usuário para digitar um número
inteiro e exiba se ele é positivo, negativo ou zero.

"""

if __name__ == "__main__":
    
    numero = int(input("Informe um número inteiro: "))

    if numero < 0:
        print(f"O número {numero} é negativo.")

    elif numero > 0:
        print(f"O número {numero} é positivo")

    else:
        print("O número informado é 0")