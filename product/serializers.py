from django.db.models import Q
from rest_framework import serializers

from product.models import Category, SubCategory, Product, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = SubCategory
        fields = ("id","category", "name", "product_count")

    def validate_name(self, value):
        if value[0].isupper():
            return value
        raise serializers.ValidationError("Invalid name")

    def get_product_count(self, obj):
        products = Product.objects.filter(sub_category=obj)
        return products.count()


class CategoryDetailSerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('sub_categories',)


class TestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    price_with_discount = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'discount',
            'image',
            "price_with_discount",
            "hit",
            "promotion",
            "popular",
            "count",
            "text"
        )

    def get_price(self, obj):
        return float(obj.price)

    def get_price_with_discount(self, obj):
        return float(obj.price_with_discount)

    def get_count(self, obj):
        return Product.objects.filter(
            Q(hit=True) | Q(popular=True) | Q(promotion=True)
        ).count()


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image')


class ProductDetailSerializer(serializers.ModelSerializer):
    savings = serializers.SerializerMethodField()
    images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "price",
            "discount",
            "price_with_discount",
            "code",
            "article",
            "savings",
            "hit",
            "promotion",
            "popular",

            "images",
        )

    def get_savings(self, obj):
        pass