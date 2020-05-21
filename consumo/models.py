from django.db import models
import datetime
from clients.models import Cliente
from assets.models import ElectricMeter

# Create your models here.
class Consumo(models.Model): #mediante este modelo se le asigna un medidor a un cliente
    client = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    meter = models.OneToOneField(ElectricMeter, on_delete=models.CASCADE, unique=True)

class Factura(models.Model):
    dateGenerated = models.DateField(auto_now=True)
    #dateExpiry = models.DateField(null=True)
    #amount = models.FloatField(null=True)
    totalConsumed = models.FloatField()
    consumo = models.ForeignKey(Consumo, on_delete=models.CASCADE)

    @property
    def amount(self):
        valorKWH = 567.9
        amo = round(self.totalConsumed*valorKWH,1) #un valor decimal
        return amo

    @property
    def expireDate(self):
        date = datetime.date.today()+datetime.timedelta(days=9)
        return date