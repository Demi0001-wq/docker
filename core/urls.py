from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductListCreateAPIView, ProductDetailAPIView

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Generic Views (Manual Routing)
    path('generic/products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('generic/products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
]
