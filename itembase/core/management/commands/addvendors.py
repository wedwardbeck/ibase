import csv
from django.core.management import BaseCommand
from itembase.core.models import Vendor


class Command(BaseCommand):
    help = 'Load a vendor csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, newline='') as csvfile:
            contsuccess = 0
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            print('Loading...')
            for row in reader:
                Vendor.objects.create(name1=row[0], name2=row[1], taxid=row[2], status=row[3], created_by=row[4])
                contsuccess += 1
            print(f'{str(contsuccess)} inserted successfully! ')
