from django.db import models

from location.models import Street


# Create your models here.


class PcInfo(models.Model):
    WINDOWS_7 = 'Windows 7'
    WINDOWS_10 = 'Windows 10'
    ASTRA_LINUX = 'ASTRA_LINUX'

    OS_CHOICES = (
        (WINDOWS_7, 'Windows 7'),
        (WINDOWS_10, 'Windows 10'),
        (ASTRA_LINUX, 'ASTRA_LINUX'),
    )

    pc_name = models.CharField(verbose_name='имя компьютера', max_length=64, unique=True)
    operation_system = models.CharField(choices=OS_CHOICES, verbose_name='Операционная система', max_length=24, default=WINDOWS_7)
    hdd_number = models.CharField(verbose_name='Учетный номер ЖМД', max_length=32, blank=False)
    hdd_serial = models.CharField(verbose_name='Серийный номер ЖМД', max_length=64, blank=False)
    inventory_number = models.CharField(verbose_name='Инвентарный номер', max_length=64, blank=False, unique=True)
    pc_model = models.CharField(verbose_name='Модель ПЭВМ', max_length=64, blank=True)
    pc_mac = models.CharField(verbose_name='MAC адрес ПЭВМ', max_length=32)
    kaspersky = models.BooleanField(verbose_name='Начличие антивируса Касперский', default=True)
    vipnet_name = models.CharField(verbose_name='Название VipNet ключа', max_length=64)
    is_active = models.BooleanField(verbose_name='Активен', default=True)
    office_number = models.ForeignKey(Street, on_delete=models.CASCADE)
