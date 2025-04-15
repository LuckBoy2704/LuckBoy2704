from django.db import models


class Category(models.Model):
    name_ca = models.CharField(max_length=50,verbose_name="Товари")
    description_ca = models.TextField(blank=True,null=True,verbose_name="Опис")
    price_ca = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    email_ca = models.EmailField(blank=True, null=True,verbose_name="Email")
    updated_at = models.DateTimeField(auto_now=True)
    order = models.IntegerField(default=0,verbose_name="Активна чи не активна")

    def __str__(self):
        return self.name_ca


class Goods(models.Model):
    name = models.CharField(max_length=50,verbose_name="Товари")
    description = models.TextField(blank=True,null=True,verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Ціна")
    url = models.URLField(blank=True, null=True,verbose_name="Посилання")
    email = models.EmailField(blank=True, null=True,verbose_name="Email")
    quantity = models.IntegerField(default=0,verbose_name="Кількість")
    image = models.ImageField(blank=True,upload_to="Photo/", null=True,verbose_name="Зображення")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія", null=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Дата створення")

    def __str__(self):
        return self.name

