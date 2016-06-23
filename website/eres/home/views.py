# -*- coding: utf-8 -*-
from __future__ import print_function
import hashlib

# general imports
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader, RequestContext
from django.utils.datastructures import MultiValueDictKeyError

# email imports
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.conf import settings
from . import forms

# Authentication
import django.contrib.auth as auth
from django.contrib import messages
from django.template.context_processors import csrf
from . models import *

# experimental
from GerenciadorEntregas  import *
from GerenciadorFuncionarios  import *

def index(request):
    if request.is_ajax():
        if request.method == 'POST':
            formRastr = forms.Rastreamento(data=request.POST)
            if formRastr.is_valid():
                try:
                    cod = formRastr.cleaned_data['codRastr']
                    entrega = rastrearEntrega(cod=cod)
                    response_data = {}
                    response_data['valido'] = 'true'
                    response_data['endereco'] = str(entrega.destinatario.logradouro + ', ' + entrega.destinatario.numero + ' - ' + entrega.destinatario.municipio + '/' + entrega.destinatario.estado)
                    response_data['status']  = entrega.status
                    response_data['dataPedido'] = entrega.dataPedido.strftime('%d/%m/%Y')
                except Exception as e:
                    response_data = {}
                    response_data['valido'] = 'false'
                    return JsonResponse(response_data)
                return JsonResponse(response_data)
    elif 'btn_enviar_cadastro' in request.POST:
        formSignup = forms.ClienteForm(data=request.POST)
        if formSignup.is_valid():
            # cria um novo usuario, ainda que ele nao venha a ser aceito pelo gerente
            newuser = models.Usuario(formSignup.cleaned_data['username'], tipoUsuario=models.tiposDeUsuario['cliente'])
            # pega um objeto cliente
            novocliente = formSignup.save(commit=False)
            # associa o novo usuario ao novo cliente
            novocliente.usuario = newuser
            # salva os dois no bd
            newuser.save()
            novocliente.save()
            # envia email
            email = EmailMessage(
                subject='Novo cadastro em ERES',
                body='Prezado novo cliente %s,\n\tAntes de poder usufruir de nossos serviços de logística, aguarde confirmação de cadastro e solicitação de nova senha de login.\nAtt,\nEquipe de SAC - ERES Ltda.'%formSignup.cleaned_data['nome'],
                from_email='sac@eres.com.br', to=[formSignup.cleaned_data['email']],
            )
            email.send()

    c = {}
    c.update(csrf(request))

    c['formRastr'] = forms.Rastreamento()
    c['formSignup'] = forms.ClienteForm()

    return render(request, 'home/index.html', c)

def login(request):
    if request.method == "POST":
            form = forms.CustomLoginForm(data=request.POST)
            if True:
                username = request.POST['username']

                password = request.POST['password']
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        auth.login(request, user)
                        tipo = getTipoUsuario(username)
                        if tipo == tiposDeUsuario['cliente']:
                            return HttpResponseRedirect('home0')
                        if tipo == tiposDeUsuario['gerente']:
                            return HttpResponseRedirect('home1')
                        if tipo == tiposDeUsuario['funcionario']:
                            return HttpResponseRedirect('home2')

    messages.error(request, 'Log Invalido')
    return render(request, 'home/index.html', {'form': forms.CustomLoginForm,})

# Cadastro de nova senha
def cadastroSenha(request, tipoUsuario, hashname):
    if request.method == "POST":
        formSenha = forms.CadastroSenhaForm(data=request.POST)
        if formSenha.is_valid():
            senha = formSenha.cleaned_data['senha']
            senha_verificacao = formSenha.cleaned_data['senha_verificacao']

            usuario = None
            if int(tipoUsuario) == models.tiposDeUsuario['cliente']:
                for cliente in models.Cliente.objects.all():
                    md5 = hashlib.md5(cliente.nome.encode('utf-8'))
                    if md5.hexdigest()[:5] == hashname:
                        usuario = cliente.usuario
                        # print(cliente)
            # elif int(tipoUsuario) == models.tiposDeUsuario['funcionario']:
            #     for funcionario in models.Funcionario.objects.all():
            #         md5 = hashlib.md5(funcionario.nome.encode('utf-8'))
            #         if md5.hexdigest()[:5] == hashname:
            #             usuario = funcionario.usuario

            if usuario is not None:
                if senha == senha_verificacao:
                    print('opa, senhas BATERAM')
                    usuario.password = senha
                    usuario.save()
                    return HttpResponseRedirect('/index')
                else:
                    print('ERRO nas senhas')

    formSenha = forms.CadastroSenhaForm()
    return render(request, 'home/cadastro/cadastroSenha.html', {'formSenha': formSenha})


