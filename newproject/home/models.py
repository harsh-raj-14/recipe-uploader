from django.db import models

# Create your models here.
class Student(models.Model):
    #id=models.AutoField() #->automatic by django
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    image=models.ImageField()
    file=models.FileField()

class Product(models.Model):
    pass

class Car(models.Model):
    car_name=models.CharField(max_length=500)
    speed=models.IntegerField(default=50)
    
    def __str__(self)->str:
        return f"Car: {self.car_name}, Speed: {self.speed}"