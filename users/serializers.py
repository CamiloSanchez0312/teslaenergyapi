from django.contrib.auth.models import User
from .models import Usuario
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario 
        fields = (
            'id','username','password' ,'first_name', 'last_name' , 
            'email','groups','is_active','is_superuser','rol'
            )
        extra_kwars = {'password':{'write_only':True}}
        

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
