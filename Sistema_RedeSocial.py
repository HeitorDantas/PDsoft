import pymysql

class RedeSocial:
    def __init__(self):
        self.conexao = pymysql.connect(
            user='root',
            host='localhost',
            password='',
            database='redesocial'
        )
        self.gerenciador = self.conexao.cursor()

    def cadastrar(self, login, senha):
        sql = '''
            insert into usuario
            (nome, login, senha)
            values
            (%s, %s);
        '''
        self.gerenciador.execute(sql,(login, senha))
        self.conexao.commit()
    def logar(self,login,senha):
        '''
            Faz uma busca no DB, pelo usuario e senha, e verifica se 
            as duas informaçoes batem
        '''
        sql = """
            select (login,senha) from usuario
            where login = '%s';
        """
        self.gerenciador.execute(sql,(login))
        self.conexao.commit()
#rs = RedeSocial()
#rs.cadastrar('pv', '123')

