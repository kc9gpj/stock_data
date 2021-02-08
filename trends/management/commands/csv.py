import csv

from django.core.management.base import BaseCommand, CommandError

from trends.models import Tickers


class Command(BaseCommand):
    def handle(self, *args, **options):
        file_locations = ['trends/tickers/amex.csv', 'trends/tickers/nyse.csv',
                'trends/tickers/nasdaq.csv', 'trends/tickers/etf.csv']
        tickers = Tickers.objects.all()
        Tickers.objects.all().delete()
        for files in file_locations:
            with open(files, 'r') as csv_file:
                reader = csv.reader(csv_file)

                for row in reader:
                    print(row[0])
                    print(row[1])
                    tickers .get_or_create(
                        symbol=row[0],
                        full_name=row[1]
                    )


        self.stdout.write(self.style.SUCCESS('Successfully exexuted csv'))