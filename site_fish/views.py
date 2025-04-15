from django.shortcuts import render

from site_fish.models import Category, Goods


def home(request):
    context = {'page_title': 'Головна ',
               'category': Category.objects.all(),
               'goods': Goods.objects.all(),}
    return render(request, 'main.html', context)

def places(request):
    context = {'page_title': 'Місця'}
    return render(request, 'places.html', context)

def species(request):
    context = {'page_title': 'Види'}
    return render(request, 'species.html', context)

def tackle(request):
    context = {'page_title': 'Спорядження'}
    return render(request, 'tackle.html', context)