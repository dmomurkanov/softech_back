from rest_framework.routers import DefaultRouter

from product.serializers import SubCategorySerializer
from product.views import CategoryViewSet, SubCategoryViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('sub-category', SubCategoryViewSet)