class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular 
        self.saldo = 0.0 

    def depositar(self,valor):
          self.saldo += valor 
          print(f'Esse é o seu saldo: R${self.saldo:.2f}')

    def sacar(self,valor):
        if self.saldo <= valor:
            print('Saldo insuficiente :')
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso")

conta = ContaBancaria("Mateus",0)

conta.depositar(100.00)

conta.sacar(150.00)

conta.sacar(50.00)

print(f"Titular: {conta.titular}")
print(f"Saldo final: R$ {conta.saldo:.2f}")



    
