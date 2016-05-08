from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader
# email imports
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

def index(request):
   template = loader.get_template('home/index.html')
   return HttpResponse(template.render(request))

def base(request):
   template = loader.get_template('home/base_template.html')
   return HttpResponse(template.render(request))

def login(request):
   return render(request, 'home/base_templateLogin.html', {})

def about(request):
    return render(request, 'home/about.html', {})

def services(request):
    return render(request, 'home/works.html', {})

from . forms import ContactForm
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
            print 'oi', content, 'oi'

            email = EmailMessage(
                    "New contact form submission",
                    content,
                    "Your website" + ' ', ['sac@eres.com.br'],
                    headers = {'Reply-To': contact_email}
            )
            email.send()
            return redirect('contact')

    return render(request, 'home/contact.html', {'form': form_class,})
