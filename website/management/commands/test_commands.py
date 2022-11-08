from website.models import Sefer, PrimaryCategory


from django.core.management.base import BaseCommand

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
# so far this gets me 41 objects 
class Command(BaseCommand):
    def handle(self, *args, **options):
        #grab the api and i think switch it out of json. Dont remember what I did. 
        r = requests.get("http://www.sefaria.org/api/index/")
        data = json.loads(r.text)
        
        z = 0
        x = 0 
        y= 0

        # # while z < 10000:
        # #     try:
        # # while y < 1000:
        # #     try:
        # while x < 1000:
        #     try:
        #         primary = object['categories'][0]
        #         id = PrimaryCategory.objects.get(name = primary)
        #         title = object['title']
        #         # new = Sefer(book = title, prime_cat = id)
        #         print("we got here", title)
        #         # new.save()
        #         x += 1 
        #         print(x)
        #     except: IndexError
        #     y = y +1 
        #     x = 0  
        #     break        
        #     # except:
        #     #     break
        #     #     z = z +1 
        #     # except:
        #     #     break 

        while z < 1000:
            try:
                while y < 1000:
                    try:
                        while x < 1000:
                            try:
                                object = (data[z]['contents'][y]['contents'][x])
                                primary = object['categories'][0]
                                id = PrimaryCategory.objects.get(name = primary)
                                title = object['title']
                                print("before save", primary, title, id)
                                new = Sefer(book = title, prime_cat = id)
                                new.save()
                                print("after save", title, id)  
                                x += 1     
                            except: IndexError
                            x = 0 
                            break 
                        y = y +1     
                    except: 
                        y = 0 
                    break 
                z = z +1 
            except: 
                break 