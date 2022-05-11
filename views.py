from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def informacion(request):
    return render(request, 'paginas/informacion.html')

def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/index.html', {'usuarios': usuarios})

def crear(request):
    formulario = UsuarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('usuarios')
    return render(request, 'usuarios/crear.html', {'formulario': formulario})

def editar(request, DNI):
    usuarios = Usuario.objects.get(DNI=DNI)
    formulario = UsuarioForm(request.POST or None, request.FILES or None, instance=usuarios)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('usuarios')
    return render(request, 'usuarios/editar.html', {'formulario': formulario})

def borrar(request, DNI):
    usuarios = Usuario.objects.get(DNI=DNI)
    usuarios.delete()
    return redirect('usuarios')
