from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from .serializers import SubstationSerializer, TransformerSerializer, ElectricMeterSerializer
from django.contrib.auth.models import User
from .models import Substation, Transformer, ElectricMeter

# Substation's API

class SubstationRegisterAPI(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Substation.objects.all()
    serializer_class = SubstationSerializer

class SubstationListAPI(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def list(self, request):
        queryset = Substation.objects.all()
        serializer_class = SubstationSerializer(queryset, many=True)
        return Response(serializer_class.data)


# Transformer's API

class TransformerRegisterAPI(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Transformer.objects.all()
    serializer_class = TransformerSerializer

class TransformerListAPI(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def list(self, request):
        queryset = Transformer.objects.all()
        serializer_class = TransformerSerializer(queryset, many=True)
        return Response(serializer_class.data)


# ElectricMeter's API

class ElectricMeterRegisterAPI(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = ElectricMeter.objects.all()
    serializer_class = ElectricMeterSerializer

class ElectricMeterListAPI(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def list(self, request):
        queryset = ElectricMeter.objects.all()
        serializer_class = ElectricMeterSerializer(queryset, many=True)
        return Response(serializer_class.data)
