from Sistema_RedeSocial import *
from interface import *


def main():
	#inicia componentes
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



if __name__ == '__main__':
	main()
