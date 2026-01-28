from rest_framework import viewsets, mixins
from product.models import Product
from product.serializers import CategorySerializer


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = CategorySerializer
