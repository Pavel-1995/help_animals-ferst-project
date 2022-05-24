
from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('transportation', views.transportation, name='transportation'),
    path('connection', views.connection, name='connection'),

]
