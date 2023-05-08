import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            release_date = datetime.strptime(phone['release_date'], '%Y-%m-%d')
            slug = slugify(phone['name'])
            Phone.objects.create(id=phone['id'],
                                 name=phone['name'],
                                 image=phone['image'],
                                 price=phone['price'],
                                 release_date=release_date,
                                 lte_exists=phone['lte_exists'],
                                 slug=slug,
                                 )
