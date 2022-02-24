from django.db import models

# Create your models here.
import vipnet_users.models
from vipnet_users.models import VipNetUsers


class PCinfo(models.Model):
    WINDOWS_7 = 'Windows 7'
    WINDOWS_10 = 'Windows 10'
    ASTRA_LINUX = 'ASTRA_LINUX'

    OS_CHOICES = (
        (WINDOWS_7, 'Windows 7'),
        (WINDOWS_10, 'Windows 10'),
        (ASTRA_LINUX, 'ASTRA_LINUX'),
    )

    pc_name = models.CharField(verbose_name='имя компьютера', max_length=64, unique=True)
    operation_system = models.CharField(choices=OS_CHOICES, verbose_name='операционная система', max_length=24, default=WINDOWS_7)
    hdd_number = models.CharField(verbose_name='Учетный номер ЖМД', max_length=32, blank=False)
    hdd_serial = models.CharField(verbose_name='Серийный номер ЖМД', max_length=64, blank=False)
    inventory_number = models.CharField(verbose_name='инвентарный номер', max_length=64, blank=False, unique=True)
    pc_model = models.CharField(verbose_name='модель ПЭВМ', max_length=64, blank=True)
    pc_mac = models.CharField(verbose_name='MAC адрес ПЭВМ', max_length=32)
    kaspersky = models.BooleanField(verbose_name='начличие антивируса Касперский', default=True)
    username = models.ForeignKey(vipnet_users.models.VipNetUsers, on_delete=models.CASCADE)
