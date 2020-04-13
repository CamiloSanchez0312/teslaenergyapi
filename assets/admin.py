from django.contrib import admin
from .models import Substation, Transformer, ElectricMeter

# Register your models here.
admin.site.register(Substation)
admin.site.register(Transformer)
admin.site.register(ElectricMeter)
