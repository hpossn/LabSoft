# -*- coding: utf-8 -*-
from __future__ import print_function
import heapq as hp
from datetime import datetime
from xmltodict import parse
import home.models as models

codigoPrioridade = {
        'Alta': 0,
        'Normal': 1,
}

def adicionarListaPedidos(xml_input):
    """
    Recebe um arquivo XML contenedor de diversos pedidos de entrega. Armazena tais pedidos na lista de pedidos pendentes no banco de dados.
    """
    doc = parse(xml_input)


    for entrega in doc['root']['pedidos']:
        # O parser de XML retorna um dicionário de dicionários, de tipo OrderedDict
        # por isso, o primeiro passo é obter o(s) OrderedDict apropriado(s)
        pedidoOrderedDict = doc['root']['pedidos'][entrega]
        # e depois convertê-lo(s) para um dicionário comum
        pedido_kwargs = { key: pedidoOrderedDict[key] for key in pedidoOrderedDict if key != 'pacote'}
        pedidoValido = True


        ## Resolve DESTINATÁRIO
        destinatarioOrderedDict = pedidoOrderedDict['destinatario']
        dest_kwargs = { key: destinatarioOrderedDict[key] for key in destinatarioOrderedDict.keys() }
        # faz-se um query para ver se o destinatário já se encontra no banco de dados
        query_destinatario = models.Destinatario.objects.filter(**dest_kwargs)
        # dã
        if len(query_destinatario) > 0:
            destinatario = query_destinatario[0]
        else:
            destinatario = models.Destinatario(**dest_kwargs)
            destinatario.save()
        # como o dicionário já contêm um campo chamado destinatario,
        # preferi apenas substituir o conteúdo desse campo com o objeto destinatario obtido anteriormente
        # a fim de que não tenha que deletar tal campo e passar nominalmente por meio de kwargs
        # o referido objeto para o construtor de pedido
        pedido_kwargs['destinatario'] = destinatario

        ## Resolve CLIENTE
        nome_cliente = doc['root']['cliente']
        query_cliente = models.Cliente.objects.get(nome=nome_cliente)
        if query_cliente is not None:
            # pelo mesmo motivo resolvi sobrescrever o conteúdo do dicionário
            pedido_kwargs['cliente'] = query_cliente
        else:
            pedidoValido = False


        # REGIÃO
        query_regiao = models.Regiao.objects.filter(nome=pedidoOrderedDict['regiao'])
        if len(query_regiao) > 0:
            # pelo mesmo motivo resolvi sobrescrever o conteúdo do dicionário
            pedido_kwargs['regiao'] = query_regiao[0]

            # cálculo do frete
            volume = float(pedidoOrderedDict['pacote']['volume'])
            peso = float(pedidoOrderedDict['pacote']['peso'])
            precoBase = query_regiao[0].precoBase
            #TODO: inserir fórmula de cálculo de frete
            preco = 0.00

        else: # if query_regiao is None
            pedidoValido = False


        ## DATA DO PEDIDO
        data = pedidoOrderedDict['dataPedido']
        # pelo mesmo motivo resolvi sobrescrever o conteúdo do dicionário
        pedido_kwargs['dataPedido'] = datetime(year=int(data['year']), month=int(data['month']), day=int(data['day']))


        ## cria o PEDIDO, se for possível
        if pedidoValido:
            entrega = models.Entrega(preco=preco, qtd_tentativas=0, status='pendente', **pedido_kwargs)
            entrega.gerarCodigoRastreamento()
            entrega.save()


def listarPedidosPendentes():
    raw_query = models.Entrega.objects.filter(status='pendente')
    lista_ret = raw_query.order_by('dataPedido', 'prioridade')
    return lista_ret

def rastrearEntrega(cod):
    try:
        e = models.Entrega.objects.get(codigoRastreamento=cod)
        return e
    except models.Entrega.DoesNotExist as ex:
        raise ex

def finalizarEntrega(cod, dataEntrega):
    try:
        # obtém a entrega
        entrega = rastrearEntrega(cod)
        # modifica o seu status para 'entregue'
        entrega.status = 'entregue'
        # acrescenta a data em que foi realizada a entrega
        entrega.dataEntrega = dataEntrega
        # libera o entregador
        entrega.entregador.status = 0
    except models.Entrega.DoesNotExist as ex:
        raise ex
