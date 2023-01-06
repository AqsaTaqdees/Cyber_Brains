from django.db import models
import datetime
#from django import forms
#from django_countries.fields import CountryField

#makemigrations means create changes and store in a file
#migrate means apply pending changes created by makemigrations

#Model is used to define database.
# Create your models here. 
class Contact(models.Model):
    firstName=models.CharField(max_length=122,default='anonymous')
    lastName=models.CharField(max_length=122,default='fighter')
    email=models.CharField(max_length=122,default='email')
    phone=models.CharField(max_length=12,default='+92')
    desc=models.TextField(default='Description')
    date=models.DateField(default=datetime.date.today())
    #used to show name of that person who enters the data in table of database
    def __str__(self):
        return self.firstName