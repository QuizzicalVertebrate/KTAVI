import csv 

# from website.models import Order

# x = Order.objects.all()
# print(x[1])

#this allows me to pull the strings out of a csv as a list so its easy to index the parts that i
# need.
with open("C:\Coding\Hatchalot_Kashot\Zeraim_index.csv", 'r', encoding="utf8") as file:
    csvreader = csv.reader(file)
    for x in csvreader:
        print(x[8])
        



