from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.http import HttpResponse
from django.template import loader
from .forms import IngredienteForm, stockform
from .models import *
from django.contrib import messages

# Create your views here.

def index (request):
    template = loader.get_template('main/indexx.html')
    context = {}
    return HttpResponse(template.render(context, request))

def login(request):
    
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                do_login(request, user)
                return redirect('/workstation')

    return render(request, "main/login.html", {'form': form})

def workstation (request):
    template = loader.get_template('main/workstation.html')
    context = {}
    return HttpResponse(template.render(context, request))

def logout(request):
    
    do_logout(request)
    
    return redirect('login')


def ingredienteviw (request):
    form = IngredienteForm()

    if request.method == "POST":
        form = IngredienteForm(request.POST)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.save()
            messages.success(request, "Agregado Correctamente")
            return redirect('/stock')

    return render(request, 'main/workstation_bodega.html')
    

def lista_ingredientes (request):
    ingredientes = IngredientesXxi.objects.all()

    data = {
        'IngredientesXxi': ingredientes
    }
    return render(request, 'main/workstation_bodega_stock.html', data)

def editar_stck(request, id):
    
    ingredientes = get_object_or_404(IngredientesXxi, id_ingrediente = id)

    data = {
        'form': stockform(instance=ingredientes)
    }
    if request.method == 'POST':
        formmulario = stockform(data=request.POST, instance=ingredientes)

        if formmulario.is_valid():
            formmulario.save()
            messages.success(request, "Stock Modificado" )
            return redirect(to="stock")
        data["form"] = formmulario        
    
    return render(request, 'main/editar_stock.html', data)

def eliminar_ingrediente(request, id):

    ingredientes = get_object_or_404(IngredientesXxi, id_ingrediente = id)
    ingredientes.delete()
    messages.success(request, "Eliminado correctamente")

    return redirect(to="stock")