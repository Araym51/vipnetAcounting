from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework import status

from .models import VipNetUsers
from .serializers import VipNetUsersSerializer
# Create your views here.

class VipNetUsersViewSet(ModelViewSet):
    queryset = VipNetUsers.objects.all()
    serializer_class = VipNetUsersSerializer
