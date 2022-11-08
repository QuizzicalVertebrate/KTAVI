#finally managed to get management commands to do something here need the setup of management/commands
# in the app the class and inheritence and the handle function with those args to get it to work
# Finally finally figured out how to import and to run as management commands
# can add a guard if the cat already exists but cuz its just me i dont need it
# You get a QuerySet by using your model’s Manager
# . Each model has at least one Manager, and it’s called objects by default.. 

from django.core.management.base import BaseCommand
import csv
from website.models import PrimaryCategory, Translation, Order

class Command(BaseCommand):
    def handle(self, *args, **options):
#use csv to create objects in a model class if they are not already present.        
        with open("C:\Coding\Hatchalot_Kashot\primary_categories.csv", 'r', encoding="utf8") as file:
            csvreader = csv.reader(file)
            for x in csvreader:
                # y = x[8]
                previous = PrimaryCategory.objects.all()
                if x in previous:
                    break
                else: 
                    new = PrimaryCategory(name = x[1])
                    new.save()    
           
        
        
x = Translation.objects.all()

# print(x)
    
    
    

#     help = "creates a new model object for the translation category"
#     def create_new_object(model, trans):
#         new = model(translation = trans)
#         new.save()
        



    


