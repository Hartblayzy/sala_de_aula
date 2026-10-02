class Elevador:
    andar_atual: 0
    total_andares: int


    def __init__(self, andar_atual: int, total_andares: int):
        self.andar_atual = andar_atual
        self.total_andares = total_andares

    def descer(self):
        if self.andar_atual > 0:
            print (f'Descendo...')
            self.andar_atual -= 1

            print (f'Você esta no andar: {self.andar_atual}')
            if self.andar_atual == 0:
                print (f'Você esta no térreo')
                
            
            if self.andar_atual == 0:
                print (f'Você esta no térreo')

        else:
            self.andar_atual = 0
    
    def subir(self):
        if self.andar_atual < self.total_andares:
            print (f'Subindo...')
            self.andar_atual += 1
            print (f'Você esta no andar: {self.andar_atual}')
            
            if self.andar_atual == self.total_andares:
                print (f'Você chegou ao último andar')
        
        
        else:
            self.andar_atual = self.total_andares




elevador = Elevador(10, 10)

elevador.descer()
elevador.descer()
elevador.descer()
elevador.descer()
elevador.descer()
elevador.descer()
elevador.descer()
elevador.descer()
elevador.descer()
elevador.descer()
elevador.descer()



        