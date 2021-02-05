from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    print('hi')

    def handle(self, *args, **options):
        print('yo')

        self.stdout.write(self.style.SUCCESS('Successfully exexuted reddit'))