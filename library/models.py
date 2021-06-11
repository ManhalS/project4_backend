from booko.settings import DEFAULT_AUTO_FIELD
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 255)
    num_pages= models.IntegerField(default=0)
    isbn = models.CharField(max_length=13,blank=True, null=True )
    publish_date =models.IntegerField(default=0,blank=True, null =True)
    FileBook = models.FileField(default='', blank= False, null=False )
    
    
    def __str__ (self):
        return self.title
    
