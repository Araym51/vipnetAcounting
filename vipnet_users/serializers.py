from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import VipNetUsers


class VipNetUsersSerializer(ModelSerializer):
    class Meta:
        model = VipNetUsers
        fields = '__all__'