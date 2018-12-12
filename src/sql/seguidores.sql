create table if not exists seguidores(
      id_seguidor int,
      id_seguido int,
      primary key(id_seguidor, id_seguido),
      foreign key(id_seguidor) references usuario(id_usuario),
      foreign key(id_seguido) references usuario(id_usuario)
  );
