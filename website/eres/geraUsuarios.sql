use eres;

show tables;

select * from home_usuario;

insert into home_usuario
(username, password, tipoUsuario) values ('gerente', '123', 0);

insert into home_usuario
(username, password, tipoUsuario) values ('entregador', '123', 1);


insert into home_usuario
(username, password, tipoUsuario) values ('cliente', '123', 2);