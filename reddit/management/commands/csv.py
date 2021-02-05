import csv

from django.core.management.base import BaseCommand, CommandError

from reddit.models import Tickers


class Command(BaseCommand):
    print('hi')

    def handle(self, *args, **options):
        tickers = Tickers.objects.all()
        # Tickers.objects.all().delete()
        with open('reddit/tickers/amex.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                print(row[0])
                print(row[1])
                tickers .get_or_create(
                    symbol=row[0],
                    full_name=row[1]
                )

        with open('reddit/tickers/nyse.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                print(row[0])
                print(row[1])
                tickers .get_or_create(
                    symbol=row[0],
                    full_name=row[1]
                )

        with open('reddit/tickers/nasdaq.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                print(row[0])
                print(row[1])
                tickers .get_or_create(
                    symbol=row[0],
                    full_name=row[1]
                )


        self.stdout.write(self.style.SUCCESS('Successfully exexuted csv'))