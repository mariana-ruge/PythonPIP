import requests

def get_categorias():
    request = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(request.status_code)
    print(request.text)
    print(type(request.text))
    categorias = request.json()
    for categoria in categorias:
        print(categoria['name'])

