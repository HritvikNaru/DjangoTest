from rest_framework import serializers
from .models import Student,ContactForm,Stocks
class StudentSerializer (serializers.ModelSerializer):
    name=serializers.CharField(max_length=100, required=True)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=200)
    class Meta:
        model = Student
        fields = (
            'name',
            'roll',
            'city'
        )



class StockSerializer (serializers.ModelSerializer):
    stock_type= serializers.CharField(max_length=100)
    stock_desc= serializers.CharField(max_length=200)
    price= serializers.IntegerField()
    quantity= serializers.IntegerField()
    class Meta:
        model = Stocks
        fields = (
            'stock_type',
            'stock_desc',
            'price',
            'quantity'
        )




class contactformSerializer(serializers.ModelSerializer):
    fname= serializers.CharField(max_length=100)
    lname= serializers.CharField(max_length=100)
    number= serializers.CharField(max_length=50)
    email= serializers.EmailField()
    password=serializers.CharField(max_length=50)
    Address= serializers.CharField(max_length=200)
    class Meta:
        model = ContactForm
        fields = (
            'fname',
            'lname',
            'number',
            'email',
            'password',
            'Address'
        )


class StudentReadSerializer (serializers.ModelSerializer):
    name=serializers.CharField(max_length=100)
    class Meta:
        model = Student
        fields = (
            'name',
        )