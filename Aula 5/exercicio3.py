class AssinaturaBase:
    def __init__(self,usuario):
        self.usuario = usuario
    
    def calcular_preco(self)
        valor = 0
        return valor
    
class AssinaturaPremium(AssinaturaBase):
    def __init__(self,usuario)
    super().__init__(usuario)
    
    def calcular_preco(self)
        return 49.90

class AssinaturaEstudante(AssinaturaBase):
    def __init__(self,usuario)
    super().__init__(usuario)
    
    def calcular_preco(self)
        return 24.90

usuario_premium = AssinaturaPremium("Mateus") 
usuario_estudante = AssinaturaEstudante("João")

print("Plano Premium:") 
print(f"Usuário: {usuario_premium.usuario}")
print(f"Preço: R$ {usuario_premium.calcular_preco():.2f}")

print("\nPlano Estudante:") 
print(f"Usuário: {usuario_estudante.usuario}") 
print(f"Preço: R$ {usuario_estudante.calcular_preco():.2f}")