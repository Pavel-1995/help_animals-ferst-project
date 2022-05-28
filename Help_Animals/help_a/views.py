from django.views.generic import DetailView
from django.shortcuts import render, redirect
from .models import Animals
from .forms import AnimalsForm




def index(request):
    return render(request, "help_a/index.html")

def animals(request):
    animals = Animals.objects.all()
    return render(request, "help_a/animals.html",  {'animals': animals})

class AddDetailView(DetailView):
    model = Animals
    template_name = 'help_a/details_view.html'
    context_object_name = 'animals_d'



def transportation(request):
    return render(request, "help_a/transportation.html")

def connection(request):
    return render(request, "help_a/connection.html")

def create(request):
    if request.method == 'POST':
        form = AnimalsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('animals')
    else:
        form = AnimalsForm()
    return render(request, "help_a/create.html", {'form': form})

