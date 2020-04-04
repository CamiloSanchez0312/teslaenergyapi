from rest_framework import serializers
from .models import Substation

class SubstationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Substation
        fields = ('name', 'latitude', 'longitude')
