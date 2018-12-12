import sqlite3
from usuario import *

class RedeSocial(object):
    def __init__(self):
        self.database = Gerenciador()
        self.database.criarTabela("sql/usuarios.sql")
        self.database.criarTabela("sql/postagens.sql")
        self.database.criarTabela("sql/curtidas.sql")
        self.database.criarTabela("sql/seguidores.sql")

    def cadastrar(self,nome, login, senha):
        '''cadastra usuario se ele nao existir'''

        usuario = Usuario(nome,login)

        self.database.inserirUsuario(usuario,senha)

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


class Gerenciador(object):
    def __init__(self):
        self.conexao = sqlite3.connect('redesocial.db')
        self.cursor = self.conexao.cursor()
    def criarTabela(self,sql_file):
        with open(sql_file,'rt') as file:
            command = file.read()
            self.cursor.execute(command)
            self.conexao.commit()
    def inserirUsuario(self,user,senha):
        '''recebe um usuario e coloca no BDD,
            é chamada quando um usuario se cadastra no sistema
        '''
        args = (user.nome, user.login, senha)
        #verifica se ja existe
        if self.dadosLogin(user.login) is not None:
            print("Usuario ja existe")
            return None
        #insere

        sql = '''
            insert into usuarios (nome,login,senha) values (?,?,?);
        '''
        self.executeSQL(sql,args)

    def inserirPostagem(self,post):
        pass
    def inserirSeguidor(self,seguidor,seguindo):
        pass
    def inserirCurtida(self):
        pass
    def dadosLogin(self,login):
        sql = '''
            select * from usuarios where login=?;
        '''
        self.executeSQL(sql,(login,))
        ret = self.cursor.fetchone()

        return ret
    def executeSQL(self,cmd,args):
        self.cursor.execute(cmd,args)
        self.conexao.commit()


if __name__ == '__main__':
    RS = RedeSocial()
    RS.cadastrar('heitor','heitor','123')
    RS.cadastrar('heitor','heitor2','123')
