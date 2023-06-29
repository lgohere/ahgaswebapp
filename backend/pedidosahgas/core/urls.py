
from django.urls import path

from . import views

urlpatterns = [
    path("get_products", views.get_products, name='get_products'),
    path("get_payment_methods", views.get_payment_methods, name='get_payment_methods'),
    path('adicionar_carrinho/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('remover_carrinho/', views.remover_carrinho, name='remover_carrinho'),
    path('send_order/', views.send_order, name='send_order'),
    path('partner_search/', views.partner_search, name='partner_search'),
]
