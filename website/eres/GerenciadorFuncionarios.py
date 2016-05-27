# -*- coding: utf-8 -*-
from __future__ import print_function
import home.models as models

def alocarEntregaParaEntregador(entrega, entregador):
    if entrega.entregador is None:
        entregador.status = 1
        entregador.save()
        entrega.entregador = entregador
        entrega.save()
    else:
        print('entrega já tem entregador responsável por realizá-la')


def liberarEntregadorDeEntrega(entregador):
    entregador.status = 0
    entregador.save()

def listarEntregadoresDisponiveis():
    return models.Entregador.objects.filter(status=0)
