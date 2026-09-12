class Animal:
    def __init__(self, membros, orgaos):
        self.membros = membros
        self.orgaos = orgaos
    
    def comer():
        print("hmmm")

    def reproduzir(self, parceiro):
        return self + parceiro
    
class Ave(Animal):
    def __init__(self, membros, orgaos, pena):
        super().__init__(membros, orgaos)
        self.penas = pena

    def voar():
        print("*Asa batendo")

class Mamifero(Animal):
    def __init__(self, membros, orgaos, pelo):
        super().__init__(membros, orgaos)
        self.pelo = pelo

    def beber_leite():
        print("hmmm leite")

class Primata(Mamifero):
    def __init__(self, membros, orgaos, pelo):
        super().__init__(membros, orgaos, pelo)
        self.polegares = 2