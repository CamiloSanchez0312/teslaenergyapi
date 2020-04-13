from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from .serializers import ClienteSerializer
from django.contrib.auth.models import User
from .models import Cliente

# Client's API

class ClienteRegisterAPI(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteListAPI(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteByCedulaAPI(generics.RetrieveUpdateAPIView): #tambien sirve para hacer PUT
    lookup_field = 'cedula'
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ClienteSerializer

    def get_queryset(self):
        user = self.request.user
        return Cliente.objects.all()
