from django.db import models

# Create your models here.
from location.models import Town, Street
from pc_info.models import PcInfo


class VipNetUsers(models.Model):
    username = models.EmailField(unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=150)
    last_name = models.CharField(verbose_name='Фамилия', max_length=150)
    fathers_name = models.CharField(verbose_name='Отчество', max_length=150)
    division = models.CharField(verbose_name='Подразделение', max_length=150)
    position = models.CharField(verbose_name='Должность', max_length=150)
    vipnet_name = models.ForeignKey(PcInfo, on_delete=models.CASCADE)
