from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from .serializers import UsuarioSerializer
from django.contrib.auth.models import User
from .models import Usuario

'''
    UserAPi
valida si tiene permisos de usuario usando el token, si el token existe retorna todos los datos del usuario
'''
class UserAPI(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Usuario.objects.all()
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

class RegisterAPI(generics.GenericAPIView):
    serializer_class = UsuarioSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user":UsuarioSerializer(user,context=self.get_serializer_context()).data,
        })