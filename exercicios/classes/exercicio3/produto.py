class Produto:
    nome:str
    preco:float


    def __init__(self, nome:str, preco:float):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual: float):
         self.preco -= self.preco * (percentual / 100)

         return self.preco

desconto = Produto('abacaxi', 5)

print (f'Valor Final: R$ {desconto.aplicar_desconto(10)}')
