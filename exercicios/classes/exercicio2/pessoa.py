class Pessoa:
    nome:str
    cidade:str

    def __init__(self, nome:str, cidade:str):
        self.nome = nome
        self.cidade = cidade


    def apresentar(self):
        return f'Olá, meu nome é {self.nome} e moro em {self.cidade}.'
    


pessoa = Pessoa(cidade='Porto Alegre', nome='Arthur')

print(pessoa.apresentar())