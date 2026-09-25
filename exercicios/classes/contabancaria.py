class ContaBancaria:
    titular: str
    saldo: 0

    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.saldo = saldo

    def depositar_valor (self, deposito: float):
        self.saldo += deposito

        return f'Titular: {self.titular} | Novo Saldo: R$ {self.saldo}'
    
saldo = ContaBancaria(saldo=0, titular='Arthur')


print(saldo.depositar_valor())
print(saldo.depositar_valor())
print(saldo.depositar_valor())
print(saldo.depositar_valor())
print(saldo.depositar_valor())


