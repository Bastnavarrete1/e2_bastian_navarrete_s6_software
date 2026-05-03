from django.shortcuts import render, get_object_or_404
from .models import Producto
import requests

def home(request):
    productos = Producto.objects.all()
    return render(request, 'home.html', {'productos': productos})

def producto_detalle(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'detalle.html', {'producto': producto})

def api_dolar(request):
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()

    clp = data['rates']['CLP']

    return render(request, 'api.html', {
        'clp': clp
    })