from django.db import models

# Create your models here.

class Category(models.Model):

   name = models.CharField(max_length=100)

   description = models.TextField()

 

   def __str__(self):

       return self.name

class Product(models.Model):

   category = models.ForeignKey(Category, on_delete=models.CASCADE)

   name = models.CharField(max_length=100)

   price = models.IntegerField()

   stock = models.IntegerField()

   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):

       return self.name