from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.http import HttpResponse
from django.template import loader

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