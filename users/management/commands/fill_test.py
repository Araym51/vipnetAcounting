from mixer.backend.django import mixer
from django.core.management.base import BaseCommand

from location.models import Town, Street
from vipnet_users.models import VipNetUsers
from pc_info.models import PcInfo


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)


    def handle(self, *args, **options):
        records_count = options['count']
        for i in range(records_count):
            mixer.blend(Town)
            mixer.blend(Street)
            mixer.blend(PcInfo)
            mixer.blend(VipNetUsers)
        print('тестовые записи созданы')