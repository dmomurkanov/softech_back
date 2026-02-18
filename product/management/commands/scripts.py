from decimal import Decimal

from django.core.management.base import BaseCommand

from product.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        queryset = Product.objects.all()
        ones = Product.objects.filter(name="test2")
        for one in ones:
            one.name = "111"
            one.save(update_fields=["name"])
        print(ones)
        print(queryset)

