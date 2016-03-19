from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader

def index(request):
   template = loader.get_template('home/index.html')
   return HttpResponse(template.render(request))

def base(request):
   template = loader.get_template('home/base_template.html')
   return HttpResponse(template.render(request))

def login(request):
   return render(request, 'home/base_templateLogin.html', {})
