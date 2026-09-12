class Usuario:
    def __init__(self,login,senha):
        self.__login = login
        self.__senha = senha 

    def alterar_senha(self,senha_antiga,nova_senha):
        if senha_antiga == self.__senha:
            self.__senha = nova_senha
            print("Senha Alterada com sucesso!")
        else:
            print("Acesso negado: Senha Incorreta!")

login = input("Digite o seu login: ")
senha = input("Digite a sua senha: ")

usuario = Usuario(login, senha)
print("\n Usuário cadastrado com sucesso!")

senha_antiga = input("Digite a sua senha atual: ")
nova_senha = input("Digite a sua nova senha: ")
usuario.alterar_senha(senha_antiga, nova_senha)