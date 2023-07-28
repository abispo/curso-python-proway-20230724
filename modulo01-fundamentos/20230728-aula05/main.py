"""
Funções

Função é um bloco de código que pode ser chamado em qualquer lugar do
nosso programa.

Utilizamos a palavra reservada def pra criar funções em Python

"""

# A função imprime uma mensagem no terminal
def ola():
    print("Olá mundo")

# Podemos passar valores pra dentro de uma função. Chamamos
# esse valores de parâmetros ou argumentos
def ola_nome(nome):
    print(f"Olá {nome}, bem-vindo ao curso de Python.")

# Uma função em Python pode ter infinitos parâmetros
def verifica_idade(nome, idade):
    if idade < 18:
        print(f"{nome}, você é menor de idade")
    else:
        print(f"{nome}, você é maior de idade")


# Uma função em Python pode ter parâmetros com valores padrão. Ou seja, se
# não forem passados valores para esse parâmetro, ele assume o valor
# informado na definição da função
def calculo_salario(nome, funcao, setor=1):
    if setor == 1:
        salario = 1000
        print(f"{nome}, sua função como {funcao} no setor {setor} recebe {salario}")

    elif setor == 2:
        salario = 3000
        print(f"{nome}, sua função como {funcao} no setor {setor} recebe {salario}")

    else:
        print("Setor desconhecido")

# As funções anteriores não retornam valores quando são chamadas
# Se quisermos criar uma função que retorna algum valor, precisamos
# utilizar a palavra reservada return
def calculo_imc(peso, altura):
    imc = peso / (altura * altura)

    return imc

# *args é tratado como uma tupla
def soma_valores_passados(*args):
    return sum(args)

# **kwargs é tratado como um dicionário
def mostra_info(**kwargs):

    for key, value in kwargs.items():
        print(f"Key: {key} | Value: {value}")

if __name__ == "__main__":
    
    # Chamamos uma função pelo seu nome, não esquecendo de abrir e fechar
    # os parentesis
    ola()

    # Passando o valor José para o argumento 'nome'
    ola_nome("José")

    # Passando valores para os argumentos 'nome' e 'idade'
    verifica_idade("José", 40)
    verifica_idade("João", 18)
    verifica_idade("Maria", 15)

    # Nas funções acima, definimos uma quantidade obrigatória de argumentos. Ou seja,
    # quando a função for chamada, devemos passar exatamente a quantidade de argumentos
    # na ordem, ou recebemos um erro

    # A linha abaixo irá gerar uma exceção, pois a função verifica_idade recebe
    # 2 argumentos, e estamos passando apenas 1
    # verifica_idade("Paulo")

    # Não somos obrigados a passar os valores para a função de maneira posicional.
    # Podemos passar os valores pelo nome do parâmetro, ou via 'keyword'
    nome = "Vanessa"
    idade = 30

    # Se quiséssemos pegar esses valores pelo terminal, poderíamos usar a função
    # input()
    # nome = input("Informe o seu nome: ")
    # idade = int(input("Informe a sua idade: "))

    verifica_idade(idade=idade, nome=nome)

    # Como o parâmetro setor já possui um valor padrão, não precisamos
    # passar um valor para ele
    calculo_salario("Jair", "Eletricista")

    # Podemos passar valores para todos os parâmetros
    calculo_salario("Luis", "Borracheiro", 2)

    # Se quisermos, podemos chamar uma função informando os valores
    # via posição e via nome do parâmetro
    calculo_salario("Márcia", setor=5, funcao="Gerente")

    # A única regra na última chamada, é que somos obrigados a passar
    # primeiro os valores de maneira posicional, e depois via nome
    # do parâmetro

    # A chamada a seguir irá gerar uma exceção
    # calculo_salario(setor=2, "Programador", nome="Alessandro")

    saida = calculo_salario("Tiago", "Gerente", 1)
    print(saida)

    imc = calculo_imc(80, 1.80)
    # Se quisermos formatar o valor suprimindo algumas casas decimais
    # Podemos utilizar a sintaxe especial depois dos dois pontos
    print(f"IMC: {imc:.2f}")

    # Vamos imaginar o seguinte cenário:
    # Precisamos criar uma função que receba números como valores,
    # porém essa quantidade de números pode variar a cada chamama.
    # Para isso, criamos uma função que recebe uma quantidade
    # arbitrária de argumentos utilizando asterisco (*)

    soma = soma_valores_passados(3, 6, 2, 3, 8, 9, 4)
    soma += soma_valores_passados(1, 4, 7, 3)
    soma += soma_valores_passados(3)
    soma += soma_valores_passados()

    print(soma)

    # É importante notar que utilizando *args, vamos sempre
    # passar os valores via posição

    # Se quisermos passar valores via nome de parâmetros, utilizamos
    # **kwargs (KeyWord args)

    mostra_info(nome="José", idade=30)
    mostra_info(nome="Maria", cidade="Blumenau", estado="SC")
    mostra_info(status="Ativo", registro=True)
    mostra_info()