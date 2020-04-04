from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from .serializers import SubstationSerializer
from django.contrib.auth.models import User
from .models import Substation

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
