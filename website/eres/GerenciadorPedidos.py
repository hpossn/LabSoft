from xmltodict import parse
from home.models import Entrega


def adicionarListaPedidos(xml_input):
    """
    Recebe um arquivo XML contenedor de diversos pedidos de entrega. Armazena tais pedidos na lista de pedidos pendentes no banco de dados.
    """
    doc = parse(xml_input)

    for entrega in doc['pedidos']['body']:
        kw = {key: doc['pedidos']['body'][entrega][key] for key in doc['pedidos']['body'][entrega].keys()}
        e = Entrega(**kw)
        return e

#	cliente = None
#	entregador = None
#	destinatario = None
#	recibo = None
#	regiao = None
#	dataPedido = None
#	preco = None
#	prioridade = None
#	status = None
#	qtd_tentativas = None
