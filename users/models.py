from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(User):
    ROLES = (
        ('AD','Administrador'),
        ('GE','Gerente'),
        ('OP','Operador'),
        ('CL','Cliente')
    )
    rol = models.CharField(max_length=2, choices=ROLES, null=False, default="")
