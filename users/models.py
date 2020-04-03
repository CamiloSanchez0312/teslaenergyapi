from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(User):
    #id = models.AutoField(primary_key=True)
    ROLES = (
        ('AD','Administrador'),
        ('GE','Gerente'),
        ('OP','Operador'),
        ('CL','Cliente')
    )
    rol = models.CharField(max_length=2, choices=ROLES, null=False, default="")

class Cliente(models.Model):
    cedula = models.CharField(max_length=15, unique=True, null=False)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=50, null=False)
    