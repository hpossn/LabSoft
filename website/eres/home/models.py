from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(models.Model):
	username = models.CharField(max_length=15, primary_key=True)
	password = models.CharField(max_length=15)
	tipoUsuario = models.IntegerField()

class Regiao(models.Model):
#	id_regiao = models.IntegerField(primary_key=True)
	nome = models.CharField(max_length=45)
	precoBase = models.FloatField()

class Destinatario(models.Model):
#	id_destinatario = models.IntegerField(primary_key=True)
	nome = models.CharField(max_length=45)
	endereco = models.CharField(max_length=45)

class Recibo(models.Model):
#	id_recibo = models.IntegerField(primary_key=True)
	assinatura = models.CharField(max_length=45)
	dataRecebimento = models.DateField()

class Funcionario(models.Model):
#	id_funcionario = models.IntegerField(primary_key=True)
	nome = models.CharField(max_length=45)
	dataNascimento = models.DateField()
	CPF = models.CharField(max_length=45)
	salario = models.FloatField()

class Gerente(Funcionario):
	pass

class Entregador(Funcionario):
	status = models.IntegerField()

class Cliente(models.Model):
#	id_cliente = models.IntegerField(primary_key=True)
	nome = models.CharField(max_length=45)
	email = models.EmailField(max_length=45)
	endereco = models.CharField(max_length=45)
	telefone = models.CharField(max_length=20)
	CNPJ = models.CharField(max_length=45)

class Entrega(models.Model):
#	id_entrega = models.IntegerField(primary_key=True)
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	entregador = models.ForeignKey(Entregador, on_delete=models.CASCADE)
	destinatario = models.ForeignKey(Destinatario, on_delete=models.CASCADE)
	recibo = models.ForeignKey(Recibo, on_delete=models.CASCADE)
	regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE)
	dataPedido = models.DateField()
	preco = models.FloatField()
	prioridade = models.IntegerField()
	status = models.CharField(max_length=45)
	qtd_tentativas = models.IntegerField()

class Veiculo(models.Model):
#	id_veiculo = models.IntegerField(primary_key=True)
	entregador = models.ForeignKey(Entregador, on_delete=models.CASCADE)
	nome = models.CharField(max_length=45)
