from django.shortcuts import render
from .models import Producto


def home(request):
    return render(request, 'home.html')

def listado(request):
    productos = Producto.objects.all()
    return render(request, 'listado.html', {'productos': productos})


# Create your views here.
