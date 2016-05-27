from django.conf.urls import url
from django.http import HttpResponseRedirect


from . import views

urlpatterns = [
    # View inicial
    url(r'^$', lambda request: HttpResponseRedirect('index'), name='index'), # xD
    url(r'^index$', views.index, name='index'),

    # Authentication
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),

    # nav bar
    url(r'^about$', views.about, name='about'),
    url(r'^works$', views.services, name='services'),
    url(r'^customers$', views.customers, name='customers'),

    # Contact form
    url(r'^contact$', views.contact, name='contact'),

    # Cadastro de cliente
    url(r'^signup$', views.signup, name='signup'),
    # Cadastro de funcionario
    url(r'^funcionario$', views.funcionario, name='funcionario'),

    # Upload de XML com pedidos de entrega
    url(r'^upload$', views.upload_pedidos, name='upload'),

    #
    url(r'^displayEntregas$', views.displayEntregas, name='displayEntregas'),

    url(r'^veiculo$', views.veiculo, name='veiculo'),
    url(r'^alocar$', views.alocar, name='alocar'),


    #Homes Usuarios
    url(r'^home0$', views.home0, name='home0'),
    url(r'^home1$', views.home1, name='home1'),
    url(r'^home2$', views.home2, name='home2'),

    #Gerente
    url(r'^gerclientes$', views.gerclientes, name='gerclientes'),
    url(r'^gerfuncionarios$', views.gerfuncionarios, name='gerfuncionarios'),
    url(r'^gerentregas$', views.gerentregas, name='gerentregas'),
    url(r'^gerregioes$', views.gerregioes, name='gerregioes'),
    url(r'^gerveiculos$', views.gerveiculos, name='gerveiculos'),
]
