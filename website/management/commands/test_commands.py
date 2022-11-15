from website.models import Sefer, PrimaryCategory, SecondaryCategory


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
                        #using the try on the obejct as a proxy for where I want the loop to end
                        #itll trigger the except when there is no object 
                        object = (data[z]['contents'][y]['contents'][x])
                        print("y =", y)
                        while x < 13:
                            try:
                                object = (data[z]['contents'][y]['contents'][x])
                                print("x =", x)  
                                primary = object['categories'][0]
                                id = PrimaryCategory.objects.get(name = primary)
                                print("primary", primary, type(primary))

                                try:
                                    print("secondary try block start")
                                    secondary = object['categories'][1]
                                    print(secondary, type(secondary))
                                except:
                                    print("no secondary")
                                    pass
                                if SecondaryCategory.objects.filter(name = secondary).exists():
                                    print("we already have this one ")
                                    #there is a potential issue here dependent on how the id works
                                else:
                                    print("else ")
                                    new_sec_cat = SecondaryCategory(name = secondary, primary_category = id)
                                    print("new_sec_cat before save")
                                    new_sec_cat.save()
                                    print("new sec cat saved succesfully")
                                #right now failing on x = 1 cuz there are two secondary cats with
                                #the same name and there is no way to get request them 
                                sec_id = SecondaryCategory.objects.get(name = secondary)
                                print("type foriegn key", id, type(id))
                                title = object['title']
                                print("before save", primary, title, id)
                                #all this is still missing the fields for the other cats
                                #if i use .pk the save doesnt work and fails silently
                                #IMPORTANT the try block is on every piece. The new is failinhg here 
                                #which punches it bac to the y loop it was working before. I think
                                #its cuz of the new secondary in the model object
                                print("after save", title, id)  
                                if Sefer.objects.filter(book = title).exists():
                                    print("we already have this sefer")
                                    #there is a potential issue here dependent on how the id works
                                else:
                                    print("else sefer ")
                                    new1 = Sefer(book = title, prime_cat = id,  secondary_cat = sec_id)
                                    print("else sefer before save")
                                    new1.save()
                                    print("new sefer saved succesfully")
                                x += 1   
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