from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import OrderForm
from .models import Goods,Category

def home(request):
    categories = Category.objects.all()
    goods = Goods.objects.all()

    context = {'categories': categories,
               'goods': goods,
               }
    return render(request, 'home.html', context)


def goods_detail(request, id=None):
    goods = get_object_or_404(Goods, id=id)
    category_in_goods = goods.category
    context = {
        'title': f'Товари ',
        'goods': goods,
        'category_in_goods': category_in_goods,
    }
    return render(request, template_name="myapp/Page.html", context=context)

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    goods_in_category = Goods.objects.filter(category=category)
    context = {
        'title': f'Категорії: {category.name_ca}',
        "category": category,
        'goods_in_category': goods_in_category
    }
    return render(request, 'Main.html', context)

def buy_goods(request, goods_id):
    goods = get_object_or_404(Goods, pk=goods_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, initial={'goods_name': goods.name, 'price': goods.price, 'quantity': 1})
        if form.is_valid():
            order = form.save()
            messages.success(request, f'Замовлення на "{goods.name}" успішно оформлено!')
            return redirect('order_success')
        else:
            messages.error(request, 'Будь ласка, виправте помилки у формі.')
    else:
        form = OrderForm(initial={'goods_name': goods.name, 'price': goods.price, 'quantity': 1})

    context = {
        'title': 'Оформлення замовлення',
        'form': form,
        'goods': goods,
    }
    return render(request, 'buy_goods.html', context)
def order_success(request):
    return render(request, 'order_success.html', {'title': 'Замовлення успішне'})

def rod(request):
    return category_detail(request, Category.objects.get(name_ca='Вудилища').id)

def hooks(request):
    return category_detail(request, Category.objects.get(name_ca='Гачки').id)

def reels(request):
    return category_detail(request, Category.objects.get(name_ca='Котушки').id)

def volosin(request):
    return category_detail(request, Category.objects.get(name_ca='Волосінь').id)

def singalizers(request):
    return category_detail(request, Category.objects.get(name_ca='Сингалізатори').id)

def bait(request):
    return category_detail(request, Category.objects.get(name_ca='Наживка').id)

def podsak(request):
    return category_detail(request, Category.objects.get(name_ca='Підсак').id)


