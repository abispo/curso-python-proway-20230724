"""
Programação Orientada a Objetos

Classe Pokemon

Utilizamos a palavra reservada class para criar uma classe

Apesar de não ser obrigatório, recomenda-se que se use a sintaxe de PascalCase na
definição do nome da classe, ou seja, a primeira letra será sempre maiúscula

"""

class Pokemon:
    
    """
    Método __init__.

    É um dos inúmeros métodos mágicos do Python. Serve para inicializar o objeto
    criado. Apesar de não ter tecnicamente correto, podemos comparar o método
    __init__ com os métodos construtores de outras linguagens, como Java ou C#

    No caso abaixo, o método inicializador recebe 3 parâmetros: name, type e health
    Os valores passados serão atribuídos às propriedados do objeto

    """
    def __init__(self, name, type, health):
        
        """
        O self é um argumento obrigatório quando trabalhamos com métodos de uma
        classe. O self nada mais é do que uma referência ao próprio objeto, assim
        como temos o 'this' em Java ou C#. A diferença é que precisamos informar
        explicitamente.

        Abaixo, estamos criando 3 atributos da classe Pokemon: _name, _type e
        _health. Esses atributos recebem os valores passados na instanciação
        do objeto
        
        """
        self._name = name
        self._type = type
        self._health = health

    """
    Criamos os métodos abaixo informando como argumento obrigatório a palavra
    reservada self. Dessa maneira, temos acesso aos atributos e métodos do objeto
    em qualquer lugar da nossa classe. Isso não se aplica a métodos de classe
    e métodos estáticos.
    """
    def attack(self):
        print(f"{self._name} atacou!")

    def dodge(self):
        print(f"{self._name} desviou do ataque!")

    def evolve(self):
        print(f"{self._name} evoluiu!")

    def info(self):
        saida = f"""
        INFORMAÇÕES DO POKEMON
        ----------------------

        Nome: {self._name}
        Tipo: {self._type}
        Constituição: {self._health}HP
        """

        return saida

if __name__ == "__main__":

    pikachu = Pokemon("Pikachu", "Elétrico", 70)
    print(pikachu.info())
    charmander = Pokemon("Charmander", "Fogo", 60)

    # pikachu e charmandar são instâncias da mesma classe, portanto objetos
    # diferentes
    print(pikachu is charmander)

    """
    Podemos criar uma quantidade de objetos virtualmente infinita a partir
    de uma classe
    """
    lista = [Pokemon("", "", 0) for _ in range(100000)]
