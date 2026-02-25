from rest_framework import viewsets, generics
from .models import Product
from .serializers import ProductSerializer

# ViewSet approach (Task 3)
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Generic Views approach (Task 5)
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # Example of overriding: adding custom logic before saving
        # Let's say we want to log the creation or modify a field
        print(f"Creating a new product: {serializer.validated_data.get('name')}")
        serializer.save()

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
