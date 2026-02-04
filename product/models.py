from django.db import models
from decimal import Decimal
from ckeditor.fields import RichTextField



class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
            return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
            return self.name


class Product(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255)
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    code = models.CharField(verbose_name="код товара", max_length=10,null=True)
    article = models.IntegerField(verbose_name="Артикул", null=True)
    discount = models.PositiveIntegerField(verbose_name="Процент скидки", null=True)
    price_with_discount = models.DecimalField(verbose_name="Цена со скидкой", max_digits=10, decimal_places=2, null=True, blank=True)
    amount = models.PositiveIntegerField(verbose_name="количество", default=0)
 
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.price_with_discount = self.price * (1 - Decimal(self.discount) / Decimal(100))
        super().save(*args, **kwargs)


class ProductDescription(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    text = RichTextField("Описание")


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    image = models.ImageField("фотография", upload_to="product")

    

        