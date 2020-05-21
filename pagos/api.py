from rest_framework import generics, permissions
from .models import Pago
from .serializers import PagoSerializer

class PagoApi(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class PagoListApi(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
