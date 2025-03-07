from rest_framework import serializers
from .models import Consumo, Factura
from clients.serializers import ClienteSerializer
from assets.serializers import ElectricMeterSerializer
        
class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = (
            'id',
            'dateGenerated',
            'expireDate',
            'amount',
            'totalConsumed',
            'consumo'
        )

class ConsumoSerializer(serializers.ModelSerializer):

    #client = ClienteSerializer() #creo que de esta forma se hace el join

    class Meta:
        model = Consumo
        fields = (
            'id',
            'client',
            'meter'
        )

class ConsumoMeterSerializer(serializers.ModelSerializer):
    meter = ElectricMeterSerializer()
    class Meta:
        model = Consumo
        fields = (
            'id',
            'client',
            'meter'
        )

