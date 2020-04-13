from rest_framework import generics, permissions, filters, views, status
from rest_framework.response import Response
from .serializers import UsuarioSerializer, ReCaptchaSerializer
from django.contrib.auth.models import User
from .models import Usuario

# User's API

class RegisterAPI(generics.GenericAPIView):
    serializer_class = UsuarioSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user":UsuarioSerializer(user,context=self.get_serializer_context()).data,
        })

class UserAPI(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UserByIdAPI(generics.RetrieveUpdateAPIView): #tambien sirve para hacer PUT
    lookup_field = 'pk'
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        user = self.request.user
        return Usuario.objects.all()

class UserByUsernameAPI(generics.RetrieveUpdateAPIView): #tambien sirve para hacer PUT
    lookup_field = 'username'
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        user = self.request.user
        return Usuario.objects.all()

# reCAPTCHA's API

class VerifyTokenAPI(views.APIView):
    allowed_methods = ["POST"]
    permission_classes = [
        permissions.AllowAny,
    ]
    def post(self, request, *args, **kwargs):
        serializer = ReCaptchaSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'success': True}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
