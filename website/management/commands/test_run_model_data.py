from website.models import Sefer
import pandas as pd 
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):

        qs = Sefer.objects.get(pk = 100)
        print(qs)
        # q = qs.values('book', 'prime_cat', "secondary_cat")
        # df = pd.DataFrame.from_records(q)
        # print(df.head())
        