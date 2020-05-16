from django.db import models
from clients.models import Cliente
from assets.models import ElectricMeter

# Create your models here.
class Consumo(models.Model): #mediante este modelo se le asigna un medidor a un cliente
    client = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    meter = models.OneToOneField(ElectricMeter, on_delete=models.CASCADE)

class Factura(models.Model):
    dateGenerated = models.DateField(auto_now=True)
    dateExpiry = models.DateField()
    amount = models.FloatField(null=False)
    totalConsumed = models.IntegerField()
    consumo = models.ForeignKey(Consumo, on_delete=models.CASCADE)
