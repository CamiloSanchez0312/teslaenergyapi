from rest_framework import generics, permissions
from .models import Consumo, Factura
from .serializers import ConsumoSerializer, FacturaSerializer

#Apis para Consumo
class ConsumoApi(generics.CreateAPIView): 
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Consumo.objects.all()
    serializer_class = ConsumoSerializer


#Apis para Factura
class FacturaApi(generics.CreateAPIView): 
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class FacturaApiList(generics.ListAPIView): 
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

