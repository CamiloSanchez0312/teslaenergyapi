from django.contrib.auth.models import User
from .models import Usuario, Cliente
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('cedula', 'first_name','last_name','email')
        