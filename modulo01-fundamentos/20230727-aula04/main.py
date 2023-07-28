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