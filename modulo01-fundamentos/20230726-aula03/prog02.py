"""
Estruturas de dados em Python

Dicionário

Um dicionário é uma estrutura de dados no formato chave: valor (key: value),
que é ordenado, mutável e não permite chaves iguais

"""

if __name__ == "__main__":

    # Podemos criar dicionários de 2 maneiras

    # maneira mais comum
    jose = {
        "nome": "José",
        "sexo": "m",
        "idade": 20,
    }
    print(jose)

    # Usando o tipo built-in dict
    maria = dict(nome="Maria", sexo="f", idade=28)
    print(maria)

    # Existem algumas regras para a criação de dicionários.
    # Nem todos os tipos de dados são aceitos como chaves, por exemplo: listas
    # e outros dicionários

    # A linha abaixo irá gerar uma exceção, pois listas não podem ser usadas como
    # chave de dicionário, tampouco dicionários.
    # erro = {[1, 2, 3]: "Impossível"}

    # De preferência, sempre utilize strings como chaves de dicionário

    # Já quando falamos de valores, podemos ter qualquer tipo de dado, inclusive
    # outros dicionários

    usuario = {
        "id": 10,
        "score": 8.95,
        "permissoes": ["leitura", "escrita"],
        "info": {
            "nome": "Paulo",
            "setor": 80,
            "nivel": 3
        },
        "ativo": True
    }

    # Acessando as informações em um dicionário

    # Acessando diretamente pelo nome da chave
    print(usuario["score"])

    # Caso a chave informada não exista, recebemos uma exceção KeyError
    # print(usuario["banana"])

    # método get()
    # O método get, retorna o valor da chave informada. Se essa chave não existir,
    # ele retorna None, ou então um valor padrão que foi especificado

    # retorna o valor da chave permissoes
    print(usuario.get("permissoes"))

    # Caso informamos uma chave que não exista, ele retorna None
    print(usuario.get("autenticacao"))

    # Podemos informar um valor padrão que será retornado caso a chave não exista
    print(usuario.get("autenticacao", "A chave especificada não existe"))

    
    # Assim como listas, podemos iterar sobre as chaves e os valores de um
    # dicionário utilizando o laço for.
    
    # Por padrão, o laço for retorna os nomes das chaves do dicionário
    for chave in usuario:
        print(chave)

    # A chamada acima é equivalente à chamada seguinte:
    for chave in usuario.keys():
        print(chave)

    # Podemos utilizar 3 métodos para exibir informações do dicionário
    # .keys(): Retorna uma lista das chaves do dicionário
    # .values(): Retorna uma lista dos valores do dicionário
    # .items(): Retorna uma lista de tuplas com a chave e valor do dicionário

    for valor in usuario.values():
        print(valor)
    

    # Retornando a lista de tuplas com chave valor
    for chave, valor in usuario.items():
        print(f"Chave: {chave} | Valor: {valor}")


    # Alterar itens de um dicionário

    # Alterando o valor da chave score para 9.5
    usuario["score"] = 9.5
    print(usuario)

    # Se a chave existir, o valor será atualizado. Se ela não
    # existir, será criada com o valor informado
    usuario["autenticado"] = False
    print(usuario)

    # Também podemos atualizar ou criar novos dados dentro
    # do dicionário utilizando o método update()

    usuario.update({
        "permissoes": ["leitura"],
        "retorno": "positivo"
    })

    print(usuario)

    # Removendo itens do dicionário

    # Podemos utilizar até 4 métodos para remover itens de um
    # dicionário

    # .pop(chave): Remove o par chave-valor a partir da chave
    # especificada

    usuario.pop("retorno")
    print(usuario)

    # .popitem(): Remove o último par chave-valor adicionado.

    # Remove o par chave-valor com a chave "autenticado"
    usuario.popitem()
    print(usuario)

    # Removendo utilizando o comando del
    del usuario["ativo"]
    print(usuario)

    # .clear(): Limpa o dicionário
    usuario.clear()
    print(usuario)