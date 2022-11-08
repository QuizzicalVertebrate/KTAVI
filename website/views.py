from gettext import translation
from django.shortcuts import render
from numpy import require
from . forms import OrderForm
from django.views.decorators.http import require_POST
from .models import Order, PrimaryCategory, SecondaryCategory, TertiaryCategory, Sefer, Translation
from .forms import OrderForm2


def base(request):
    return render(request, 'base.html')

def input(request):
#create an instance of the orderform object
    Input_Form = OrderForm()
    class_object = Translation.objects.all()
    primary_categories = PrimaryCategory.objects.all()
# gets the data back from the final div that displays the last choice which has the name attrib
# final choice but this only works becuase I know what category it comes from. more work 
# would be needed to allow it to handle something from every choice and the defualts worked fine
# if there is no imput in the select box it does not come back as as none but as open this select 
# menu.
    if request.method == 'POST':
        if request.POST['final choice'] == int:
            data = request.POST['final choice']
            trans = request.POST['translation']
            t = TertiaryCategory.objects.get(pk = data)
            n = Translation.objects.get(pk=trans)
            new = Order(text =t, translation = n)
            new.save()
        else: 
            data = request.POST['secondary_category']
            trans = request.POST['translation']
            t = SecondaryCategory.objects.get(pk = data)
            n = Translation.objects.get(pk=trans)
            new = Order(text = t, translation = n)
            new.save()
# i have the id number of the object in the category. I need to grab the name. To do that i need 
#to grab the category and..
    
    context = {'form': Input_Form, 'primary_categories': primary_categories,'class_object': class_object}

    return render(request, 'input.html', context)


def fake_api(request):

    print("success")


    user_choice_key = request.GET.get('primary_category')



    print(user_choice_key )

    


    secondary_category = SecondaryCategory.objects.filter(primary_category=user_choice_key )

    print(secondary_category)

    context = {'secondary_category': secondary_category}

    return render (request, 'partials/secondaries', context)


def fake_api2(request):
    print("success2")
    
    user_choice_key_2 = request.GET.get('secondary_category')
    
    tertiary_category = TertiaryCategory.objects.filter(category_two=user_choice_key_2 )

    
    # v = tertiary_category
# whats being printed here now is a proxy for the actual sefer selected. In a final model this will
# have all the proper info already there so I dont have to use any information from the previous choices 
# I just have to grab this one and save it into the order model to pass to the program. 
    
    
    
    
    # if request.method == 'POST':
    #     final_choice = request.POST['test'] 
    #     print(final_choice, "hello")

    # test = Order(text = v)

    # test.save()


    context = {'tertiary_category': tertiary_category}

    return render (request, 'partials/tertiaries.html', context)


def test(request):
#instantiate a instance of the form by calling it as a function. It takes the post(how?)
# this gives me the form with the data its clear that the form can both be the blank version 
# and the one with the .
    form = OrderForm(request.POST)
    class_object = Translation.objects.all()
    context = {'form': form, 'class_object': class_object}

    if form.is_valid():
        n = form.cleaned_data['text']
        s = Sefer(book = n, primary_category = "hellooooo")
        s.save()
       
    return render (request, 'test.html', context)