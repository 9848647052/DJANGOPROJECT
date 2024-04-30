from django.db import models

# Create your models here.
class Farm(models.Model):
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    mdate=models.DateField()
    price=models.IntegerField()


class vegetables(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()

    def __str__(self):
        return self.name 
    

class customer(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name