from django.db import models


# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    city=models.CharField(max_length=200)




class ContactForm(models.Model):
    fname= models.CharField(max_length=100)
    lname= models.CharField(max_length=100)
    number= models.CharField(max_length=50)
    email= models.EmailField()
    password=models.CharField(max_length=50)
    Address= models.CharField(max_length=200)


class Stocks(models.Model):
    stock_type= models.CharField(max_length=100)
    stock_desc= models.CharField(max_length=200)
    price= models.IntegerField()
    quantity= models.IntegerField()



class Cart(models.Model):
    cus_id=models.ForeignKey(ContactForm , on_delete=models.CASCADE)
    stock_id=models.ForeignKey(Stocks, on_delete=models.CASCADE)


class Orders(models.Model):
    cus_id=models.ForeignKey(ContactForm , on_delete=models.CASCADE)
    stock_id=models.ForeignKey(Stocks, on_delete=models.CASCADE)
    
   
