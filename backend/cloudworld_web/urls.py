"""
URL configuration for cloudworld_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from productos.views import home, producto_detalle
from carrito.views import agregar_carrito, ver_carrito, restar_carrito
from django.contrib.auth import views as auth_views
from productos.views import api_dolar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('producto/<int:id>/', producto_detalle),
    path('agregar/<int:id>/', agregar_carrito),
    path('carrito/', ver_carrito),
    path('restar/<int:id>/', restar_carrito),

    path('login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('logout/', auth_views.LogoutView.as_view(next_page='/')),
    path('api/', api_dolar),
]


