from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import User, Payment
from .serializers import *
class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        # Logic for creating points is omitted for simplicity in this reconstruction
        payment.save()
