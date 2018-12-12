create table if not exists postagens(
      id_postagem integer not null primary key AUTOINCREMENT,
      id_usuario int,
      texto text,
      data_postagem datetime,
      foreign key (id_usuario) references usuario(id_usuario)
  );
