from django.db import models

class Substation(models.Model):
    name = models.CharField(max_length=15, null=False)
    latitude = models.DecimalField(max_digits=30, decimal_places=20, null=False)
    longitude = models.DecimalField(max_digits=30, decimal_places=20, null=False)
    # location = models.PointField(null=False, unique=True)

class Transformer(models.Model):
    name = models.CharField(max_length=15, null=False)
    latitude = models.DecimalField(max_digits=30, decimal_places=20, null=False)
    longitude = models.DecimalField(max_digits=30, decimal_places=20, null=False)
    substation = models.ForeignKey(Substation, on_delete=models.CASCADE)

class ElectricMeter(models.Model):
    name = models.CharField(max_length=15, null=False)
    latitude = models.DecimalField(max_digits=30, decimal_places=20, null=False)
    longitude = models.DecimalField(max_digits=30, decimal_places=20, null=False)
    transformer = models.ForeignKey(Transformer, on_delete=models.CASCADE)
