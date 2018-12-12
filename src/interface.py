from os import system,name
from Sistema_RedeSocial import RedeSocial

def clear():
	system('cls' if name == 'nt' else 'clear')

class UI:
	'''
		--Classe de interface do usuario--
		Essa classe deve ter uma instacia redeSocial conectada
	'''
	RS = None
	def setRS(self,rs):
		self.id = rs

	def __init__(self):
		self.listaOpcoes = {}

	def _mostrar(self):
		'''abtract method'''
		pass

	def escolherOpcao(self):
		while True:
			op = input("Digite a opcao: ")
			if op in self.listaOpcoes.keys():
				return op
			else:
				raise IOError
	def run(self):
		op = None
		while True:
			self._mostrar()
			try:
				op = self.escolherOpcao()
				clear()
			except IOError as e:
				clear()
				print("opcao invalida")
			finally:
				return self.listaOpcoes[op]

class UI_TelaInicial(UI):
	nome = 'inicio'
	def __init__(self):
		ops = [1,2,3]
		opsNomes = ['login','cadastro','sair']
		self.listaOpcoes = {str(op):nome for op,nome in zip(ops,opsNomes)}
	def _mostrar(self):

		print("---------  Bem vindo   -------\n")

		print("Menu:")
		print("1 - Fazer Login")
		print("2 - Fazer cadastro")
		print("3 - Sair do programa")
	def branch(self,op):
		ret = ''
		if op is '1': ret = 'login'
		elif op is '2': ret = 'cadastro'
		elif op is '3': ret =  'sair'
		else: ret =  self.nome
		return ret
class UI_HomePage(UI):
	nome = 'homepage'
	def __init__(self):
		ops = [1,2,3,4]
		opsNomes = ['timeline','postar','buscar','sair']
		self.listaOpcoes = {str(op):nome for op,nome in zip(ops,opsNomes)}
	def _mostrar(self):
		print("---------  Bem vindo   -------\n")

		print("Menu:")
		print("1 - Timeline")
		print("2 - Postar")
		print("3 - Buscar")
		print("4 - Sair")


class UI_Login(UI):
	nome = 'login'
	def run(self):
		print("=======+++ LOGIN +++=========")
		self.login = input("LOGIN: ")
		self.senha = input("SENHA: ")
		#if sucesso vai para homePage
		#else para inicio
		return 'homepage'

class UI_Cadastro(UI):
	nome = 'cadastro'
	def run(self):
		print("=======+++ CADASTRO +++=========")
		self.login = input("LOGIN: ")
		self.senha = input("SENHA: ")
		#if sucesso vai para inicio
		#else para inicio
		return 'inicio'

if __name__ == '__main__':
	RS = RedeSocial()
	UI.setRS(UI,RS)
	telas = {(tela.nome):tela for tela in UI.__subclasses__()}

	telaAtual = telas['inicio']()
	while True:
		proxTela = telaAtual.run()
		if proxTela is 'sair':
			print("TCHAU")
			break
		try:
			telaAtual = telas[proxTela]()
		except KeyError as ke:
			print("Acao inexistente ou nao implementada ainda")
