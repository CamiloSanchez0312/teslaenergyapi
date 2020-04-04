from django.db import models

# Create your models here.
class Substation(models.Model):
    name = models.CharField(max_length=15, null=False)
    latitude = models.DecimalField(max_digits=30, decimal_places=20, null=False)
    longitude = models.DecimalField(max_digits=30, decimal_places=20, null=False)
    # location = models.PointField(null=False, unique=True)
