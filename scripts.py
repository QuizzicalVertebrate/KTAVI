import requests 
import json 
import pandas as pd



# book_resource = resources.modelresource_factory(model=PrimaryCategory)()
# dataset = tablib.Dataset(['', 'New book'], headers=['id', 'name'])
# result = book_resource.import_data(r'C:\Coding\Hatchalot_Kashot\primary_categories.csv', dry_run=True)
# print(result.has_errors())

# from website.models import PrimaryCategory


r = requests.get("http://www.sefaria.org/api/index/")

data = json.loads(r.text)

object = (data[0]['contents'][5]['contents'][0]['contents'][0]["contents"][0])
for x in object['categories']:
    print(x)

print(object)
#grab a object and grab its categories in order and send them to the right spots on the model
# object 
# there is a question im strigling with here which is how to have a loop unfold with diff actions
# depending on if it keeps unfolding its not a simple for loop cuz i dont want to do the same
# thing to each spot on the loop what i really want to do is use the loop as a list and index
# the list so that gives me the answer cuz its already a list i just need to check for nulls
# which means wrapping it in a try except.



# object = (data[13]['contents'][2]['contents'][2])
# title = object['categories']
# x = title[0]
# try:
#     y = title[1]
#     print(y)
# except:
#     print("that didnt work at step 2")
# try:
#     z = title[2]
#     print(z)
# except:
#     print("that didnt work at step 3")




 
# while x < 100:
#     object = (data[13]['contents'][y]['contents'][x])
#     lst.append()
 
        
#need a loop here that loops through each of the 13 cats and goes down and gets each 
# lst = []
# x = 0 
# while x < 5:
#     object = (data[0]['contents'][0]['contents'][x])
#     x += 1 
#     lst.append(object['title'])

# dct = {'secondary_category': lst }
# df = pd.DataFrame(dct)
# df.to_csv('secondary_categories.csv')

# # object = (data[0]['contents'][0]['contents'])

# # print(data)
# x = 0   
# lst = []
# while x < 12:
#     try:
#         object = (data[x]['contents'][0]['contents'][0])
#         lst.append(object['primary_category'])
#         x += 1
#     except:
#         object = (data[x]['contents'][0]['contents'][0]['contents'][0]) 
#         lst.append(object['primary_category'])
#         x += 1
# dct = {'primary_category':lst}
# df = pd.DataFrame(dct)  
# df.to_csv('primary_categories.csv')
# test =  object = (data[2]['contents'][0]['contents'][0]['contents'][0])
# print(test['primary_category'])

# # def get__text_by_numberinsubcategory(x = int, y = int ):
# #     r = requests.get("http://www.sefaria.org/api/index/")
# #     data = json.loads(r.text)
# #     # object = (data[3]['contents'][0]['contents'][3])
# #     category = object = (data[x]['contents'][0]['contents'][0]['categories'])
# #     object = (data[x]['contents'][0]['contents'][y])
# #     return print(category, '\n', object) 



# # get__text_by_numberinsubcategory(3, 3)


# # r = requests.get("http://www.sefaria.org/api/titles/Chiddushei_Ramban_on_Niddah")
# # data = json.loads(r.text)
# # print(data)
# # data = json.loads(r.text)
# # # object = (data[3]['contents'][0]['contents'][3])
# # # category = object = (data[x]['contents'][0]['contents'][0]['categories'])
# # object = (data[3]['contents'][0]['contents'][3])

# # df = pd.DataFrame.from_dict(object).to_csv('take2.csv')

# # df = pd.DataFrame.from_dict(data).to_csv('take3.csv')




# # print(df)






# # print(data[0]['contents'][0]['contents'][0]['enShortDesc'])

# # print(data[3]['contents'][0]['contents'][3])


# # def get_sefaria_objects():
# #     r = requests.get("http://www.sefaria.org/api/index/")
# #     data = json.loads(r.text)























