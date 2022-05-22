
from django.shortcuts import render



def index(request):
    return render(request, "help_a/index.html")

def about(request):
    return render(request, "help_a/about.html")