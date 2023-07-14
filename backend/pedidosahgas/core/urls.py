
from django.urls import path

from . import views

urlpatterns = [
    path("api/get_products", views.get_products, name='get_products'),
    path("api/get_payment_methods", views.get_payment_methods, name='get_payment_methods'),
    path('api/adicionar_carrinho/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('api/remover_carrinho/', views.remover_carrinho, name='remover_carrinho'),
    path('api/send_order/', views.send_order, name='send_order'),
    path('api/partner_search/', views.partner_search, name='partner_search'),
]
