from django.contrib.auth.models import User
from .models import Usuario
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

class RolSelializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')

class UsuarioSerializer(serializers.ModelSerializer):
    usuarios = RolSelializer(many = False)
    class Meta:
        model = User 
        fields = (
            'id','username', 'password', 'first_name', 'last_name' , 
            'email','groups','is_active','is_superuser','usuarios'
            )
        extra_kwars = {'password':{'write_only':True}}

    def create(self, validated_data):
        usuario = validated_data.pop('usuarios')
        user = User.objects.create_user(**validated_data)
        Usuario.objects.create(user=user, **usuario)
        return user