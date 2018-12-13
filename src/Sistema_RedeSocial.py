import sqlite3
import datetime
from usuario import *

class RedeSocial(object):
    def __init__(self):
        self.database = Gerenciador()
        self.database.criarTabela("sql/usuarios.sql")
        self.database.criarTabela("sql/postagens.sql")
        self.database.criarTabela("sql/curtidas.sql")
        self.database.criarTabela("sql/seguidores.sql")
       #self.database.criarTabela("sql/respostas.sql")

    def cadastrar(self,nome, login, senha):
        '''cadastra usuario se ele nao existir'''

        usuario = Usuario(nome,login)

        resp = self.database.inserirUsuario(usuario,senha)
        if resp == True:
            print("Usuario cadastrado!")
    def logar(self,login,senha):
        '''
            Faz uma busca no DB, pelo usuario e senha, e verifica se
            as duas informaçoes batem
        '''
        senhaRecebida = self.database.dadosLogin(login)

        if senhaRecebida == None:
            print("ERRO: login nao existe!")
            return False

        if(senha == senhaRecebida):
            return True

        return False

    def postar(self, login,text):
        self.database.inserirPostagem(login,texto)
    def timeline(self):
        return self.database.buscarPostagens()

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
        return True

    def verifica_id_usuario(self, login):
        sql = '''
            select id_usuario from usuarios where login=?;
        '''
        args = (login, )
        self.executeSQL(sql, args)
        resultados = self.cursor.fetchone()
        return resultados[0]

    def inserirPostagem(self,login,texto):
        id_usuario = self.verifica_id_usuario(login)
        sql = '''
                    insert into postagens
                    (id_usuario, texto, data_postagem)
                    values
                    (?, ?,datetime('now'))
                '''
        args = (texto, id_usuario)
        self.executeSQL(sql, args)

    def buscarPostagens(self):

        sql = '''
                select * from postagens;
            '''
        self.cursor.execute(sql)
        self.conexao.commit()
        ret = self.cursor.fetchall()
        ret_list = [(texto,data) for _,texto,_,data in ret]
        return ret_list

    def responder(self, usuario, id_postagem, texto):
        id_usuario = self.verifica_id_usuario(usuario)
        sql = '''
            insert into respostas
            (id_usuario, id_postagem, texto)
            values
            (?, ?, ?)
        '''
        args = (id_usuario, id_postagem, texto)
        self.executeSQL(sql, args)


    def inserirSeguidor(self,usuario_seguidor, usuario_seguido):
        id_usuario_seguidor = self.verifica_id_usuario(usuario_seguidor)
        id_usuario_seguido = self.verifica_id_usuario(usuario_seguido)

        sql = '''
                           insert into seguidores
                           (id_seguidor, id_seguido)
                           values
                           (?, ?);
                       '''
        args = (id_usuario_seguidor, id_usuario_seguido)
        self.executeSQL(sql, args)

    def inserirCurtida(self, user, id_postagem):
        id_usuario = self.verifica_id_usuario(user)
        sql = '''
                            insert into curtidas
                            (id_usuario, id_postagem)
                            values
                            (?, ?)
                 '''
        args = (id_usuario, id_postagem)
        self.executeSQL(sql, args)

    def dadosLogin(self,login):

        sql = '''
            select (senha) from usuarios where login=?;
        '''
        self.executeSQL(sql,(login,))
        ret = self.cursor.fetchone()
        if ret is not None:
            return ret[0]
        else:
            return None


    def executeSQL(self,cmd,args):

        self.cursor.execute(cmd,args)
        self.conexao.commit()


if __name__ == '__main__':
    RS = RedeSocial()
    RS.database.buscarPostagens()
