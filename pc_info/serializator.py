from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from .models import PcInfo

class PcInfoModelSeriazer(ModelSerializer):
    class Meta:
        model = PcInfo
        fields = '__all__'