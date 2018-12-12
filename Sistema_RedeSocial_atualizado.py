import mysql.connector

class Sistema_RedeSocial:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            user='root',
            host='localhost',
            password='',
            database='redesocial'
        )
        self.gerenciador = self.conexao.cursor()

    def cadastrar(self, login, senha):
        sql = '''
            insert into usuario
            (login, senha)
            values
            (%s, %s);
        '''
        self.gerenciador.execute(sql,(login, senha))
        self.conexao.commit()
    def logar(self, login, senha):
        '''
            Faz uma busca no DB, pelo usuario e senha, e verifica se 
            as duas informaçoes batem
        '''
        sql = """
            select login, senha from usuario 
            where login = %s and senha = %s;
        """
        self.gerenciador.execute(sql,(login, senha))
        self.conexao.commit()
    def verifica_id_usuario(self, login):
        sql = '''
            select id_usuario from usuario where login = %s;
        '''
        self.gerenciador.execute(sql, (login, ))
        resultados = self.gerenciador.fetchone()
        return resultados[0]

    def postar(self, usuario, texto):
        id_usuario = self.verifica_id_usuario(usuario)
        sql = '''
            insert into postagem
            (id_usuario, texto, data_postagem)
            values
            (%d, now(), %s)
        '''
        self.gerenciador.execute(sql,(texto, id_usuario))
        self.conexao.commit()
    def responder(self, usuario, id_postagem, texto):
        id_usuario = self.verifica_id_usuario(usuario)
        sql = '''
            insert into respostas
            (id_usuario, id_postagem, texto)
            values
            (%d, %d, %s)
        '''
        self.gerenciador.execute(sql,(id_usuario, id_postagem, texto))
        self.conexao.commit()

    def seguir(self, usuario_seguidor, usuario_seguido):
        id_usuario_seguidor = self.verifica_id_usuario(usuario_seguidor)
        id_usuario_seguido = self.verifica_id_usuario(usuario_seguido)

        sql = '''
                    insert into seguidores
                    (id_seguidor, id_seguido)
                    values
                    (%d, %d)
                '''
        self.gerenciador.execute(sql,(id_usuario_seguidor,id_usuario_seguido))
        self.conexao.commit()

    def curtir(self, usuario, id_postagem):
        id_usuario = self.verifica_id_usuario(usuario)
        sql = '''
                    insert into curtidas
                    (id_usuario, id_postagem)
                    values
                    (%d, %d)
         '''
        self.gerenciador.execute(sql, (id_usuario_seguidor, ))
        self.conexao.commit()


    #def responder(self, ):
#rs = RedeSocial()
#rs.cadastrar('pv', '123')

