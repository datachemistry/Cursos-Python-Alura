
class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print("Contruindo objeto ...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))
        
    def depositar(self, valor):
        self.__saldo = self.__saldo + valor
    
    
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.limite
        return valor_a_sacar <= valor_disponivel
        
    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo = self.__saldo - valor
        else:
            print("O valor {} ultrapassou o limite".format(valor))
        
    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        
    
    
    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite
    
    @property
    def titular(self):
        return self.__titular
    
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
    @staticmethod  
    def codigo_banco():
        return "001"
    
    @staticmethod  
    def codigos_bancos():
        return {'BB': '001','Caixa':'104','Bradesco':'237'}
        
# Código de teste
#>>> from conta import Conta
#>>> conta = Conta(123, "Nico", 55.5, 1000.0)
#Construindo objeto ... <conta.Conta object at 0x7f82af89d048>
#>>> conta.limite = 2000.0
#>>> conta.limite
#2000.0
    
    