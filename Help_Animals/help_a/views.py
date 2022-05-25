
from django.shortcuts import render
from .models import Animals, Category


def index(request):
    return render(request, "help_a/index.html")

def animals(request):
    animals = Animals.objects.all()
    return render(request, "help_a/animals.html", {'animals': animals})

def transportation(request):
    return render(request, "help_a/transportation.html")

def connection(request):
    return render(request, "help_a/connection.html")