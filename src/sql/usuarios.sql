CREATE TABLE if not exists usuarios(
      id_usuario INTEGER not null Primary key AUTOINCREMENT,
      nome varchar(20) not null,
      login varchar(20) not null,
      senha varchar(8) not null
  );
