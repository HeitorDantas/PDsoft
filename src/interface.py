from os import system,name

def clear():
	system('cls' if name == 'nt' else 'clear')

class UI:
	'''classe de interface do usuario'''
	def __init__(self):
		self.listaOpcoes = []

	def _mostrar(self):
		'''abtract method'''
		pass

	def escolherOpcao(self):
		while True:
			op = input("Digite a opcao: ")
			if op in self.listaOpcoes:
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
				return self.branch(op)
	def branch(self,op):
		ret = ''
		if op is '1': ret = 'login'
		elif op is '2': ret = 'cadastro'
		elif op is '3': ret =  'sair'
		else: ret =  self.nome
		return ret
class UI_TelaInicial(UI):
	nome = 'inicio'
	def __init__(self):
		self.listaOpcoes = [1,2,3]
		self.listaOpcoes = [str(op) for op in self.listaOpcoes]
	def _mostrar(self):

		print("---------  Bem vindo   -------\n")

		print("Menu:")
		print("1 - Fazer Login")
		print("2 - Fazer cadastro")
		print("3 - Sair do programa")

class UI_HomePage(UI):
	nome = 'homepage'
	def __init__(self):
		self.listaOpcoes = [1,2,3,4]
		self.listaOpcoes = [str(op) for op in self.listaOpcoes]
	def _mostrar(self):
		print("---------  Bem vindo   -------\n")

		print("Menu:")
		print("1 - Timeline")
		print("2 - Postar")
		print("3 - Postar")
		print("4 - Sair")

class UI_Login(UI):
	nome = 'login'
	def run(self):
		self.login = input("LOGIN: ")
		self.senha = input("SENHA: ")
		#if sucesso vai para homePage
		#else para inicio
		return 'inicio'




if __name__ == '__main__':
	telas = {(tela.nome):tela for tela in UI.__subclasses__()}


	telaAtual = telas['inicio']()
	while True:
		proxTela = telaAtual.run()
		if proxTela is 'sair':
			print("TCHAU")
			break
		telaAtual = telas[proxTela]()
