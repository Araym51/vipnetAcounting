from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from location.serializers import StreetModelSerializer
from .models import PcInfo

class PcInfoModelSeriazer(ModelSerializer):
    office_number = StreetModelSerializer()
    class Meta:
        model = PcInfo
        fields = '__all__'