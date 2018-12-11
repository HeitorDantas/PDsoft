import sqlite3

conexao = sqlite3.connect("redesocial.db")
gerenciador = conexao.cursor()

#sql = 'create database if not exists redesocial.db;'
#gerenciador.execute(sql)

sql = '''
    create table if not exists usuario(
        id_usuario integer not null Primary key AUTOINCREMENT,
        nome varchar(20) not null,
        login varchar(20) not null,
        senha varchar(8) not null
    );
'''
gerenciador.execute(sql)

sql = '''
    create table if not exists postagem(
        id_postagem integer not null primary key AUTOINCREMENT,
        id_usuario int,
        texto text,
        data_postagem datetime,
        foreign key (id_usuario) references usuario(id_usuario)
    );
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


conexao.commit()
