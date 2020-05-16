from django.db import models

class Cliente(models.Model):
    cedula = models.CharField(max_length=15, unique=True, null=False)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=50, null=False)
    is_active = models.BooleanField(default=True)
    TYPES = (
         ('CO','Corporativo'),
         ('NA','Natural')
     )
    type = models.CharField(max_length=2, choices=TYPES, null=False, default="")
