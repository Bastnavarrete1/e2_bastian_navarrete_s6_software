from django.shortcuts import render, redirect, get_object_or_404
from productos.models import Producto
from .models import Carrito, ItemCarrito
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def agregar_carrito(request, id):
    producto = get_object_or_404(Producto, id=id)

    user = request.user
    print("USER:", user)

    if not user:
        return redirect('/')

    carrito, created = Carrito.objects.get_or_create(usuario=user)

    item, created = ItemCarrito.objects.get_or_create(
        carrito=carrito,
        producto=producto,
        defaults={"cantidad": 1}
    )

    if not created:
        item.cantidad += 1
        item.save()

    print("ITEM GUARDADO:", item)

    return redirect('/')


@login_required
def ver_carrito(request):
    user = request.user

    if not user:
        return render(request, 'carrito.html', {
            'items': [],
            'total': 0
        })

    carrito = Carrito.objects.filter(usuario=user).first()

    items = carrito.itemcarrito_set.all() if carrito else []

    total = sum(i.producto.precio * i.cantidad for i in items)

    return render(request, 'carrito.html', {
        'items': items,
        'total': total
    })

@login_required
def restar_carrito(request, id):
    item = get_object_or_404(ItemCarrito, id=id)

    if item.cantidad > 1:
        item.cantidad -= 1
        item.save()
    else:
        item.delete()

    return redirect('/carrito/')