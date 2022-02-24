from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

import location.models
from location.models import Town, Street


class VipNetUsers(AbstractUser):
    username = models.EmailField(unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=150)
    last_name = models.CharField(verbose_name='Фамилия', max_length=150)
    fathers_name = models.CharField(verbose_name='Отчество', max_length=150)
    division = models.CharField(verbose_name='подразделение', max_length=150)
    position = models.CharField(verbose_name='должность', max_length=150)
    town_name = models.ForeignKey(location.models.Town, on_delete=models.CASCADE)
    street = models.ForeignKey(location.models.Street, on_delete=models.CASCADE)
    office_number = models.ForeignKey(location.models.Street, on_delete=models.CASCADE)