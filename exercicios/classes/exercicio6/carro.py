class Carro:
    marca: str
    modelo: str
    ligado: bool

    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print (f'O {self.marca} {self.modelo} agora está ligado')

    def desligar(self):
        self.ligado = False
        print (f'O {self.marca} {self.modelo} agora está desligado')



carro = Carro('Renault', 'Clio')


carro.ligar()
carro.desligar()
    