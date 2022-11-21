from tkinter import CASCADE
from django.db import models

class Order(models.Model):
    text = models.CharField(max_length= 100, blank= True)
    translation = models.CharField(max_length= 100, blank= True)
    paperhight = models.IntegerField(default=10)
    paperwidth = models.IntegerField(default=10)
    # hebfont = models.CharField(max_length= 100, blank= True)
    # hebboldfont = models.CharField(max_length= 100, blank=True)
    # engfont = models.CharField(max_length= 100, blank= True)
    # top = models.IntegerField(default=10)
    # bottom = models.IntegerField(default=10)
    # inner = models.IntegerField(default=10)
    # outer = models.IntegerField(default=10)
    # fontsize = models.IntegerField(default=10)
    # spacing = models.IntegerField(default=10)
    # newpage = models.IntegerField(default=10)
    # layout = models.CharField(max_length= 100, blank= True)
    # parskip = models.IntegerField(default=10)
    # pagenumloc = models.CharField(max_length= 100, blank= True)
    # pagenumheb = models.IntegerField(default=10)
    # headpos = models.CharField(max_length= 100, blank = True)
    # evenhead = models.CharField(max_length= 100, blank= True)
    # oddhead = models.CharField(max_length= 100, blank= True)
    # chapfontsize = models.IntegerField(default=10)

    def __str__(self):
        return self.text


class Translation(models.Model):
    translation = models.CharField(max_length=100, blank= True)
    
    def __str__(self):
        return self.translation

class PrimaryCategory(models.Model):
    name = models.CharField(max_length= 50, default='we have a miss here', unique = True)

    def __str__(self):
        return self.name

class SecondaryCategory(models.Model):
    name = models.CharField(max_length= 50, default='we have a miss here')
    primary_category = models.ForeignKey(PrimaryCategory, 
    on_delete= models.CASCADE, related_name='secondary_category')

    def __str__(self):
        return self.name 

# class TertiaryCategory(models.Model):
#     name = models.CharField(max_length= 50, default='we have a miss here')
#     category_two = models.ForeignKey(SecondaryCategory, 
#     on_delete= models.CASCADE, null = True, related_name='tertiary_category')

#     def __str__(self):
#         return self.name 


# class QuaternaryCategory(models.Model):
#     name = models.CharField(max_length= 50, default='we have a miss here')
#     category_three = models.ForeignKey(TertiaryCategory, 
#     on_delete= models.CASCADE, null = True, related_name='quaternary_category')

#     def __str__(self):
#         return self.name 

class Sefer(models.Model):
    book = models.CharField(max_length= 100, blank= True, primary_key= True)
    prime_cat = models.ForeignKey(PrimaryCategory, 
    on_delete= models.CASCADE,  null = True, related_name= 'prime_cat')
    secondary_cat = models.ForeignKey(SecondaryCategory, 
    on_delete= models.CASCADE, null = True, related_name= 'secondary_cat', blank = True)
    # tertiary_cat = models.ForeignKey(TertiaryCategory, 
    # on_delete= models.CASCADE, null = True, related_name= 'tertiary_cat', blank = True)
    # quaternary_cat = models.ForeignKey(QuaternaryCategory, 
    # on_delete= models.CASCADE, null = True,  related_name= 'quaternary_cat', blank = True)
    
    def __str__(self):
        return '{} - {} ({})'.format(self.pk, self.book, self.prime_cat, self.secondary_cat)
