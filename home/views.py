from django.shortcuts import render
from django.http import HttpResponse

def home(request): 
    peoples = [
        {'name' : 'abhijeet gupta','age':26},
        {'name' : 'rohan sharma','age':23},
        {'name' : 'vicky kaushal','age':24},
        {'name' : 'depanshu chorishya','age':17},
        {'name' : 'sandeep','age':63}

    ]
    
    return render(request , "home/index.html" , context= {'peoples':peoples})

def about(request):
    return render(request,"home/about.html")

def contact(request):
    return render(request,"home/contact.html")

def success_page(request):
    return HttpResponse("<h1>Hey this is a Success page</h1>")

