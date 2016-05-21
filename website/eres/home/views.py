from __future__ import print_function

# general imports
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader, RequestContext

# email imports
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from . import forms

# Authentication
import django.contrib.auth as auth
from django.contrib import messages
from django.template.context_processors import csrf
from . models import *

# experimental
from GerenciadorEntregas  import *

def index(request):
    if request.is_ajax():
        if request.method == 'POST':
            formRastr = forms.Rastreamento(data=request.POST)
            if formRastr.is_valid():
                #print('eh valido')
                try:
#                   entrega = rastrearEntrega(cod= request.POST['codigo'])
                    cod = formRastr.cleaned_data['codRastr']
                    #print('cod', cod)
                    entrega = rastrearEntrega(cod=cod)
                    #print(entrega.destinatario.nome)
                    response_data =  {'endereco': str(entrega.destinatario.logradouro + ', ' + entrega.destinatario.numero + ' - ' + entrega.destinatario.municipio + '/' + entrega.destinatario.estado)}
                    response_data['status']  = entrega.status
                    response_data['dataPedido'] = entrega.dataPedido.strftime('%d/%m/%Y')
                except Exception as e:
                    return JsonResponse({})
                return JsonResponse(response_data)

    c = {}
    c.update(csrf(request))

    c['formRastr'] = forms.Rastreamento()

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
                    return render(request, 'home/base_template.html', {'funcao_usuario': getTipoUsuario(user.username)})
#                else:
#                    print user, 'desabilitado'
        else:
            print('nao existe')

    # return HttpResponseRedirect("index", {'invalid_login': True})
    messages.error(request, 'Log Invalido')
    return render(request, 'home/index.html', {'form': forms.CustomLoginForm,})

def getTipoUsuario(username):
    usuario = Usuario.objects.get(username=username)
    return usuario.tipoUsuario

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('index')

def about(request):
    return render(request, 'home/about.html', {})

def services(request):
    return render(request, 'home/works.html', {})

def customers (request):
    return render(request, 'home/customers.html', {})

def contact(request):
    form_class = forms.ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

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

            escreverArq(content)

            email = EmailMessage(
                    "New contact form submission",
                    content,
                    "Your website" + ' ', ['sac@eres.com.br'],
                    headers = {'Reply-To': contact_email}
            )
            email.send()
            return redirect('contact')

    return render(request, 'home/contact.html', {'form': form_class,})

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

def upload_pedidos(request):
    if request.method == 'POST':
        form = forms.ArquivoPedidosForm(request.POST, request.FILES)
        if form.is_valid():
            adicionarListaPedidos(request.FILES['file'].read())
    else:
        form = forms.ArquivoPedidosForm()

    return render(request, 'home/upload.html', {'form': form})

def veiculo(request):
    if request.method == 'POST':
        form = forms.VeiculoForm(data=request.POST)
        if form.is_valid():
            vei = form.save(commit=False)
            print(type(vei))
    else:
        form = forms.VeiculoForm()

    return render(request, 'home/cadastro/funcionario.html', {'form': form})

def displayEntregas(request):
    result = listarPedidosPendentes()
    return render(request, 'home/displayEntregas.html', {'result': result})
