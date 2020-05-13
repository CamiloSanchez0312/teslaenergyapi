from rest_framework import serializers
from .models import Substation, Transformer, ElectricMeter

class SubstationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Substation
        fields = ('id', 'name', 'latitude', 'is_active','longitude')

class TransformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transformer
        fields = ('id', 'name', 'latitude', 'longitude', 'is_active','substation')

class ElectricMeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectricMeter
        fields = ('id', 'name', 'latitude', 'longitude', 'is_active','transformer')
