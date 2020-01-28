import psycopg2
from django.utils import timezone
from django.core.management import BaseCommand
from itembase.core.models import VineVendorImport


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        filename = 'vine_user_1/test.csv'
        conn = psycopg2.connect("host=localhost dbname=ibase user=felix password=Ch3nna12016")
        cur = conn.cursor()
        with open('itembase/media/' + filename, 'r') as source:
            next(source)
            cur.copy_from(source, 'public.core_vinevendorimport', sep='|',
                          columns=['vendor_code', 'name', 'addr1', 'addr2', 'addr3', 'city', 'state',
                                   'zipcode', 'phone', 'extension', 'salesperson_name', 'salesperson_email',
                                   'salesperson_phone'])

        conn.commit()

        VineVendorImport.objects.filter(created_on__isnull=True).update(created_on=timezone.now())
        VineVendorImport.objects.filter(source__isnull=True).update(source=filename)
