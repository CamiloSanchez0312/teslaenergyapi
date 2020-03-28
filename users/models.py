from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    ROLES = (
        ('AD','Administrador'),
        ('GR','Gerente'),
        ('OP','Operador'),
        ('CL','Cliente')
    )
    rol = models.CharField(max_length=2, choices=ROLES, null=False, default="")
    user = models.OneToOneField(User, related_name=("usuarios"), on_delete=models.CASCADE)