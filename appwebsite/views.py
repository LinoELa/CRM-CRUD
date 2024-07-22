from django.shortcuts import render

# Para la autentificacion 
from django.contrib.auth import authenticate, login , logout

#Mensaje al hacer un log in o un log out 
from django.contrib import messages

# Create your views here.

def home(request):
    return render (request, 'home.html', {})