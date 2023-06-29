from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import requests
import json
import re

API_URL ='https://livefrontapp-api.gasdelivery.com.br'
GOOGLE_PLACES_KEY='AIzaSyDXWZt8O3y0lYSDresa8iAy14bvEumbYDc'
GD_GROUP_HASH = '99b97d48ff2976e48105748d0e02f148' # revenda demonstração
partner_hash_id = 'fc3e40dab457fdef1ea84d1583fa91ad' # revenda demonstração
product_hash_id = 'bf0d0049b3b3e5a3f2c4d8f00ad8ff28'

carrinho = []

@csrf_exempt
def get_products(request):
    headers = {
        "gd-group-hash": GD_GROUP_HASH,
        "Content-Type": "application/json"
    }
    response = requests.get(f"{API_URL}/product", headers=headers)
    data = response.json()
    produtos = data['data']
    print(produtos)
    return render(request, 'template.html', {'produtos': produtos, 'carrinho': carrinho})

def adicionar_carrinho(request):
    produto_id = request.GET.get('produto_id')
    carrinho.append(produto_id)
    print(carrinho)
    return JsonResponse({'status': 'success', 'carrinho': carrinho})

def remover_carrinho(request):
    produto_id = request.GET.get('produto_id')
    if produto_id in carrinho:
        carrinho.remove(produto_id)
    print(carrinho)
    return JsonResponse({'status': 'success', 'carrinho': carrinho})



zip_code = '11045101'
product_name = 'P-13' 

# "P-13" 
# "product_hash_id": "bc99cd783f2993a72484c1c60ac7ba04", 
# "product_image_url": "https://s3.amazonaws.com/gasdelivery/live/products/2/P-13.jpg", 
# "product_short_description": "G\u00e1s GLP 13 KG", 
# "product_special_price": "130.00", 
# "product_container_flag": "1", 
# "product_container_price": "0.00"

# "P-20" 
# "product_hash_id": "bf0d0049b3b3e5a3f2c4d8f00ad8ff28", 
# "product_image_url": 
# "https://s3.amazonaws.com/gasdelivery/live/products/2/P-20.jpg", 
# "product_short_description": "agua", 
# "product_special_price": "10.00", 
# "product_container_flag": "1", 
# "product_container_price": "20.00"

# "P-45" 
# "product_hash_id": "9ce4f54aaef41af18a0f40681143403a", 
# "product_image_url": "https://s3.amazonaws.com/gasdelivery/live/products/2/P-45.jpg",
#  "product_short_description": "G\u00e1s GLP 45 KG", 
# "product_special_price": "320.00", 
# "product_container_flag": "1", 
# "product_container_price": "55.00"

# "Assistência Técnica": 
# "product_hash_id": "3db7501d758648b407331117a9510256", 
# "product_image_url": "https://s3.amazonaws.com/gasdelivery/live/products/2/at.jpg", 
# "product_short_description": "mao de obra", 
# "product_special_price": "60.00", "product_container_flag": "0", 
# "product_container_price": null, 

def partner_search(request):
    headers = {
        'gd-group-hash': GD_GROUP_HASH,
        "Content-Type": "application/json"
    }
    response = requests.get(f"{API_URL}/partner/{zip_code}/product/{product_name}", headers=headers)
    data = response.json()
    partners_list = data['data']
    product_hash_id = partners_list[0]['product_hash_id']
    request.session['product_hash_id'] = product_hash_id
    print (product_hash_id)
    return JsonResponse({'status': 'success', 'partners': partners_list})


    # for produto in data['data']:
    #     print(produto)

# na sessão de escolha de produto o campo product_name é preenchido.


# firebase_token = 'AIzaSyAErzTrST75ugXtuxB3_lAl6rKz8R1tZd8'

# export const createOrder = ({ address, vendor, checkoutInfo, firebaseToken, paymentGateway }) => {



def send_order(pedido):
    # product_hash_id = request.session.get('product_hash_id')
    pedido = {
        "address": {
            "address": "Oswaldo Cruz",
            "street_number": "429",
            "complement": "apt 85",
            "zip_code": "11045101",
            "neighborhood": "Boqueirão",
            "city": "Santos",
            'country': 'BR',
            "state": "SP",
            "lat": "-23.96816",
            "lng": "-46.32294"
        },
        "product": [
            {
                "hashid": product_hash_id,
                "quantity": "1",
                "vessel": "0"
            }
        ],
        "order": {
            "full_name": "Test",
            "phone": "13981942956",
            "partner_hashid": partner_hash_id,
            "mean_of_payment_id": "457",
            "date": "2023-05-31",
            "time": "15:00",
            "firebase_token": "AIzaSyAErzTrST75ugXtuxB3_lAl6rKz8R1tZd8"
        }
    }

    headers = {
        "gd-group-hash": GD_GROUP_HASH,
        "Content-Type": "application/json"
    }

    response = requests.post(f"{API_URL}/partner/order", headers=headers, data=json.dumps(pedido))

    if response.status_code == 200:
        return JsonResponse({"status": "success", "data": response.json()})
    else:
        return JsonResponse({"status": "error", "error": f"Erro ao fazer a solicitacao: {response.status_code}"}, status=500)
    



def get_payment_methods(request):
    headers = {
        "gd-group-hash": GD_GROUP_HASH,
        "Content-Type": "application/json"
    }
    response = requests.get(f"{API_URL}/partner/{partner_hashid}/means-of-payment", headers=headers)
    data = response.json()
    meios_de_pagamento = [meio['name'] for meio in data['data']]
    # for meio in meios_de_pagamento:
    #     print(meio)
    return render(request, 'template.html', {'meios_de_pagamento': meios_de_pagamento})


def process_location_details(details, address):
    if 'geometry' in details and 'location' in details['geometry']:
        lat = details['geometry']['location']['lat']
        lng = details['geometry']['location']['lng']
        address['lat'] = lat
        address['lng'] = lng
    return address


def get_current_place(lat, lng):

    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={37.7749},{-122.4194}&key={GOOGLE_PLACES_KEY}"
    response = requests.get(url)
    json_response = response.json()

    return json_response['results'][0]

details = {
    'geometry': {
        'location': {
            'lat': 37.7749,
            'lng': -122.4194
        }
    }
}

address = {
    'street': '123 Main St',
    'city': 'San Francisco',
    'state': 'CA',
    'country': 'US'
}

updated_address = get_current_place(details, address)
print(updated_address)