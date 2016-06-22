# import django
# django.setup()
import getpass
from datetime import datetime
from django.contrib.auth.models import User
import models

def cadastrarGerente():
    nome = input('nome: ')
    dataNascimento = input('data de nascimento [dd/mm/aaaa]: ')
    CPF = input('CPF: ')
    salario = input('salario: ')

    gerente = models.Gerente(nome=nome, dataNascimento=datetime(dataNascimento, '%d/%m/%Y'), CPF=CPF, salario=float(salario))
    print(gerente.nome, gerente.dataNascimento)
