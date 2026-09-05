class Filme:
    def __init__(self,titulo,duracao):
        self.assistido = False 
        self.titulo = titulo 
        self.duracao = duracao

    def marcar_como_assistido(self): #snakecase (Padrão fora da classe)
        self.assistido = True
        print(f'O {self.titulo} foi assistido ({self.assistido})')


filme1 = Filme("Django Livre","165")
filme2 = Filme("O Lobo de Wall Street","180")

filme1.marcar_como_assistido()
