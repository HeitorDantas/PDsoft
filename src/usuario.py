

class Usuario(object):
	def __init__(self,nome,login,id=None):
		self.nome = nome
		self.login = login
		self.id = id
	def seguir(self,user):
		pass
	def curtir(self,post):
		pass
	def responderPostagem(self):
		'''talvez precisasse de uma classe de comentario
		,ao menos que se responda um post com outro post
		'''
		pass
	def buscarUsuario(self,user):
		pass
