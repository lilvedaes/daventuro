import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username='lilvedaes').exists():
            User.objects.create_superuser('lilvedaes',
                                          'daventuro@gmail.com',
                                          'y;_f"YfN:$2.9XaN')
