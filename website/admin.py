from django.contrib import admin
from import_export import resources
from .models import (Order, SecondaryCategory, Sefer, 
PrimaryCategory, TertiaryCategory, QuaternaryCategory, Translation)

# Register your models here.

admin.site.register(Order)
admin.site.register(Sefer)
admin.site.register(PrimaryCategory)
admin.site.register(SecondaryCategory)
admin.site.register(TertiaryCategory)
admin.site.register(QuaternaryCategory)
admin.site.register(Translation)


class BookResource(resources.ModelResource):

    class Meta():

        model = PrimaryCategory


