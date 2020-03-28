from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializer
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Usuario

class UsuarioViewSetsUsername(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (permissions.IsAuthenticated, )

class UsuariosAll(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer