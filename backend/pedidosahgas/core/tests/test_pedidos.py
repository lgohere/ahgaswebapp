from pedidosahgas.accounts.models import User
from pedidosahgas.accounts.tests import fixtures
from pedidosahgas.core.models import Pedido


def test_criar_pedido_sem_login(client):
    resp = client.post("/api/core/pedidos/add", {"new_pedido": "walk the dog"})
    assert resp.status_code == 401


def test_criar_pedido_com_login(client, db):
    fixtures.user_jon()
    client.force_login(User.objects.get(username="jon"))
    resp = client.post("/api/core/pedidos/add", {"new_pedido": "walk the dog"})
    assert resp.status_code == 200


def test_criar_pedido_com_login(client, db):
    fixtures.user_jon()
    Pedido.objects.create(description="walk the dog")

    client.force_login(User.objects.get(username="jon"))
    resp = client.get("/api/core/pedidos/list")
    data = resp.json()

    assert resp.status_code == 200
    assert data == {"pedidos": [{"description": "walk the dog", "done": False, "id": 1}]}
