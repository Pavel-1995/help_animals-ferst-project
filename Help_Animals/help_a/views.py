
from django.shortcuts import render



def index(request):
    return render(request, "help_a/index.html")

def about(request):
    return render(request, "help_a/about.html")

def transportation(request):
    return render(request, "help_a/transportation.html")

def connection(request):
    return render(request, "help_a/connection.html")