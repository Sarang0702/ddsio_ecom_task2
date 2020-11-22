from django.db import models

# class User(models.Model):
#
#     Name = models.CharField(max_length=30)
#     Mob = models.CharField(primary_key=True,max_length=13)
#     Email = models.EmailField(unique=True)
#     DOB =  models.DateField()
#     Pin = models.IntegerField()
#     Password = models.CharField(max_length=30)
#

class Product(models.Model):
    Name = models.CharField(max_length=20)
    Price = models.DecimalField(decimal_places=2,max_digits=10)
    Image = models.ImageField(upload_to='product_images/')
    Description = models.TextField(max_length=60)
    Category = models.CharField(max_length=15)

    def __str__(self):
        return self.Name