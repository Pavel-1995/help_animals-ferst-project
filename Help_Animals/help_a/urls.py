from django.contrib import admin
from django.urls import path, include
from  django.conf import settings
from django.conf.urls.static import static
from .import views


urlpatterns = [

    path('', views.index, name='home'),
    path('animals/', views.animals, name='animals'),
    path('transportation', views.transportation, name='transportation'),
    path('connection', views.connection, name='connection'),
    path('create', views.create, name='create'),

]
