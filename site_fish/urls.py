
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hooks/', views.hooks, name='hooks'),
    path('rod/', views.rod, name='rod'),
    path('volosin/', views.volosin, name='volosin'),
    path('reels/', views.reels, name='reels'),
    path('singalizers/', views.singalizers, name='singalizers'),
    path('bait/', views.bait, name='bait'),
    path('podsak/', views.podsak, name='podsak'),
    path('buy/goods/<int:goods_id>/', views.buy_goods, name='buy_goods'),
    path('order/success/', views.order_success, name='order_success'),
    path('goods/<int:id>/', views.goods_detail, name='goods_detail'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
]
