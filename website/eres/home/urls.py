from django.conf.urls import url

from . import views

urlpatterns = [
    # View inicial
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),

    # Authentication
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    # nav bar
    url(r'^about$', views.about, name='about'),
    url(r'^works$', views.services, name='services'),

    # Contact form
    url(r'^contact$', views.contact, name='contact'),

    # Cadastro de cliente
    url(r'^signup$', views.signup, name='signup'),

    # Upload de XML com pedidos de entrega
    url(r'^upload$', views.upload_pedidos, name='upload'),
]
