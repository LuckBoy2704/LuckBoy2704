from django.contrib import admin
from site_fish.models import Goods, Category, Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'goods_name', 'quantity', 'created_at')
    list_filter = ('created_at', 'goods_name')
    search_fields = ('name', 'phone_number', 'address', 'goods_name')
    readonly_fields = ('created_at',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_ca',)

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Order, OrderAdmin)