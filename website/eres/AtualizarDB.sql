use eres;
-- create database eres;

delete from home_usuario;
delete from home_entrega;
delete from home_destinatario;
delete from home_entregador;
delete from home_funcionario;
delete from home_regiao;
delete from home_cliente;


insert into home_usuario (username, password, tipoUsuario, cpf) values ('gerente', '123', 1, '123');
insert into home_usuario (username, password, tipoUsuario, cpf) values ('juca', '123', 2, '6678');
insert into home_usuario (username, password, tipoUsuario, cpf) values ('entregador2', '123', 2, '123');
insert into home_usuario (username, password, tipoUsuario, cpf) values ('cliente', '123', 0, '123');
insert into home_usuario (username, password, tipoUsuario, cpf) values ('LAR', '123', 0, '111');


-- insert into home_destinatario (nome, logradouro, numero, complemento, municipio, estado) values ('Hugo', 'Rua 1', 125, '', 'São Paulo', 'SP');
-- insert into home_destinatario (nome, logradouro, numero, complemento, municipio, estado) values ('Jose', 'Avenida Alves', 2, 'Ap1', 'São Paulo', 'SP');
-- insert into home_destinatario (nome, logradouro, numero, complemento, municipio, estado) values ('Casarin', 'Avenida Python', 32, 'Ap 47', 'Jundiaí', 'SP');
-- insert into home_destinatario (nome, logradouro, numero, complemento, municipio, estado) values ('Rafael', 'Rua do lago', 4, 'Ap56', 'Goiânia', 'GO');

insert into home_funcionario (nome, dataNascimento, CPF, salario) values ('João', '1980-12-21', '000', 2500);
insert into home_funcionario (nome, dataNascimento, CPF, salario) values ('Luís', '1985-04-11', '000', 2800);
insert into home_funcionario (nome, dataNascimento, CPF, salario) values ('Alberto', '1990-05-12', '000', 4500);

insert into home_regiao (nome, precoBase) values ('Lapa', 23);
insert into home_regiao (nome, precoBase) values ('Pinheiros', 12);
insert into home_regiao (nome, precoBase) values ('oeste', 2);

insert into home_cliente (nome, email, endereco, telefone, cnpj) values ('LAR', 'lar@lar.com.br', 'Rua do Lar 1', '2123-8961', '000');

select * from home_usuario;
select * from home_destinatario;
select * from home_entregador;
select * from home_funcionario;
select * from home_regiao;
select * from home_entrega;
select * from home_cliente;

show tables;