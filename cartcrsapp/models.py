from django.db import models

# Create your models here.
class Datas(models.Model):
    message = models.CharField(max_length=50,default="")
    name = models.CharField(max_length=20,default="")
    mail = models.CharField(max_length=50,default="")
    number = models.IntegerField(default="")
    
    

class Appointment(models.Model):
    date = models.DateField()
    department = models.CharField(max_length=100,default="")
    doctor = models.CharField(max_length=100,default="")
    name = models.CharField(max_length=100,default="")
    phone = models.CharField(max_length=20,default="")
    email = models.EmailField(max_length=50,default="")

    # Optionally, add any additional fields or methods as needed
 
    
   