#TODA A PARTE DO LOGIN
def home0(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
        tipo = getTipoUsuario(username)
        if tipo == tiposDeUsuario['cliente']:
            if request.method == 'POST':
                form = forms.ArquivoPedidosForm(request.POST, request.FILES)
                if form.is_valid():
                    adicionarListaPedidos(request.FILES['file'].read())
            else:
                form = forms.ArquivoPedidosForm()

            return render(request, 'home/clientes/upload.html', {'form': form})
        else:
            return HttpResponseRedirect('/index')

def home1(request):
    if request.user.is_authenticated():
        username = request.user.username
        tipo = getTipoUsuario(username)
        if tipo == tiposDeUsuario['gerente']:
            return render(request, 'home/gerente/user1.html')

    return HttpResponseRedirect('/index')

def home2(request):
    if request.user.is_authenticated():
        username = request.user.username
        tipo = getTipoUsuario(username)
        if tipo == tiposDeUsuario['funcionario']:
            return render(request, 'home/funcionarios/user2.html')
    return HttpResponseRedirect('/index')

def entregasAlocadas(request):

    def getIDEntregador(username):
        usuario = Usuario.objects.get(username=username)
        entregador = models.Entregador.objects.get(usuario=usuario)
        return entregador.CPF

    username = None
    if request.user.is_authenticated():
        username = request.user.username
        tipo = getTipoUsuario(username)
        idEntregador = getIDEntregador(username)
        if tipo == 2:
            result = models.Entrega.objects.all()
            if request.method == 'POST':
                formEntregaAlocada = forms.EntregasAlocadas(data=request.POST, idEntregador=idEntregador)

                if formEntregaAlocada.is_valid():
                    entrega = formEntregaAlocada.cleaned_data['entrega_select']
                    finalizarEntrega(
                        cod=entrega.codigoRastreamento, dataEntrega=datetime.now()
                        )
            result = listarPedidosAlocados(idEntregador)
            return render(request, 'home/funcionarios/entregasAlocadas.html', {'result': result, 'form': forms.EntregasAlocadas(idEntregador=idEntregador)})
    return HttpResponseRedirect('/index')

def trocarsenha(request):
    if request.user.is_authenticated():
        username = request.user.username
        tipo = getTipoUsuario(username)
        if tipo == models.tiposDeUsuario['funcionario']:
            if request.method == "POST":
                formSenha = forms.CadastroSenhaForm(data=request.POST)
                if formSenha.is_valid():
                    senha = formSenha.cleaned_data['senha']
                    senha_verificacao = formSenha.cleaned_data['senha_verificacao']

                    usuario = models.Usuario.objects.get(username=username)
                    if senha == senha_verificacao:
                        usuario.password = senha
                        usuario.save()
                        return HttpResponseRedirect('/home2')


    formSenha = forms.CadastroSenhaForm()
    return render(request, 'home/funcionarios/trocarsenha.html', {'formSenha': formSenha})

#GERENTE
def gerclientes(request):
    if request.user.is_authenticated():
        username = request.user.username
        gerente = models.Gerente.objects.filter(usuario__username=username)[0]
        tipo = getTipoUsuario(username)
        if tipo == tiposDeUsuario['gerente']:
            if request.method == 'POST':
                for cliente in Cliente.objects.filter(CNPJ__in=request.POST.getlist('aprovado')):
                    md5 = hashlib.md5(cliente.nome.encode('utf-8'))
                    template = get_template('email_para_cliente.txt')
                    context = {
                        'gerente_nome': gerente.nome,
                        'url_link': 'localhost:8000/cadastroSenha/{tipoUsuario}/{hashname}'.format(tipoUsuario=int(models.tiposDeUsuario['cliente']), hashname=md5.hexdigest()[:5]),
                    }
                    content = template.render(context)
                    EmailMessage(
                        subject='Cadastro em ERES aprovado',
                        body= content,
                        from_email='gerente@lar.com.br',
                        to=[cliente.email]
                    ).send()

                Cliente.objects.filter(CNPJ__in=request.POST.getlist('aprovado')).update(isNew=False)
            return render(request, 'home/gerente/clientes.html', {'clientes_pendentes': Cliente.objects.filter(isNew=True), 'clientes_aprovados': Cliente.objects.filter(isNew=False)})
    return HttpResponseRedirect('/index')

def gerfuncionarios(request):
    if request.is_ajax():
        if request.method == 'POST':
            formEntregador = forms.EntregadorForm(data=request.POST)

            if formEntregador.is_valid():

                try:
                    nome = formEntregador.cleaned_data['nome']
                    dataNasc = formEntregador.cleaned_data['dataNascimento']
                    salario = formEntregador.cleaned_data['salario']
                    cpf = formEntregador.cleaned_data['CPF']
                    veiculos = formEntregador.cleaned_data['veiculos']
                    username = request.POST.get('nomedeusuario', '')

                    try:
                        antigo = Entregador.objects.get(CPF=cpf)
                    except Exception as e:
                        antigo = None

                    if antigo is not None:
                        response_data = {'msg':"Funcionario com CPF " + cpf + ' já existe'}

                    else:
                        entregador = Entregador(nome=nome, dataNascimento=dataNasc, CPF=cpf, salario=salario, veiculos=veiculos)
                        try:
                            entregador.save()
                            usuario = models.Usuario(username=username, password=cpf, tipoUsuario=models.tiposDeUsuario['funcionario'])
                            usuario.save()
                            entregador.usuario = usuario
                            entregador.save()
                        except Exception as e:
                            print('deu erro na hora de salvar')
                            print(e)
                        response_data = {}
                        response_data['msg'] = 'entregador ' + nome + ' foi cadastrado com sucesso.'

                except Exception as e:
                    response_data = {}
                    response_data['msg'] = 'Problema no cadastro do entregador'
                    return JsonResponse(response_data)
                return JsonResponse(response_data)

    username = None
    if request.user.is_authenticated():
        username = request.user.username
        tipo = getTipoUsuario(username)
        if tipo == tiposDeUsuario['gerente']:
            form = forms.EntregadorForm()
            if request.method == 'POST':
                form = forms.EntregadorForm(data=request.POST)
            return render(request, 'home/gerente/user1-funcionarios.html', {'formFunc':form})
        return HttpResponseRedirect('/index')



def gerentregas(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
        tipo = getTipoUsuario(username)
        if tipo == tiposDeUsuario['gerente']:
            result = models.Entrega.objects.filter(status='pendente')
            if request.method == 'POST':
                formEntregaEntregador = forms.EntregaEntregadorForm(data=request.POST)
                if formEntregaEntregador.is_valid():
                    alocarEntregaParaEntregador(
                        entrega=formEntregaEntregador.cleaned_data['entrega_select'],
                        entregador=formEntregaEntregador.cleaned_data['entregador_select']
                        )
            return render(request, 'home/gerente/alocarEntregaParaEntregador.html', {'result': result, 'form': forms.EntregaEntregadorForm()})
    return HttpResponseRedirect('/index')



def gerregioes(request):
    if request.is_ajax():
        if request.method == 'POST':
            formRegiao = forms.RegiaoForm(data=request.POST)
            if formRegiao.is_valid():
                try:
                    nomeRegiao = formRegiao.cleaned_data['nome']
                    valorPrecoBase = formRegiao.cleaned_data['precoBase']

                    try:
                        antigo = Regiao.objects.get(nome=nomeRegiao)
                    except Exception as e:
                        antigo = None

                    if antigo is not None:
                        antigo.precoBase = valorPrecoBase
                        antigo.save()
                        response_data = {'msg': "Preco base da região " + nomeRegiao + ' atualizado'}
                    else:
                        regiao = Regiao(nome=nomeRegiao, precoBase=valorPrecoBase)
                        regiao.save()
                        response_data = {}
                        response_data['msg'] = 'A região ' + nomeRegiao + ' foi cadastrada com sucesso.'
                except Exception as e:
                    response_data = {}
                    response_data['msg'] = 'Problema no cadastro da regiao'
                    return JsonResponse(response_data)
                return JsonResponse(response_data)

    if request.user.is_authenticated():
        username = request.user.username
        tipo = getTipoUsuario(username)
        if tipo == tiposDeUsuario['gerente']:
            form = forms.RegiaoForm()
            if request.method == 'POST':
                form = forms.RegiaoForm(data=request.POST)
            return render(request, 'home/gerente/user1-regiao.html', {'form':form})
        return HttpResponseRedirect('/index')



def gerveiculos(request):
    if request.is_ajax():
        if request.method == 'POST':
            formVeiculo = forms.VeiculoForm(data=request.POST)
            if formVeiculo.is_valid():
                try:
                    marcaVeiculo = formVeiculo.cleaned_data['marca']
                    modeloVeiculo = formVeiculo.cleaned_data['modelo']
                    anoVeiculo = formVeiculo.cleaned_data['ano']
                    placaVeiculo = formVeiculo.cleaned_data['placa']
                    antigo = None

                    try:
                        antigo = Veiculo.objects.get(placa=placaVeiculo)
                    except Exception as e:
                        antigo = None
                        print(type(e))
                        print(e.args)
                        print(e)
                        response_data = {}
                        response_data['msg'] = 'Veículo com placa ' + placaVeiculo + ' teve problema no cadastro'

                    if antigo != None:
                        response_data = {}
                        response_data['msg'] = 'Veículo com placa ' + placaVeiculo + ' já existe'
                    else:
                        veiculo = Veiculo(marca=marcaVeiculo, modelo=modeloVeiculo, ano=anoVeiculo, placa=placaVeiculo)
                        veiculo.save()
                        response_data = {}
                        response_data['msg'] = marcaVeiculo + ' ' + modeloVeiculo + ' foi cadastrada com sucesso.'
                except Exception as e:
                    response_data = {}
                    response_data['msg'] = 'Problema no cadastro do veiculo'
                    return JsonResponse(response_data)
                return JsonResponse(response_data)

    username = None
    if request.user.is_authenticated():
        username = request.user.username
        tipo = getTipoUsuario(username)
        if tipo == tiposDeUsuario['gerente']:
            form = forms.VeiculoForm()
            if request.method == 'POST':
                form = forms.RegiaoForm(data=request.POST)
            return render(request, 'home/gerente/user1-veiculos.html', {'form':form})
        return HttpResponseRedirect('/index')

def getTipoUsuario(username):
    usuario = Usuario.objects.get(username=username)
    return usuario.tipoUsuario

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index')

def about(request):
    return render(request, 'home/about.html', {'formSignup': forms.ClienteForm()})

def services(request):
    return render(request, 'home/works.html', {'formSignup': forms.ClienteForm()})

def customers (request):
    return render(request, 'home/customers.html', {'formSignup': forms.ClienteForm()})

def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                    'contact_name',
                    ''
            )
            contact_email = request.POST.get(
                    'contact_email',
                    ''
            )
            form_content = request.POST.get(
                    'content',
                    ''
            )

            # Email the profile with the contact information
            template = get_template('contact_template.txt')
            context = Context({
                    'contact_name': contact_name,
                    'contact_email': contact_email,
                    'form_content': form_content,
            })

            content = template.render(context)

            email = EmailMessage(
                    "New contact submission",
                    content,
                    settings.DEFAULT_FROM_EMAIL, ['sac@eres.com.br'],
                    headers = {'Reply-To': contact_email}
            )
            email.send()
            return redirect('contact')

    return render(request, 'home/contact.html', {'form': forms.ContactForm, 'formSignup': forms.ClienteForm()})

def signup(request):
    if request.method == 'POST':
        form = forms.ClienteForm(data=request.POST)
        if form.is_valid():
            cli = form.save()

    return render(request, 'home/cadastro/cliente.html', {'form':  forms.ClienteForm()})

def funcionario(request):
    if request.method == 'POST':
        form = forms.EntregadorForm(data=request.POST)
        if form.is_valid():
            func = form.save()

    return render(request, 'home/cadastro/entregador.html', {'form':  forms.EntregadorForm()})

def veiculo(request):
    if request.method == 'POST':
        form = forms.VeiculoForm(data=request.POST)
        if form.is_valid():
            vei = form.save(commit=False)
    else:
        form = forms.VeiculoForm()

    return render(request, 'home/cadastro/funcionario.html', {'form': form})

def regiao(request):
    if request.method == 'POST':
        form = forms.RegiaoForm(data=request.POST)
        if form.is_valid():
            vei = form.save()
    form = forms.RegiaoForm()

    return render(request, 'home/cadastro/regiao.html', {'form': form})


def displayEntregas(request):
    result = models.Entrega.objects.all()
    return render(request, 'home/displayEntregas.html', {'result': result})
