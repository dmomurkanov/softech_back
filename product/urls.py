from rest_framework.routers import DefaultRouter

from product.views import CategoryViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet)