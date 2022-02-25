from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from pc_info.models import PcInfo
from pc_info.serializator import PcInfoModelSeriazer
# Create your views here.


class PcInfoModelViewSet(ModelViewSet):
    queryset = PcInfo.objects.all()
    serializer_class = PcInfoModelSeriazer