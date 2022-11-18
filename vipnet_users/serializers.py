from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from location.serializers import StreetModelSerializer
from pc_info.serializator import PcInfoModelSeriazer
from .models import VipNetUsers


class VipNetUsersSerializer(ModelSerializer):
    vipnet_name = PcInfoModelSeriazer()
    class Meta:
        model = VipNetUsers
        fields = '__all__'