from django.db import models
from consumo.models import Factura
from users.models import Usuario

# Create your models here.
class Pago(models.Model):
    date = models.DateField(auto_now=True)
    factura = models.OneToOneField(Factura, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)