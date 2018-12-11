from Sistema_RedeSocial import *
from interface import *


RS = RedeSocial()

## User interface
#tela inicial
#tela de login
#tela de cadastro

def telaInicial():
	print("---------  Bem vindo   -------\n")

	print("Menu:")
	print("1 - Fazer Login")
	print("2 - Fazer cadastro")
	print("3 - Sair do programa")
	return '1','2','3'

def telaLogin():
	login = input("LOGIN: ")
	senha = input("SENHA: ")
	return (login,senha)

def telaCadastro():
	print("---CADASTRO DE USUARIO---")
	login = input("LOGIN: ")
	senha = input("SENHA: ")
	return (login,senha)

def telaHomePage():
	'''
		mostra as opcoes disponiveis para um usuario logado
	'''
	pass
def escolherOpcao(listaOpcoes):
	while True:
		op = input("Digite a opcao: ")
		if op in listaOpcoes:
			return op
		else:
			print("opcao invalida")
			continue

def main():

	while True:
		opcoes = telaInicial()

		op = escolherOpcao(opcoes)

		if op is '1':
			login,senha = telaLogin()

			#RedeSocial valida o login e manda o usuario para a homePage
			loginOK = RS.logar(login,senha)
			if loginOK is False:
				print("Login ou senha incorretas, tente novamente")
				continue
			else:
				telaHomePage()

		elif op is '2':
			login,senha = telaCadastro()
			'''
			redeSocial faz o cadastro, insere o usuario no DB
			verifica se o usuario ja existe

			'''
			RS.cadastrar(login, senha)
		elif op is '3':
			print("TCHAU")
			return


if __name__ == '__main__':

	main()
