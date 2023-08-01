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


class Carro(Veiculo):

    def __init__(self, marca, modelo, ano):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano

    def abrir_portas(self):
        print("Portas do carro abertas")

    def fechar_portas(self):
        print("Portas do carro fechadas")


class Moto:

    def __init__(self, marca, modelo, ano, cilindradas):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._cilindradas = cilindradas

    def ligar(self):
        print("Moto ligada")

    def desligar(self):
        print("Moto desligada")

    def dar_grau(self):
        print("Chama no grau")


class Bicicleta:

    def __init__(self, marca, modelo, ano, numero_de_marchas):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._numero_de_marchas = numero_de_marchas

    def pedalar(self):
        print("Bicicleta pedalando")

if __name__ == "__main__":

    gol_quadrado = Carro("Gol Geração 1", "1995 Turbo", 1995)
    gol_quadrado.fechar_portas()
    gol_quadrado.ligar()
    gol_quadrado.desligar()