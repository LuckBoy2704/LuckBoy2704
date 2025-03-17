from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('places/', views.places_page, name='places'),
    path('species/', views.species_page, name='species'),
    path('tackle/', views.tackle_page, name='tackle'),
]