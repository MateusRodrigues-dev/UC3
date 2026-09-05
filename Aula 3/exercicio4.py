class CarteiraDigital:
    def __init__(self,nome_titular,saldo_inicial):
        self.nome_titular = nome_titular
        self.saldo_inicial = saldo_inicial

    

    def transferir_pix(self,valor,carteira_destino):
        if self.saldo_inicial >= valor:
            self.saldo_inicial -= valor
            carteira_destino.saldo_inicial += valor

            print(f"Transferência de R$ {valor:.2f} realizada com sucesso!")
        else:
            print("Erro: Saldo insuficiente para realizar o PIX.")

cliente_a = CarteiraDigital("Mateus", 500.00)
cliente_b = CarteiraDigital("Cliente B", 100.00)

cliente_a.transferir_pix(150.00, cliente_b)

print(f"Saldo de {cliente_a.nome_titular}: R$ {cliente_a.saldo_inicial:.2f}")
print(f"Saldo de {cliente_b.nome_titular}: R$ {cliente_b.saldo_inicial:.2f}")

