from ..models import Pedido


def add_pedido(new_pedido):
    pedido = Pedido(description=new_pedido)
    pedido.save()
    return pedido.to_dict_json()


def list_pedidos():
    pedidos = Pedido.objects.all()
    return [item.to_dict_json() for item in pedidos]
