from rest_framework import viewsets, mixins
from product.models import Product, SubCategory, Category
from product.serializers import (
    CategorySerializer,
    SubCategorySerializer,
    CategoryDetailSerializer,
    ProductSerializer,
    ProductDetailSerializer
)
from django.db.models import Q

class CategoryViewSet(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet
    ):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CategoryDetailSerializer
        return CategorySerializer



class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class ProductViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.filter(
        Q(hit=True) | Q(popular=True) | Q(promotion=True)
    )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductSerializer





