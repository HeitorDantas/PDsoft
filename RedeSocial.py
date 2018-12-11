import pymysql

conexao = pymysql.connect(
    user = 'root',
    host = 'localhost',
    password = '',
    #database = 'redesocial',
)
gerenciador = conexao.cursor()

sql = 'create database if not exists redesocial;'
gerenciador.execute(sql)

conexao.connect(database='redesocial')

sql = '''
    create table if not exists usuario(
        id_usuario int not null auto_increment,
        nome varchar(20) not null, 
        login varchar(20) not null,
        senha varchar(8) not null,
        primary key (id_usuario)
    )auto_increment=1;
'''
gerenciador.execute(sql)

sql = '''
    create table if not exists postagem(
        id_postagem int not null auto_increment,
        id_usuario int,
        texto text,
        data_postagem datetime,
        primary key(id_postagem),
        foreign key (id_usuario) references usuario(id_usuario)
    )auto_increment=1;
'''
gerenciador.execute(sql)

sql = '''
    create table if not exists curtidas(
        id_usuario int,
        id_postagem int,
        primary key(id_usuario, id_postagem),
        foreign key(id_usuario) references usuario(id_usuario),
        foreign key(id_postagem) references postagem(id_postagem) 
    );
'''

gerenciador.execute(sql)

sql = '''
    create table if not exists seguidores(
        id_seguidor int,
        id_seguido int,
        primary key(id_seguidor, id_seguido),
        foreign key(id_seguidor) references usuario(id_usuario),
        foreign key(id_seguido) references usuario(id_usuario)
    );
'''

gerenciador.execute(sql)









