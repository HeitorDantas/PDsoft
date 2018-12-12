import sqlite3
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

        self.database.inserirUsuario(usuario,senha)

    def logar(self,login,senha):
        '''
            Faz uma busca no DB, pelo usuario e senha, e verifica se
            as duas informaçoes batem
        '''
        sql = """
            select (login) from usuario
            where login=%s and senha=%s;
        """

        args = (login,senha)
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
            insert into usuarios (nome,login,senha) values (%s,%s,%s);
        '''
        self.executeSQL(sql,args)
    def verifica_id_usuario(self, login):
        sql = '''
            select id_usuario from usuario where login = %s;
        '''
        args = (login, )
        self.executeSQL(sql, args)
        resultados = self.cursor.fetchone()
        return resultados[0]
    def inserirPostagem(self,user,texto):
        id_usuario = self.verifica_id_usuario(user)
        sql = '''
                    insert into postagem
                    (id_usuario, texto, data_postagem)
                    values
                    (%d, now(), %s)
                '''
        args = (texto, id_usuario)
        self.executeSQL(sql, args)

    def responder(self, usuario, id_postagem, texto):
        id_usuario = self.verifica_id_usuario(usuario)
        sql = '''
            insert into respostas
            (id_usuario, id_postagem, texto)
            values
            (%d, %d, %s)
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
                           (%d, %d)
                       '''
        args = (id_usuario_seguidor, id_usuario_seguido)
        self.executeSQL(sql, args)

    def inserirCurtida(self, user, id_postagem):
        id_usuario = self.verifica_id_usuario(user)
        sql = '''
                            insert into curtidas
                            (id_usuario, id_postagem)
                            values
                            (%d, %d)
                 '''
        args = (id_usuario, id_postagem)
        self.executeSQL(sql, args)

    def dadosLogin(self,login):

        sql = '''
            select  from usuarios where login=;
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
