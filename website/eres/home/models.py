# -*- coding: utf-8 -*-
from django.db import models
__all__ = ['Usuario', 'Entrega', 'Destinatario']

class Usuario(models.Model):
    username = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=15)
    tipoUsuario = models.IntegerField()


class Regiao(models.Model):
    nome = models.CharField(max_length=45)
    precoBase = models.FloatField()
    def __str__(self):
        return self.nome
    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'Regioes'


class Destinatario(models.Model):
    # identificação
    nome = models.CharField(max_length=256)
    # endereço
    logradouro = models.CharField(max_length=45)
    numero = models.CharField(max_length=4)
    complemento = models.CharField(max_length=45, blank=True, null=True)
    municipio = models.CharField(max_length=45)
    estado = models.CharField(max_length=2)
    class Meta:
        ordering = ['nome']


class Recibo(models.Model):
    assinatura = models.CharField(max_length=45)
    dataRecebimento = models.DateField()
    def __str__(self):
        return 'id:{id} {dataRecebimento}'.format(id=self.id, dataRecebimento=self.dataRecebimento)
    class Meta:
        ordering=['dataRecebimento']


class Funcionario(models.Model):
    nome = models.CharField(max_length=45)
    dataNascimento = models.DateField()
    CPF = models.CharField(max_length=45)
    salario = models.FloatField()
    def __str__(self):
        return self.nome
    class Meta:
        ordering = ['nome']

class Gerente(Funcionario):
    pass


class Entregador(Funcionario):
    status = models.IntegerField(blank=True, null=True)
    veiculos = models.ManyToManyField('Veiculo', verbose_name='Veiculos que esta autorizado a usar', related_name='entregadores')
    class Meta:
        verbose_name_plural = 'Entregadores'


class Cliente(models.Model):
    nome = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    endereco = models.CharField(max_length=45)
    telefone = models.CharField(max_length=20)
    CNPJ = models.CharField(max_length=45)
    def __str__(self):
        return self.nome


class Entrega(models.Model):
    # Fields necessários
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    destinatario = models.ForeignKey(Destinatario, on_delete=models.CASCADE)
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE)
    dataPedido = models.DateField()
    prioridade = models.CharField(max_length=10)
    # Fields a serem preenchidos conforme evolução do pedido de entrega
    status = models.CharField(max_length=45)
    dataEntrega = models.DateField(blank=True, null=True)
    qtd_tentativas = models.IntegerField()
    recibo = models.ForeignKey(Recibo, on_delete=models.CASCADE, blank=True, null=True)
    entregador = models.ForeignKey(Entregador, on_delete=models.CASCADE, blank=True, null=True)
    # Field preenchido automaticamente
    preco = models.FloatField()


class Veiculo(models.Model):
    # entregador = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    marca = models.CharField(max_length=45)
    modelo = models.CharField(max_length=45)
    ano = models.CharField(max_length=4)
    placa = models.CharField(max_length=8)
    def __str__(self):
        return '{marca} {modelo} {placa}'.format(marca=self.marca, modelo=self.modelo, placa=self.placa)
