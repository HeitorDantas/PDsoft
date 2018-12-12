create table if not exists curtidas(
      id_usuario int,
      id_postagem int,
      primary key(id_usuario, id_postagem),
      foreign key(id_usuario) references usuario(id_usuario),
      foreign key(id_postagem) references postagem(id_postagem)
  );
