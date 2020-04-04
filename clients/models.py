from django.db import models

# Create your models here.


class Cliente(models.Model):
    cedula = models.CharField(max_length=15, unique=True, null=False)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=50, null=False)