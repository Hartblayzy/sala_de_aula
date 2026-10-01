class Retangulo:
    base: int
    altura: int

    def __init__(self, base: int, altura: int):
        self.base = base
        self.altura = altura


    def calcula_area (self):
        area = self.base * self.altura

        return f'Area : {area}'

    def calcular_perimetro(self):
        perimetro = 2 * (self.base + self.altura)

        return f'Perimetro : {perimetro}'
    

retangulo = Retangulo(5, 10)

print(retangulo.calcula_area())
print(retangulo.calcular_perimetro())
    