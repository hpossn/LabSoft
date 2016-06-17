# -*- coding: utf-8 -*-
import hashlib
from django.db import models


tiposDeUsuario = {
    'cliente': 0,
    'gerente': 1,
    'funcionario': 2,
}


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
    # identificacao
    nome = models.CharField(max_length=256, default='')
    # endereco
    logradouro = models.CharField(max_length=45, default='')
    numero = models.CharField(max_length=4, default='')
    complemento = models.CharField(max_length=45, blank=True, null=True)
    municipio = models.CharField(max_length=45, default='')
    estado = models.CharField(max_length=2, default='')
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
    CPF = models.CharField(max_length=45, primary_key=True)
    salario = models.FloatField()
    def __str__(self):
        return self.nome
    class Meta:
        ordering = ['nome']

class Gerente(Funcionario):
    pass


class Entregador(Funcionario):
    status = models.IntegerField(default=0)
    veiculos = models.ManyToManyField('Veiculo', verbose_name='Veiculos que esta autorizado a usar', related_name='entregadores')
    class Meta:
        verbose_name_plural = 'Entregadores'


class Cliente(models.Model):
    nome = models.CharField(max_length=45, default='')
    email = models.EmailField(max_length=45, default='')
    endereco = models.CharField(max_length=45, default='')
    telefone = models.CharField(max_length=20, default='')
    CNPJ = models.CharField(max_length=45, default='', primary_key=True)
    isNew = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Entrega(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    destinatario = models.ForeignKey(Destinatario, on_delete=models.CASCADE)
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE)
    dataPedido = models.DateField()
    prioridade = models.CharField(max_length=10)
    # Fields a serem preenchidos conforme evolucaoo do pedido de entrega
    status = models.CharField(max_length=45, default='pendente')
    dataEntrega = models.DateField(blank=True, null=True)
    qtd_tentativas = models.IntegerField()
    recibo = models.ForeignKey(Recibo, on_delete=models.CASCADE, blank=True, null=True)
    entregador = models.ForeignKey(Entregador, on_delete=models.CASCADE, blank=True, null=True)
    codigoRastreamento = models.CharField(max_length=8, default='')
    # Field preenchido automaticamente
    preco = models.FloatField()

    def gerarCodigoRastreamento(self):
        stringCode = self.cliente.nome + self.cliente.CNPJ  + str(self.preco) + str(self.dataPedido) + self.destinatario.nome
        stringCode = stringCode.encode()
        md5 = hashlib.md5(stringCode)
        self.codigoRastreamento = md5.hexdigest()[:8]

    def __str__(self):
        return 'cod: %s'%self.codigoRastreamento

class Veiculo(models.Model):
    # entregador = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    marca = models.CharField(max_length=45, default='')
    modelo = models.CharField(max_length=45, default='')
    ano = models.CharField(max_length=4, default='0000')
    placa = models.CharField(max_length=8, default='AAA-0000')
    def __str__(self):
        return '{marca} {modelo} {placa}'.format(marca=self.marca, modelo=self.modelo, placa=self.placa)
