from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class User(models.Model):
     name= models.CharField(max_length=200)
     EmailField = models.CharField(max_length=200)
     password= models.CharField(max_length=200)
     fileupload = models.FileField (upload_to =user_directory_path)
     
     def __str__(self):
         return self.name
class Book(models.Model):
    title= models.CharField(max_length=100)
    author= models.CharField(max_length=100)
    year = models.IntegerField(blank=True, null=True)
    filedownload =models.Filefiled(download_to = user_directory_path)
    
    def __str__(self):
        return self.title