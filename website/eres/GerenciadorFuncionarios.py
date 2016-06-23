# -*- coding: utf-8 -*-
from __future__ import print_function
import home.models as models

def alocarEntregaParaEntregador(entrega, entregador):
    if entrega.entregador is None:
        # seta entregador como ocupado
        entregador.status = 1

        # altera o status da entrega para em transito
        entrega.status = 'em_transito'

        # faz a alocação propriamente dita
        entrega.entregador = entregador

        # salva no banco de dados todas as alterações
        entregador.save()
        entrega.save()
    else:
        print('entrega já tem entregador responsável por realizá-la')


def liberarEntregadorDeEntrega(entregador):
    entregador.status = 0
    entregador.save()

def listarEntregadoresDisponiveis():
    return models.Entregador.objects.filter(status=0)

def listarVeiculosDisponiveis():
    return models.Veiculo.objects.all()
