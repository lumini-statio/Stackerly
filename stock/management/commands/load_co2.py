from django.core.management.base import BaseCommand
from django.conf import settings
import csv
from datetime import date
from itertools import islice
from stock.models import CO2


class Command(BaseCommand):
    help = 'Load CSV data from CO2 file'

    def handle(self, *args, **kwargs):
        datafile = settings.BASE_DIR / 'data' / 'co2.csv'

        with open(datafile, 'r') as file:
            reader = csv.DictReader(islice(file, 40, None))

            for row in reader:
                dt = date(
                    year=int(row['year']),
                    month=int(row['month']),
                    day=1
                )

                CO2.objects.get_or_create(date=dt, average=float(row['average']))
