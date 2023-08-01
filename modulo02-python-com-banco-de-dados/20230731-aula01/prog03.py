"""
Programação Orientada a Objetos

Herança

Utilizamos a herança quando criamos classes que herdam atributos e métodos de
uma classe pai(ou superclasse)

Exemplo: Sistema de gestão de veículos

"""

class Veiculo:

    def __init__(self, marca, modelo, ano):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano

    def ligar(self):
        print(f"{self._marca} ({self._modelo}/{self._ano}) ligou.")

    def desligar(self):
        print(f"{self._marca} ({self._modelo}/{self._ano}) desligou.")

"""
A linha abaixo indica que a classe Carro está herdando os métodos e os atributos
definidos na classe Veiculo. Podemos chamar a classe Carro de subclasse(ou classe filha)
e a classe Veículo de superclasse (ou classe pai/mãe)
"""
class Carro(Veiculo):

    def abrir_portas(self):
        print("Portas do carro abertas")

    def fechar_portas(self):
        print("Portas do carro fechadas")


class Moto(Veiculo):

    def __init__(self, marca, modelo, ano, cilindradas):
        """
        A função built-in super() executa um método definido na
        classe mãe. Usamos essa função pra executar um método que está sendo
        herdado
        """
        super().__init__(marca=marca, modelo=modelo, ano=ano)
        self._cilindradas = cilindradas

    def dar_grau(self):
        print("Chama no grau")


class Bicicleta(Veiculo):

    def __init__(self, marca, modelo, ano, numero_de_marchas):
        super().__init__(marca=marca, modelo=modelo, ano=ano)
        self._numero_de_marchas = numero_de_marchas

    def ligar(self):
        raise Exception("Bicicleta não liga!")
    
    def desligar(self):
        raise Exception("Bicicleta não desliga")

    def pedalar(self):
        print("Bicicleta pedalando")

if __name__ == "__main__":

    gol_quadrado = Carro("Gol Geração 1", "1995 Turbo", 1995)
    gol_quadrado.fechar_portas()
    gol_quadrado.ligar()
    gol_quadrado.desligar()

    vespa = Moto("Vespa", "Vespa 1979", 1979, 50)
    vespa.ligar()
    vespa.dar_grau()
    vespa.desligar()

    bicicleta = Bicicleta("Specialized", "Specialized 200000", 2023, 29)
    bicicleta.pedalar()
    bicicleta.ligar()