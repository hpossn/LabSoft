from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader, RequestContext

# email imports
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from . forms import ContactForm

# Auth
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from . forms import UserForm

# experimental
from manage import escreverArq

def index(request):
    return render(request, 'home/index.html', {'form': UserForm,})

def login(request):
    if request.method == "POST":
        form = UserForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return render(request, 'home/base_template.html', {'form': UserForm, })
#                else:
#                    print user, 'desabilitado'
        else:
            logout(request)
            print user, 'nao existe'

    # return HttpResponseRedirect("index", {'invalid_login': True})
    messages.error(request, 'Log Invalido')
    return render(request, 'home/index.html', {'form': UserForm,})

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('index')

def about(request):
    return render(request, 'home/about.html', {})

def services(request):
    return render(request, 'home/works.html', {})

def contact(request):
    form_class = ContactForm

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
