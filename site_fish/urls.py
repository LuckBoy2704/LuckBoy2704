from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('places/', views.places, name='places'),
    path('species/', views.species, name='species'),
    path('tackle/', views.tackle, name='tackle'),
]