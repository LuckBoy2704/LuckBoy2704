from django.shortcuts import render

def home(request):
    context = {'page_title': 'Головна '}
    return render(request, 'home.html', context)

def places(request):
    context = {'page_title': 'Місця'}
    return render(request, 'places.html', context)

def species(request):
    context = {'page_title': 'Види'}
    return render(request, 'species.html', context)

def tackle(request):
    context = {'page_title': 'Спорядження'}
    return render(request, 'tackle.html', context)