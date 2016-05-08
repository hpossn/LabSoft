from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^base$', views.base, name='base'),
    url(r'^login', views.login, name='login'),
    url(r'^about', views.about, name='about'),
    url(r'^works', views.services, name='services'),
    # Contact form
    url(r'^contact', views.contact, name='contact'),
]
