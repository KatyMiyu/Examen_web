from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    navs = Navbar.objects.all()
    context = {
        'navs' : navs
    }
    return render (request, 'libro/index.html',context)

def libros(request):
    navs = Navbar.objects.all()
    libros = Libros.objects.all()
    context = {
        'navs' : navs,
        'libros' : libros
    }
    return render (request, 'libro/libros.html',context)

def autores(request):
    navs = Navbar.objects.all()
    autores = Autores.objects.all()
    context = {
        'navs' : navs,
        'autores' : autores
    }
    return render (request, 'libro/autores.html',context)

def categorias(request):
    navs = Navbar.objects.all()
    categorias = Categorias.objects.all()
    context = {
        'navs' : navs,
        'categorias' : categorias
    }
    return render (request, 'libro/categorias.html',context)