class Circulo:
    raio: int

    def __init__(self, raio: int):
        self.raio = 10 if raio < 10 else raio


#Instância
circulo = Circulo (8)



