from django.db import models
from django.conf import settings


class Category(models.Model):
    name_ca = models.CharField(max_length=50, verbose_name="Товари")
    description_ca = models.TextField(blank=True, null=True, verbose_name="Опис")
    price_ca = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_ca

    def get_absolute_url(self):
        return f"/category/{self.name_ca}"


class Goods(models.Model):
    name = models.CharField(max_length=50, verbose_name="Товари")
    description = models.TextField(blank=True, null=True, verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    url = models.URLField(blank=True, null=True, verbose_name="Посилання")
    quantity = models.IntegerField(default=0, verbose_name="Кількість")
    image = models.ImageField(blank=True, upload_to="Photo/", null=True, verbose_name="Зображення")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія", null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.price} грн"

    def goods_model(self):
        return f"/goods/{self.id}"

class Order(models.Model):
    goods_name = models.CharField(max_length=255, verbose_name='Назва товару')
    quantity = models.IntegerField(default=1, verbose_name='Кількість')
    name = models.CharField(max_length=100, verbose_name='Ваше ім\'я')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефону')
    address = models.TextField(verbose_name='Адреса доставки')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Замовлення №{self.id} на {self.quantity} x {self.goods_name} від {self.name}'

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'
