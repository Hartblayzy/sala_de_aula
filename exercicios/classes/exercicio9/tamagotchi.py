class Tamagotchi:
    nome : str
    fome : int
    energia : int

    def __init__(self, nome: str, fome: int, energia: int):
        self.nome = nome
        self.fome = fome if fome >=0 and fome <=100 else print(f'Valor incorreto para Fome')
        self.energia = energia if energia >= 0 and energia<= 100 else print(f'Valor incorreto para Energia')


    def comer(self):
        if self.fome >=0 and self.fome <=100:
            self.fome -=10 
            self.energia +=10
            if self.fome > 100:
                self.fome = 100
            elif self.fome < 0:
                self.fome = 0
            if self.energia > 100:
                self.energia = 100
            elif self.energia < 0:
                self.energia = 0


    
    