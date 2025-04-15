from django.contrib import admin
from site_fish.models import Goods, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_ca',)

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)



