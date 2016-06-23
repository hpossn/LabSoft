import django
django.setup()
import getpass
from datetime import datetime
import home.models as models

def cadastrarGerente():
    nome = input('nome: ')
    dataNascimento = input('data de nascimento [dd/mm/aaaa]: ')
    CPF = input('CPF: ')
    salario = input('salario: ')

    gerente = models.Gerente(nome=nome, dataNascimento=datetime.strptime(dataNascimento, '%d/%m/%Y'), CPF=CPF, salario=float(salario))
    try:
        gerente.save()
        username = input('username: ')
        senha = getpass.getpass('senha: ')
        senha_verificacao = getpass.getpass('digite a senha novamente: ')
        while senha != senha_verificacao:
            senha = getpass.getpass('senha: ')
            senha_verificacao = getpass.getpass('digite a senha novamente: ')
        user = models.Usuario(username=username, password=senha, tipoUsuario=models.tiposDeUsuario['gerente'])
        gerente.usuario = user
        user.save()
        gerente.save()
    except Exception as e:
        print('nao foi possivel cadastrar novo gerente:', e)
        return

    print('Gerente cadastrado com sucesso!')
