class Mago:
    pontos_de_vida:int 
    pontos_de_mana: int 
    capacidade: int = 50

    def __init__ (self,pontos_de_vida: int, pontos_de_mana: int):
        self.pontos_de_vida = pontos_de_vida
        self.pontos_de_mana = pontos_de_mana
        
mago = Mago(30, 50) #ou
mago_vekna = Mago(pontos_de_mana = 50, pontos_de_vida= 30)
        
