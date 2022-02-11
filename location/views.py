from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Town, Street
from .serializers import TownModelSerializer, StreetModelSerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.


class TownModelViewSet(ModelViewSet):
    queryset = Town.objects.all()
    serializer_class = TownModelSerializer


class StreetModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer]
    queryset = Street.objects.all()
    serializer_class = StreetModelSerializer