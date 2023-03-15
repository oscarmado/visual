from django.shortcuts import render

# Create your views here.
def inicio(request):
    contexto={}
    return render(request, 'inicio.html', contexto)

def listar_productos(request):
    productos=['portatil lenovo','iphone 7','mac 12 mini','iphone 14 pro']
    contexto={}
    return render(request, 'listar_productos.html', contexto)