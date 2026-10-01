class Cachorro:
    nome:str
    raca: str
    idade: int

    def __init__ (self, nome: str, raca: str, idade: int):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir (self):
        print (f' Au Au! O {self.nome} está latindo.')


cachorro = Cachorro('Otto','Shi-tzu', 2 )

cachorro.latir()