
class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print("Contruindo objeto ...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))
        
    def depositar(self, valor):
        self.saldo = self.saldo + valor
        
    def sacar(self, valor):
        self.saldo = self.saldo - valor
    
    