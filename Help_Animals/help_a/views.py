from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

from .forms import AnimalsForm
from .models import Animals
#
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


class AddDetailView(DetailView):
    model = Animals
    template_name = 'help_a/details_view.html'
    context_object_name = 'animals_d'

class AddUpdateView(UpdateView):
    model = Animals
    template_name = "help_a/create.html"
    fields = ['title', 'slug', 'content', 'photo', 'cat']

class DeleteView(DeleteView):
    model = Animals
    template_name = "help_a/delete.html"
    success_url = '/animals/'



def index(request):
    return render(request, "help_a/index.html")

def animals(request):
    animals = Animals.objects.all()
    return render(request, "help_a/animals.html", {'animals': animals})

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



class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = "help_a/register.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    ##После регистрации сохраняет пользователя##


#####
class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'help_a/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('home')

