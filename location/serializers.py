from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from models import Town, Street

class TownModelSerializer(ModelSerializer):
    class Meta:
        model = Town
        fields = '__all__'


class StreetModelSerializer(ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'
