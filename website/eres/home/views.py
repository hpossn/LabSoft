from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader, RequestContext

# email imports
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from . import forms
# Auth
import django.contrib.auth as auth
from django.contrib import messages
#from django.views.decorators.csrf import csrf_protect
from django.template.context_processors import csrf
#from django.contrib.auth.forms import AuthenticationForm

# experimental
from manage import escreverArq

def index(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'home/index.html', c)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return render(request, 'home/base_template.html')
#                else:
#                    print user, 'desabilitado'
        else:
            print user, 'nao existe'

    # return HttpResponseRedirect("index", {'invalid_login': True})
    messages.error(request, 'Log Invalido')
    return render(request, 'home/index.html', {'form': AuthenticationForm,})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('index')

def about(request):
    return render(request, 'home/about.html', {})

def services(request):
    return render(request, 'home/works.html', {})

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
        form = forms.FuncionarioForm(data=request.POST)
    else:
        form = forms.FuncionarioForm()

    return render(request, 'home/cadastro/funcionario.html', {'form': form})

def upload_pedidos(request):
    if request.method == 'POST':
        form = forms.ArquivoPedidosForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES['file'].read())
    else:
        form = forms.ArquivoPedidosForm()

    return render(request, 'home/upload.html', {'form': form})
