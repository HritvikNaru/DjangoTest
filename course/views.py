from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Student,ContactForm,Stocks,Cart,Orders
from .serializers import StudentSerializer, StudentReadSerializer,contactformSerializer,StockSerializer
# from rest_framework import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
import json
from ast import literal_eval




#because httpResponse is a class so we need to import it before using it
# Create your views here.

# variables for testing
# nm=""
# idn=10 

#adding the stocks to cart
def addtocarts(request):
    if request.method == 'POST':
            post=Cart()
            stock_idval= request.POST.get('addcart')
            post.stock_id= Stocks.objects.get(id=stock_idval)
            post.cus_id= ContactForm.objects.get(id=idn)
            post.save()
                
            return redirect('/shopping')  

    else:
            return redirect('/shopping')
    

#displating the stocks
def showcart(request):
    id_set=[]
    allcartobjects= Cart.objects.filter(cus_id_id=idn)
    list=allcartobjects.values()
    # context= {'all_objects': allcartobjects}
    # serializer = StockSerializer(data) #converted to python object
    # json_data = JSONRenderer().render(serializer.data) #python to json 
    # return HttpResponse(json_data, content_type='application/json') #sent json to client
    for i in list:
        id_set.append(i['stock_id_id'])
    # print("ser::", list[0]['id'])
    print("set::",id_set)
    objects = Stocks.objects.filter(id__in=id_set)
    list1=objects.values()
    print(list1)
    # print("data::", data)
    
    return render(request,"coursetemplates/cart.html",{'list1':list1,'name':nm})



#Deleting the cart
def cartdelete(request):
    if request.method == 'POST':
        delid=request.POST.get('deletecart')
        print(delid)
        Cart.objects.filter(stock_id_id=delid).delete()
        return redirect('/showcart')  
    return redirect('/showdelete')  




# contactdetails added to the database
def showform(request):
        if request.method == 'POST':
            post=ContactForm()
            post.fname= request.POST.get('Fname')
            post.lname= request.POST.get('Lname')
            post.number= request.POST.get('Mobileno')
            post.email= request.POST.get('email')
            post.password= request.POST.get('Password')
            post.Address= request.POST.get('address')

            post.save()
                
            return redirect('/register')  

        else:
            return redirect('/register')


#placing the orders from the cart
def ordersplaced(request):
    if request.method == 'POST':
        post=Orders()
        allobj=Cart.objects.filter(cus_id_id=idn)
        for i in allobj.values():
            post=Orders()
            print(i)
            post.stock_id= Stocks.objects.get( id=i['stock_id_id'])
            post.cus_id= ContactForm.objects.get(id=idn) 
            post.save()
        Cart.objects.filter(cus_id_id=idn).delete()
        return redirect("/showorder")

    
    return redirect("/showorder")

#Displaying the orders
def showorders(request):
    id_set=[]
    allorderedobjects= Orders.objects.filter(cus_id_id=idn)
    list=allorderedobjects.values()
    # context= {'all_objects': allcartobjects}
    # serializer = StockSerializer(data) #converted to python object
    # json_data = JSONRenderer().render(serializer.data) #python to json 
    # return HttpResponse(json_data, content_type='application/json') #sent json to client
    for i in list:
        id_set.append(i['stock_id_id'])
    # print("ser::", list[0]['id'])
    print("set::",id_set)
    objects = Stocks.objects.filter(id__in=id_set)
    list1=objects.values()
    print(list1)
    # print("data::", data)
    return render(request,"coursetemplates/orders.html",{'list1':list1,'name':nm})






# fetch inventory data and display to the customer
def shopping(request):
    all_objects= Stocks.objects.all()
    list=all_objects.values()
    # context= {'all_objects': all_objects}
    # serializer = StockSerializer(data) #converted to python object
    # json_data = JSONRenderer().render(serializer.data) #python to json 
    # return HttpResponse(json_data, content_type='application/json') #sent json to client
    # print("ser::", context.get('stock_type'))
    # print("data::", data)
    return render(request,"coursetemplates/shopping.html",{'list1':list,'name':nm})
    
# def showform(request):
#     print(request.body)
#     form= FormContactForm(request.POST or None)
#     if form.is_valid():
#         print("hello haan valid hai")
#         form.save()
  
#     context= {'form': form }
        
#     return render(request,'coursetemplates/register.html', context)

#for signin 

def signin(request):
    return render(request,"coursetemplates/signin.html")

# for registration

def register(request):
    return render(request,"coursetemplates/register.html")


def learn_django (request):
    return HttpResponse("<h1> hello django course</h1>")


# contact details fetched here and can be used for signin

def contactdetails(request):
    if request.method == 'POST':
            emaildata= request.POST.get('email')
    stu=ContactForm.objects.get(email=emaildata)   #model object created(complex) 
    serializer = contactformSerializer(stu) #converted to python object
    json_data = JSONRenderer().render(serializer.data) #python to json 
    resp = json.loads(json_data)
    print(resp['fname'])
    global nm
    global idn
    print(stu.id)
    nm=resp['fname']
    idn=stu.id
    # return render(request,"feetemplate/hello.html",{'month':12})
    return render(request,"coursetemplates/index.html",{'name':nm})
    # return HttpResponse(json_data, content_type='application/json') #sent json to client
    # result=JsonResponse(serializer.data)
    
    # return result
    # json_str = json.dumps(result)
    # # load the json to a string
    

    # return resp



# These api's are practice api'


def student_detail(request,pk):
    stu=Student.objects.get(id=pk)   #model object created(compolex) 
    serializer = StudentSerializer(stu) #converted to python object
    # json_data = JSONRenderer().render(serializer.data) #python to json 
    # return HttpResponse(json_data, content_type='application/json') #sent json to client


    return JsonResponse(serializer.data)




@csrf_exempt
def stucreate(request):
    if request.method == 'POST':
        
        print('req.data:::', request.body, type(request.body))

        jsondata=request.body
        print(type(jsondata))
        my_dict = literal_eval(jsondata.decode('utf-8'))
        print(my_dict,"hello")  
        print(type(my_dict)) 
        serializer=StudentSerializer(data=my_dict)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data= serializer.validated_data
        print('data::', data,type(data))
        data = StudentReadSerializer(data).data
        print('res:::', data,type( data))
            # serializer.save()
            # res={'msg': 'Data Created'}
            # print('1')
            # jsondata=JSONRenderer.render(request.POST,res)
            # print('2')
            # return HttpResponse(jsondata,content='application/json')
        # jsondata = JSONRenderer.render(request.POST,serializer.errors)
        return HttpResponse(dict(data))
        

