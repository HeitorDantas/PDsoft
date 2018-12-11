import sqlite3

class RedeSocial:
    def __init__(self):	
        self.conexao = sqlite3.connect('redesocial.db')
        self.gerenciador = self.conexao.cursor()

    def cadastrar(self, login, senha):
        sql = '''
            insert into usuario
            (login, senha)
            values (?,?);
        '''

        self.gerenciador.execute(sql,(login, senha))
        self.conexao.commit()
    def logar(self,login,senha):
        '''
            Faz uma busca no DB, pelo usuario e senha, e verifica se 
            as duas informaçoes batem
        '''
        sql = """
            select (login) from usuario
            where login=?;
        """

       	args = (login,)
        self.gerenciador.execute(sql,args)
        self.conexao.commit()
		
        info = self.gerenciador.fetchall()
        for i in info:
            print(i)
#rs = RedeSocial()
#rs.cadastrar('pv', '123')

