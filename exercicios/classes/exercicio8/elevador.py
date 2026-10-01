class Elevador:
    andar_atual: int
    total_andares: int


    def __init__(self, andar_atual: int, total_andares: int):
        self.andar_atual = 0 = andar_atual
        self.total_andares = total_andares

        