class Carta:
    remetente: str
    destinatario: str
    conteudo: str
    
    def __init__(self, remetente: str, destinatario: str, conteudo: str):

        self.remetente = remetente
        self.destinatario = destinatario
        self.conteudo = conteudo

carta = Carta(destinatario='Bianca', remetente= 'Arthur', conteudo= 'Te amo')