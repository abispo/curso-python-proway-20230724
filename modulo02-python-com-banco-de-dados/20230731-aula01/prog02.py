"""
Programação Orientada a Objetos

Encapsulamento

É o processo de "esconder" detalhes da implementação de uma classe de outros
objetos. Esse processo é um pouco diferente no Python, se formos comparar com
outras linguagens como Java e C#.

"""

class ContaBancaria:
    
    def __init__(self, numero, saldo):

        """
        No Python não temos o conceito de público ou privado, ou seja, qualquer
        objeto definido dentro de uma classe pode ser acessando diretamente. Porém
        utilizamos a convenção do '_', ou seja, todo atributo/método de uma classe
        que começa por '_' devem ser tratados como atributos/métodos privados
        """
        self._numero = numero
        self._saldo = saldo

    def sacar(self, valor):
        if valor >= self._saldo:
            self._saldo = self._saldo - valor
            return valor        

    def depositar(self, valor):
        if valor > 0:
            self._saldo = self._saldo + valor

    """
    Podemos criar os métodos getters e setters utilizando a sintaxe própria do
    Python, que se dá através do decorator @property

    Dessa maneira, acessamos o valor do atributo "privado" a partir de um 
    acessor "público"

    # O decorator @property transforma um método em um atributo, ou seja, não
    utilizamos mais os parentesis
    """
    @property
    def numero(self):
        return self._numero
    
    @property
    def saldo(self):
        return self._saldo
    
    def get_saldo(self):
        return self._saldo


if __name__ == "__main__":

    conta_viacredi = ContaBancaria(123, 1000)
    print(conta_viacredi.numero)