from rest_framework import serializers
from .models import Substation, Transformer, ElectricMeter

class SubstationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Substation
        fields = ('name', 'latitude', 'longitude')

class TransformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transformer
        fields = ('name', 'latitude', 'longitude', 'substation')

class ElectricMeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectricMeter
        fields = ('name', 'latitude', 'longitude', 'transformer')
