#for each individual item i need to know which things its downstream of. The primary cat is in 
# the thing itself but iirc only that the program needs to grab the names of the things as we 
# go down.

import requests, json, pandas as pd

r = requests.get("http://www.sefaria.org/api/index/")

data = json.loads(r.text)

#this is the whole api result to play with in the terminal 
# object = (data[0]['contents'][0]['contents'][0])

#this is the program to export specific results to the csv. What needs to be done is to get it to 
# run in each part until it hits no result that makes sure to get all the objects.

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
       
        lst = []
        x = 0 
        y= 0 
        while x < 12:
            object = (data[x]['contents'][0]['contents'][0])
            x += 1 
            print(object)

# dct = {'secondary_category': lst }
# df = pd.DataFrame(dct)
# df.to_csv('secondary_categories.csv')