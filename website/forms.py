from django import forms
# Import the forms library
from .models import Order, PrimaryCategory, QuaternaryCategory, SecondaryCategory, TertiaryCategory
from dynamic_forms import DynamicField, DynamicFormMixin

class OrderForm(forms.ModelForm):
    class Meta():
        model = Order
        fields = '__all__'
#this implementation failed cuz of the htmx part of the jinja for reasons i cant fathom
class OrderForm2(DynamicFormMixin, forms.Form):

    def query_func(form2):
        primary_category = form2['text'].value()
        
        return SecondaryCategory.objects.filter(primary_category = primary_category )

    def initial_text(form2):
        primary_category = form2['text'].value()
        
        return SecondaryCategory.objects.filter(primary_category = primary_category ).first()


    text = forms.ModelChoiceField(
        queryset= PrimaryCategory.objects.all(),
        initial= PrimaryCategory.objects.first(),
    )

    text2 = DynamicField(forms.ModelChoiceField, queryset = query_func, initial = initial_text)




