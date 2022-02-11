from django.db import models

# Create your models here.

class Town(models.Model):
    town_name = models.CharField(verbose_name='Город', max_length=128)


class Street(models.Model):
    street = models.CharField(verbose_name='Улица', max_length=128)
    house_number = models.CharField(verbose_name='номер дома', max_length=64)
    office_number = models.PositiveIntegerField(verbose_name='номер кабинета')
    town_name = models.ForeignKey(Town, on_delete=models.CASCADE)
