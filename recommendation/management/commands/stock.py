from recommendation.models import Stock, Sector, Industry
from django.core.management.base import BaseCommand
import json
import os

#csv file path for stocks
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                        '_sp_stock_2019.json')
class Command(BaseCommand):
    help = 'Populate db with Stocks'

    def handle(self, *args, **options):
        with open(path, 'r') as file:
            reader = json.load(file)
           # sector = Sector.objects.get(pk=all)
           # industry = Industry.objects.all()
            #print (sector)
            for row in reader:
                print(row["Sector"])
                sector = Sector.objects.get(name=row["Sector"])
                industry = Industry.objects.all()
                print(row['Ticker'])
                print(row['Industry'], Industry.objects.get(name=row["Industry"]).id)
                created = Stock.objects.get_or_create(
                    ticker=row["Ticker"],
                    name=row["Name"],
                    description=row["Description"],
                    #GICS_sector=row["GICS Sector"],
                    sector_id=Sector.objects.get(name=row["Sector"]).id,
                    industry_id=Industry.objects.get(name=row["Industry"]).id,
                    Female_exec=(row["Female_Exec"]>=1), # do I add >= 1??
                    risk=(row["Risk"] >= 1.3),
                    csr=row["Csr"],
                    hr=row["Hr"],
                )
                self.stdout.write(' created: ' + str(created))