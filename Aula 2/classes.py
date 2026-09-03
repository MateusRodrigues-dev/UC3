class Cachorro:
   #Método constructor 
    def __init__(self, nome, raca, tamanho, cor_pelo, patas): #Atributos da classe
        self.nome = nome 
        self.raca = raca 
        self.tamanho = tamanho
        self.cor_pelo = cor_pelo
        self.patas = 4 

#Self é um termo para a forma identificar com o que ela está lidando, o próprio objeto sendo criado
zeca = Cachorro("Zeca", "Viralata", "Médio", "Caramelo")
brutus = Cachorro("Brutus", "Pitbull", "Grande", "Preto")
mel = Cachorro("Mel", "Yorkshire", "Pequeno", "Marrom")

zeca.patas = 3 #como lidar com excessões 

print(zeca.nome)


class Usuario:
    def __init__(self, nome, email):
        self.nome = nome 
        self.email = email
        self.ativo = True 
  
  #Método de uma classe 
    def desativar_conta(self):
    self.ativo = False

    def mudar_nome(self):
    self.nome = input("Digite seu novo nome de usuário")


nova_conta = Usuario("Gustavo","gustavo@email.com")

nova_conta.desativar_conta()

print(nova_conta.ativo)
