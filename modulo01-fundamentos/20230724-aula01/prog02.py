# Tipos de dados em Python

# tipos numéricos: int, float, complex
# tipo string: "python"
# tipo boolean: True, False

if __name__ == "__main__":
    
    # Tipos inteiros não possuem casa decimal
    a = 1
    b = 3
    print(a + b)

    # Tipo float (ponto flutuante) possui casas decimais
    resultado = 10 / 3
    print(resultado)

    # Números complexos possuem 2 partes: A real e a imaginária
    print(1j)

    # Uma string em Python é qualquer sequência de caracteres que
    # esteja dentro de aspas simples ou duplas

    nome = "Amanda"
    nome = 'Carla'
    texto = "Curso de 'Python'"

    print(texto)

    # input é a função built-in que recebe dados via teclado
    nome = input("Informe o seu nome: ")

    print(nome)

    # Há algumas maneiras de concatenar strings em Python
    # Utilizando o operador '+'
    print("Bem vindo ao curso, " + nome + ".")

    # Usando o caracter '%'
    print("Bem vindo ao curso, %s." % (nome,))

    # Usando o método format()
    print("Bem vindo ao curso, {}.".format(nome))

    # Podemos também nomear os parâmetros do format
    print("Bem vindo ao curso, {aluno}.".format(aluno=nome))

    # Podemos utilizar também as f-strings
    print(f"Bem vindo ao curso, {nome}.")

    # Podemos também utilizar strings multi-linhas no Python
    # Elas começam por uma sequência de 3 aspas (simples ou duplas) e terminam
    # da mesma maneira
    instrutor = "Alessandro Bispo"
    texto = f"""
Bem-vindos ao curso de Python.

Instrutor: {instrutor}

Ementa Fundamentos
    - O que é Python
    - Instalando o Python

"""

    print(texto)

    # Também temos o tipo de dado booleano em Python, representado por
    # True e False

    print(True, False)