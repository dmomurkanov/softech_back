from django.db import models
from decimal import Decimal

class Product(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255)
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    description = models.TextField(verbose_name="Описание", null=True)
    code = models.CharField(verbose_name="код товара", max_length=10,null=True)
    article = models.IntegerField(verbose_name="Артикул", null=True)
    discount = models.PositiveIntegerField(verbose_name="Процент скидки", null=True)
    price_with_discount = models.DecimalField(verbose_name="Цена со скидкой", max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.price_with_discount = self.price * (1 - Decimal(self.discount) / Decimal(100))
        super().save(*args, **kwargs)
        