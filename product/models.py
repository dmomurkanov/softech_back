from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255)
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name