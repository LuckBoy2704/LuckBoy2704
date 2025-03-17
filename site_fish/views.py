from django.shortcuts import render

def home_page(request):
    context = {'page_title': 'Головна сторінка'}
    return render(request, 'home.html', context)

def places_page(request):
    context = {'page_title': 'Місця'}
    return render(request, 'places.html', context)

def species_page(request):
    context = {'page_title': 'Види'}
    return render(request, 'species.html', context)

def tackle_page(request):
    context = {'page_title': 'Спорядження'}
    return render(request, 'tackle.html', context)