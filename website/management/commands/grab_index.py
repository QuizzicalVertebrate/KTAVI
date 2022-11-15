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

# from django.core.management.base import BaseCommand

# class Command(BaseCommand):
#     def handle(self, *args, **options):
       
#         lst = []
#         x = 0 
#         y= 0 
#         try: 
#             while x < 50:
#                 object = (data[13]['contents'][x]['contents'][y])
#                 x += 1 
#                 lst.append(object)
#         except:
#             pass

# dct = {'secondary_category': lst }
# df = pd.DataFrame(dct)
# df.to_csv('secondary_categories.csv')

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
#the q is the conceptual mistake. I cant reset the var in the loop beofre the break cuz.
#thats just an infinite loop 
        while z < 5:
            try:
                #this is a chap. I used the object itself in a try to know when to break out. But 
                #it doesnt fail on nested objects so really need to be more direct and check for 
                #something that fits the right model. Really thats the need here to find all the 
                #objects that have a title and categories list recursively 
                object = (data[z]['contents'][y]['contents'][x])
                print("z =", z)
                while y < 5:
                #cant zero out x in the x loop 
                    try:
                        object = (data[z]['contents'][y]['contents'][x])
                        print("y =", y)
                        while x < 10:
                            try:
                                object = (data[z]['contents'][y]['contents'][x])
                                primary = object['categories'][0]
                                ident = PrimaryCategory.objects.get(name = primary)
                                title = object['title']
                                print("before save", primary, title, id)
                                #all this is still missing the fields for the other cats
                                #if i use .pk the save doesnt work and fails silently
                                new = Sefer(book = title, prime_cat = ident)
                                print("where save would be")
                                # new.save()
                                print("after save", title, ident)  
                                x += 1 
                                print("x =", x)    
                            except: 
                                break
                        y += 1 
                        x = 0 
                    except: # what i really need is the ability to stop once i run out of ys
                        #but im not going to hit a index error cuz im not actually manipulating 
                        #the y just incrementing it there is a var i dont have i really want to 
                        #trigger it when the x hits an except but i cant use that cuz thats the 
                        #trigger for the y incrementing. I can maybe do recursive if it hits itself
                        #or something. Answer i can try and find the answer at the top of the loop 
                        #and see if i get a key error  
                        print("hit the except on y")
                        break          
                z += 1 
                y = 0 
            except: 
                print("all done")
                break