from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from .serializers import UsuarioSerializer
from django.contrib.auth.models import User

'''
    UserAPi
valida si tiene permisos de usuario usando el token, si el token existe retorna todos los datos del usuario
'''
class UserAPI(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

class UserByIdAPI(generics.RetrieveAPIView):
    lookup_field = 'pk'
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.all()

class UserByUsernameAPI(generics.RetrieveAPIView):
    lookup_field = 'username'
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.all()
    '''
    def get_object(self):
        return self.request.user '''