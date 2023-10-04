from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse
from vege.views import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/login/")
def notices(request):
    if request.method == "POST":
      

      data = request.POST

      notice_name = data.get('notice_name')
      notice_description = data.get('notice_description')
      
      Noticehub.objects.create(
         
      notice_name = notice_name,
      notice_description = notice_description,
         
      )

      return redirect('/notices/')
    
    queryset = Noticehub.objects.all()

    if request.GET.get('search'):
       queryset = queryset.filter(notice_name__icontains = request.GET.get('search'))

    context = {'notices': queryset}
      
    
    return render(request , 'notices.html', context)


def update_notice(request,id):
    queryset = Noticehub.objects.get(id = id)

    if request.method == "POST":
       data = request.POST
       notice_name = data.get('notice_name')
       notice_description = data.get('notice_description')
       queryset.notice_name = notice_name
       queryset.notice_description = notice_description
       queryset.save()
       return redirect('/notices/')
    



    context = {'notice': queryset}
    return render(request , 'update_notices.html', context)
   
   

def delete_notice(request,id):
   
   queryset = Noticehub.objects.get(id = id)
   queryset.delete()
   
   return redirect('/notices/')


def login_page(request):

   if request.method == "POST":
      username = request.POST.get('username')
      password = request.POST.get('password')
   
      if not User.objects.filter(username=username).exists():
        messages.error(request, 'Invalid Username')
        return redirect('/login/')
      
      user = authenticate(username = username , password = password)

      if user is None:
         messages.error(request, 'Invalid Password')
         return redirect('/login/')
       
      else:
        
        login(request,user)
        return redirect('/notices/')
   
   return render(request , 'login.html')

def logout_page(request):

    logout(request)
    return redirect('/login/')

def register(request):

   if request.method == "POST":
      first_name = request.POST.get('first_name')
      last_name = request.POST.get('last_name')
      username = request.POST.get('username')
      password = request.POST.get('password')


      user = User.objects.filter(username=username)

      if user.exists():
         messages.info(request, "username already exist.")
         return redirect('/register/')



      user = User.objects.create(
         first_name = first_name,
         last_name = last_name,
         username = username
      )
         
      user.set_password(password)
      user.save()
      messages.info(request, "account created successfuly.")
      return redirect('/register/')

      

    
   return render(request , 'register.html')
   

def home(request):
   return render(request , 'base.html')